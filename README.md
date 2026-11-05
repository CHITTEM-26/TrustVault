# 🔐 TrustVault
## Secure Document Sharing with a Real Audit Trail

**SNOVASYS Fresher Hiring Challenge 2026**

TrustVault is a secure document-sharing web application built using Python Flask and SQLite. It allows registered users to upload, download, and share documents with controlled permissions.

The application uses SHA-256 hashing to verify document integrity and maintains an audit trail to record important user activities.

---

## 🌐 Live Demo

- **Live Website:** https://trustvault-2i51.onrender.com
- **GitHub Repository:** https://github.com/CHITTEM-26/TrustVault
- **Admin Dashboard:** https://trustvault-2i51.onrender.com/admin

---

## 🎯 Project Objectives

- Provide secure user registration and login.
- Allow users to upload and download documents.
- Enable controlled document sharing.
- Verify document integrity using SHA-256.
- Maintain an activity history through audit logs.
- Provide an Admin Dashboard to monitor system activities.
- Prevent unauthorized document access.

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| Backend | Python, Flask |
| Frontend | HTML, CSS |
| Database | SQLite |
| Authentication | Flask-Login |
| Password Security | Werkzeug |
| File Integrity | SHA-256 |
| Deployment | Render |
| Version Control | GitHub |

---

## ✨ Main Features

1. **User Registration and Login** – Secure account creation and authentication.
2. **Password Hashing** – Passwords are stored as hashes.
3. **Document Upload** – Upload supported documents to private storage.
4. **Secure Document Download** – Download only authorized documents.
5. **Document Sharing** – Share documents with registered users.
6. **SHA-256 Hash Generation** – Generate a unique file fingerprint.
7. **Integrity Verification** – Verify file integrity before downloading.
8. **Audit Trail** – Record important user and document activities.
9. **Unauthorized Access Prevention** – Block users who do not have permission.
10. **Admin Dashboard** – Monitor users, documents, shares, and audit activities.

---

## 🔒 Security Features

- Passwords are protected using Werkzeug password hashing.
- Uploaded documents are stored outside the public static folder.
- Server-side access checks enforce document ownership and sharing permissions.
- Unauthorized download requests are rejected.
- SHA-256 hashes help detect document modifications.
- Important activities are recorded in the audit trail.
- Admin access is restricted to accounts with the admin role.
- Public registration assigns the normal user role.

---

## 📁 Project Structure

```text
TrustVault/
│
├── app.py
├── requirements.txt
├── README.md
│
├── private_uploads/
│
├── instance/
│
├── templates/
│   ├── register.html
│   ├── login.html
│   ├── dashboard.html
│   ├── upload.html
│   ├── audit.html
│   └── admin.html
│
└── static/
```

---

## ⚙️ Installation and Execution

### Requirements

- Windows operating system
- Python 3 installed
- Web browser
- Internet connection for installing dependencies

### Step 1: Clone the repository

```bash
git clone https://github.com/CHITTEM-26/TrustVault.git
```

### Step 2: Open the project folder

```bash
cd TrustVault
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Run the application

```bash
python app.py
```

### Step 5: Open the application

Visit the following address in your browser:

```text
http://127.0.0.1:5000
```

Register an account and log in to start using TrustVault.

---

## 🧪 Testing Results

The following application features were tested:

| Test Case | Result |
|---|---|
| User Registration | Successful |
| User Login | Successful |
| Password Hashing | Successful |
| Document Upload | Successful |
| SHA-256 Hash Generation | Successful |
| File Integrity Verification | Successful |
| Document Sharing | Successful |
| Shared Document Download | Successful |
| Unauthorized Access Prevention | Successful |
| Audit Trail | Successful |
| Admin Dashboard | Successful |

---

## 👨‍💻 Admin Configuration

The Admin account is configured using environment variables in Render.

| Environment Variable | Purpose |
|---|---|
| `ADMIN_EMAIL` | Admin account email |
| `ADMIN_PASSWORD` | Admin account password |
| `ADMIN_NAME` | Admin display name |
| `SECRET_KEY` | Flask application secret |

Admin users can access the Admin Dashboard to monitor registered users, uploaded documents, sharing activities, and audit logs.

**Note:** Never publish secret keys or passwords in the GitHub repository.

---

## 🚀 Deployment

TrustVault is deployed using Render.

**Deployment URL:** https://trustvault-2i51.onrender.com

The application uses the following deployment configuration:

**Build Command**
```bash
pip install -r requirements.txt
```

**Start Command**
```bash
gunicorn app:app
```

---

## 🔮 Future Enhancements

- Email notifications.
- Two-factor authentication.
- Encrypted document storage.
- Expiring document-sharing links.
- Advanced audit log protection.
- Cloud storage integration.
- Persistent database and file storage.

---

## ⚠️ Deployment Note

The current Render free service uses temporary local storage. Database records and uploaded files may not persist across restarts or redeployments without persistent storage or an external database and file-storage service.

Do not upload confidential or sensitive documents to the demonstration application.

---

## 🎓 Conclusion

TrustVault demonstrates the practical implementation of secure document sharing using Python Flask, SQLite, authentication, access control, SHA-256 file integrity verification, and audit logging.

The project highlights important cybersecurity concepts and provides a foundation for developing secure document-management applications.

---

## 📌 Project Information

- **Project Name:** TrustVault
- **Challenge:** SNOVASYS Fresher Hiring Challenge 2026
- **Category:** Web Application / Cybersecurity
- **Project Type:** Full-Stack Web Application
- **Developer:** CHITTEM-26
- **Backend:** Python Flask
- **Database:** SQLite
- **Deployment:** Render

---

**Developed as part of the SNOVASYS Fresher Hiring Challenge 2026.**
