

import os
import uuid
import hashlib

from flask import (
    Flask, render_template, request, redirect,
    url_for, flash, send_from_directory, abort
)

from flask_sqlalchemy import SQLAlchemy

from flask_login import (
    LoginManager, UserMixin, login_user,
    login_required, logout_user, current_user
)

from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename

from email_validator import validate_email, EmailNotValidError
from sqlalchemy import inspect, text


# ==================================
# APPLICATION CONFIGURATION
# ==================================

app = Flask(__name__)

app.config["SECRET_KEY"] = "change-this-local-development-secret"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trustvault.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["MAX_CONTENT_LENGTH"] = 10 * 1024 * 1024

UPLOAD_FOLDER = os.path.join(app.root_path, "private_uploads")

os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "docx", "png", "jpg", "jpeg"}

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"


# ==================================
# USER MODEL
# ==================================

class User(UserMixin, db.Model):

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    role = db.Column(
        db.String(20),
        default="user",
        nullable=False
    )


# ==================================
# DOCUMENT MODEL
# ==================================

class Document(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    original_name = db.Column(db.String(255), nullable=False)

    stored_name = db.Column(db.String(255), nullable=False)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    # SHA-256 hash of the uploaded document
    sha256_hash = db.Column(db.String(64), nullable=True)


# ==================================
# DOCUMENT SHARE MODEL
# ==================================

class DocumentShare(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    document_id = db.Column(
        db.Integer,
        db.ForeignKey("document.id"),
        nullable=False
    )

    shared_with_email = db.Column(db.String(120), nullable=False)

    permission = db.Column(
        db.String(20),
        default="download",
        nullable=False
    )


# ==================================
# AUDIT LOG MODEL
# ==================================

class AuditLog(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    document_id = db.Column(
        db.Integer,
        db.ForeignKey("document.id"),
        nullable=True
    )

    action = db.Column(db.String(100), nullable=False)

    details = db.Column(db.String(255))

    timestamp = db.Column(
        db.DateTime,
        default=db.func.now(),
        nullable=False
    )


# ==================================
# SHA-256 FILE HASH FUNCTION
# ==================================

def calculate_file_hash(file_path):

    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:

        for chunk in iter(lambda: file.read(4096), b""):

            sha256.update(chunk)

    return sha256.hexdigest()


# ==================================
# AUDIT RECORDING FUNCTION
# ==================================

def record_audit(action, document_id=None, details=""):

    try:

        log = AuditLog(
            user_id=current_user.id,
            document_id=document_id,
            action=action,
            details=details
        )

        db.session.add(log)
        db.session.commit()

    except Exception:

        db.session.rollback()

        app.logger.exception("Could not save audit log")


# ==================================
# LOAD USER
# ==================================

@login_manager.user_loader
def load_user(user_id):

    return db.session.get(User, int(user_id))


# ==================================
# FILE EXTENSION CHECK
# ==================================

def allowed_file(filename):

    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


# ==================================
# HOME
# ==================================

@app.route("/")
def home():

    return redirect(url_for("login"))


# ==================================
# REGISTRATION
# ==================================

@app.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form.get("name", "").strip()

        email = request.form.get("email", "").strip().lower()

        password = request.form.get("password", "")

        if not name or not email or not password:

            flash("All fields are required.")

            return redirect(url_for("register"))

        try:

            validate_email(
                email,
                check_deliverability=False
            )

        except EmailNotValidError:

            flash("Please enter a valid email address.")

            return redirect(url_for("register"))

        if len(password) < 8:

            flash("Password must contain at least 8 characters.")

            return redirect(url_for("register"))

        if User.query.filter_by(email=email).first():

            flash("Email already registered.")

            return redirect(url_for("register"))

        user = User(
            name=name,
            email=email,
            password=generate_password_hash(password),
            role="user"
        )

        db.session.add(user)

        db.session.commit()

        flash("Registration successful. Please login.")

        return redirect(url_for("login"))

    return render_template("register.html")


# ==================================
# LOGIN
# ==================================

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email", "").strip().lower()

        password = request.form.get("password", "")

        user = User.query.filter_by(email=email).first()

        if user and check_password_hash(user.password, password):

            login_user(user)

            record_audit(
                "LOGIN",
                details="User logged in"
            )

            return redirect(url_for("dashboard"))

        flash("Invalid email or password.")

    return render_template("login.html")


# ==================================
# DASHBOARD
# ==================================

@app.route("/dashboard")
@login_required
def dashboard():

    documents = Document.query.filter_by(
        user_id=current_user.id
    ).all()

    shared_documents = (
        Document.query
        .join(
            DocumentShare,
            Document.id == DocumentShare.document_id
        )
        .filter(
            DocumentShare.shared_with_email == current_user.email
        )
        .all()
    )

    return render_template(
        "dashboard.html",
        user=current_user,
        documents=documents,
        shared_documents=shared_documents
    )


# ==================================
# UPLOAD DOCUMENT
# ==================================

@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload():

    if request.method == "POST":

        if "document" not in request.files:

            flash("No file selected.")

            return redirect(url_for("upload"))

        file = request.files["document"]

        if file.filename == "":

            flash("Please select a file.")

            return redirect(url_for("upload"))

        if not allowed_file(file.filename):

            flash("Only PDF, DOCX, PNG, JPG and JPEG files are allowed.")

            return redirect(url_for("upload"))

        original_name = secure_filename(file.filename)

        if not original_name:

            flash("Invalid filename.")

            return redirect(url_for("upload"))

        stored_name = str(uuid.uuid4()) + "_" + original_name

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            stored_name
        )

        file.save(file_path)

        # Calculate SHA-256 hash
        file_hash = calculate_file_hash(file_path)

        document = Document(
            original_name=original_name,
            stored_name=stored_name,
            user_id=current_user.id,
            sha256_hash=file_hash
        )

        db.session.add(document)

        db.session.commit()

        record_audit(
            "DOCUMENT_UPLOADED",
            document.id,
            "Uploaded: " + original_name
        )

        record_audit(
            "SHA256_GENERATED",
            document.id,
            "SHA-256: " + file_hash
        )

        flash("Document uploaded and SHA-256 hash generated successfully!")

        return redirect(url_for("dashboard"))

    return render_template("upload.html")


# ==================================
# SHARE DOCUMENT
# ==================================

@app.route("/share/<int:document_id>", methods=["POST"])
@login_required
def share_document(document_id):

    document = Document.query.filter_by(
        id=document_id,
        user_id=current_user.id
    ).first()

    if document is None:

        abort(404)

    recipient_email = request.form.get(
        "email", ""
    ).strip().lower()

    try:

        validate_email(
            recipient_email,
            check_deliverability=False
        )

    except EmailNotValidError:

        flash("Please enter a valid recipient email.")

        return redirect(url_for("dashboard"))

    recipient = User.query.filter_by(
        email=recipient_email
    ).first()

    if recipient is None:

        flash("This email is not registered.")

        return redirect(url_for("dashboard"))

    if recipient.id == current_user.id:

        flash("You cannot share a document with yourself.")

        return redirect(url_for("dashboard"))

    existing_share = DocumentShare.query.filter_by(
        document_id=document.id,
        shared_with_email=recipient_email
    ).first()

    if existing_share:

        flash("Document already shared with this user.")

        return redirect(url_for("dashboard"))

    share = DocumentShare(
        document_id=document.id,
        shared_with_email=recipient_email,
        permission="download"
    )

    db.session.add(share)

    db.session.commit()

    record_audit(
        "DOCUMENT_SHARED",
        document.id,
        "Shared with: " + recipient_email
    )

    flash("Document shared successfully!")

    return redirect(url_for("dashboard"))


# ==================================
# SECURE DOCUMENT DOWNLOAD
# ==================================

@app.route("/download/<int:document_id>")
@login_required
def download_document(document_id):

    document = db.session.get(Document, document_id)

    if document is None:

        abort(404)

    is_owner = document.user_id == current_user.id

    has_permission = DocumentShare.query.filter_by(
        document_id=document.id,
        shared_with_email=current_user.email,
        permission="download"
    ).first() is not None

    if not is_owner and not has_permission:

        abort(403)

    file_path = os.path.join(
        app.config["UPLOAD_FOLDER"],
        document.stored_name
    )

    if not os.path.isfile(file_path):

        abort(404)

    # Verify file integrity
    current_hash = calculate_file_hash(file_path)

    if not document.sha256_hash:

        flash("Document has no saved SHA-256 hash. Contact the administrator.")

        record_audit(
            "INTEGRITY_CHECK_FAILED",
            document.id,
            "No saved SHA-256 hash"
        )

        abort(409)

    if current_hash != document.sha256_hash:

        record_audit(
            "INTEGRITY_CHECK_FAILED",
            document.id,
            "Document hash mismatch. Possible file modification."
        )

        abort(409)

    record_audit(
        "INTEGRITY_VERIFIED",
        document.id,
        "SHA-256 integrity check passed"
    )

    record_audit(
        "DOCUMENT_DOWNLOADED",
        document.id,
        "Downloaded: " + document.original_name
    )

    return send_from_directory(
        app.config["UPLOAD_FOLDER"],
        document.stored_name,
        as_attachment=True,
        download_name=document.original_name
    )


# ==================================
# USER AUDIT TRAIL
# ==================================

@app.route("/audit")
@login_required
def audit():

    logs = (
        AuditLog.query
        .filter_by(user_id=current_user.id)
        .order_by(AuditLog.timestamp.desc())
        .all()
    )

    return render_template(
        "audit.html",
        logs=logs
    )


# ==================================
# ADMIN DASHBOARD
# ==================================

@app.route("/admin")
@login_required
def admin_dashboard():

    if current_user.role != "admin":

        abort(403)

    total_users = User.query.count()

    total_documents = Document.query.count()

    total_shares = DocumentShare.query.count()

    logs = (
        db.session.query(AuditLog, User)
        .join(User, AuditLog.user_id == User.id)
        .order_by(AuditLog.timestamp.desc())
        .all()
    )

    users = User.query.order_by(User.id.desc()).all()

    return render_template(
        "admin.html",
        total_users=total_users,
        total_documents=total_documents,
        total_shares=total_shares,
        logs=logs,
        users=users
    )


# ==================================
# LOGOUT
# ==================================

@app.route("/logout")
@login_required
def logout():

    record_audit(
        "LOGOUT",
        details="User logged out"
    )

    logout_user()

    return redirect(url_for("login"))


# ==================================
# FILE SIZE ERROR
# ==================================

@app.errorhandler(413)
def file_too_large(error):

    flash("File is too large. Maximum size is 10 MB.")

    return redirect(url_for("upload"))


# ==================================
# CREATE AND UPDATE DATABASE
# ==================================

with app.app_context():

    db.create_all()

    # Add SHA-256 column to an existing database if necessary
    columns = inspect(db.engine).get_columns("document")

    column_names = [column["name"] for column in columns]

    if "sha256_hash" not in column_names:

        with db.engine.begin() as connection:

            connection.execute(
                text(
                    "ALTER TABLE document ADD COLUMN sha256_hash VARCHAR(64)"
                )
            )

    # Generate hashes for existing documents
    old_documents = Document.query.filter(
        Document.sha256_hash.is_(None)
    ).all()

    for document in old_documents:

        file_path = os.path.join(
            app.config["UPLOAD_FOLDER"],
            document.stored_name
        )

        if os.path.isfile(file_path):

            document.sha256_hash = calculate_file_hash(file_path)

    db.session.commit()


# ==================================
# RUN APPLICATION
# ==================================

if __name__ == "__main__":

    app.run(debug=True)
