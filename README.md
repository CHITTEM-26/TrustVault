# TRUSTVAULT
## Secure Document Sharing with a Real Audit Trail

**SNOVASYS Fresher Hiring Challenge 2026**

### 1. Project Overview

TrustVault is a secure document-sharing web application that allows users to upload, download, and share documents with registered users.

It uses SHA-256 hashing to verify document integrity and maintains an audit trail to record important user activities.

### 2. Project Objectives

- Provide secure user registration and login.
- Allow users to upload and download documents.
- Enable controlled document sharing.
- Verify document integrity using SHA-256.
- Maintain an activity history.
- Provide an Admin Dashboard to monitor system activities.

### 3. Technology Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS
- **Database:** SQLite
- **Authentication:** Flask-Login
- **Password Security:** Werkzeug password hashing
- **File Integrity:** SHA-256

### 4. Main Features

1. User Registration and Login
2. Password Hashing
3. Document Upload
4. Secure Document Download
5. Document Sharing
6. SHA-256 Hash Generation
7. File Integrity Verification
8. User Activity Audit Trail
9. Unauthorized Access Prevention
10. Admin Dashboard

### 5. Security Features

- Passwords are stored as secure hashes.
- Uploaded documents are stored in a private folder.
- Users can access their own documents and documents shared with them.
- Unauthorized document access is blocked.
- SHA-256 hashes are used to detect file modifications.
- Important activities are recorded in the audit trail.

### 6. Project Folder Structure

```text
TrustVault/
│
├── app.py
├── requirements.txt
├── README.md
├── uploads/
├── private_uploads/
├── instance/
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

### 7. Installation and Execution

**Requirements:**
- Windows operating system
- Python installed
- Web browser

**Step 1:** Open Command Prompt.

**Step 2:** Navigate to the project folder.

```cmd
cd /d C:\Users\USER\OneDrive\Desktop\TrustVault
```

**Step 3:** Install dependencies.

```cmd
pip install -r requirements.txt
```

**Step 4:** Run the application.

```cmd
python app.py
```

**Step 5:** Open the browser and visit:

```text
http://127.0.0.1:5000
```

### 8. Testing Results

The following features were tested:

- User registration and login – Successful
- Document upload – Successful
- SHA-256 hash generation – Successful
- Integrity verification – Successful
- Document sharing – Successful
- Shared document download – Successful
- Unauthorized access prevention – Successful
- Admin Dashboard – Successful
- Audit Trail – Successful

### 9. Future Enhancements

- Email notifications
- Two-factor authentication
- Encrypted document storage
- Expiring sharing links
- Advanced audit log protection
- Cloud storage integration

### 10. Conclusion

TrustVault provides a document-sharing platform with access control, file integrity verification, and activity tracking.

The project demonstrates practical implementation of Python Flask, SQLite, authentication, secure file handling, and cybersecurity concepts.

**Project:** TrustVault  
**Challenge:** SNOVASYS Fresher Hiring Challenge 2026  
**Category:** Web Application / Cybersecurity