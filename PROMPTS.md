# PROMPTS.md

## AI-Assisted Development Record — TrustVault

**Project:** TrustVault — Secure Document Sharing with a Real Audit Trail  
**Technology:** Python, Flask, SQLite, HTML, CSS  
**AI Tool Used:** ChatGPT

**Note:** This record was prepared retrospectively on November 6, 2026, from my development notes and actual project issues. The entries summarize my AI-assisted development process.

---

### Entry 1 — Application Structure and Authentication

**Date:** November 2, 2026

**What I asked:**  
Help me build a beginner-friendly Flask application for secure document sharing with user registration and login.

**What the AI produced:**  
A Flask application structure with user authentication, database models, password hashing, and login and registration pages.

**What was wrong or needed improvement:**  
Some generated code and template setup needed to be integrated and tested in my project environment.

**What I did instead:**  
I installed the required packages, organized the project files, configured Flask and SQLite, and tested registration and login.

**Commit:** [Insert the actual GitHub commit URL]

---

### Entry 2 — Fixing TemplateNotFound

**Date:** November 5, 2026

**What I asked:**  
Help me fix the Flask TemplateNotFound error for the registration page.

**What the AI produced:**  
An explanation of Flask template loading and the correct template filename.

**What was wrong:**  
The registration template had accidentally been saved as `register.html.txt` instead of `register.html`.

**What I did instead:**  
I identified the incorrect file extension and renamed the file to `register.html`. I then tested the registration page again.

**Commit:** [Insert the actual GitHub commit URL]

---

### Entry 3 — Document Sharing and Authorization

**Date:** November 5, 2026

**What I asked:**  
Help me implement secure document sharing and prevent unauthorized users from downloading documents.

**What the AI produced:**  
A document-sharing route and permission-checking logic for download access.

**What was wrong or needed improvement:**  
The dashboard referred to a `share_document` endpoint that was not available at that stage, causing a Flask BuildError.

**What I did instead:**  
I corrected the route integration and tested document sharing using two different user accounts. I checked that an authorized user could download a shared document and that an unshared document was blocked.

**Commit:** [Insert the actual GitHub commit URL]

---

### Entry 4 — Audit Trail and File Integrity

**Date:** November 5, 2026

**What I asked:**  
Help me understand and implement SHA-256 file integrity verification and audit logging.

**What the AI produced:**  
Guidance for generating a SHA-256 fingerprint for uploaded files and recording document-related activities in an audit log.

**What was wrong or needed improvement:**  
I needed to understand how to verify file integrity and how audit records help track activities rather than simply display messages.

**What I did instead:**  
I reviewed the implementation and tested the available document and audit features. I used the audit trail to track recorded activities and the SHA-256 fingerprint to check file integrity.

**Commit:** [Insert the actual GitHub commit URL]

---

### Entry 5 — Deployment and Testing

**Date:** November 6, 2026

**What I asked:**  
Help me deploy my Flask application using Render and troubleshoot deployment problems.

**What the AI produced:**  
Deployment guidance for configuring the Flask application, dependencies, and Gunicorn server.

**What was wrong or needed improvement:**  
I needed to verify that the deployed application started correctly and that its pages worked after deployment.

**What I did instead:**  
I deployed TrustVault on Render, checked the deployment logs, opened the live website, and tested login and dashboard access.

**Commit:** [Insert the actual GitHub commit URL]

---

## What I Learned

- AI-generated code must be reviewed and tested before using it.
- Authentication and authorization are different security concepts.
- Server-side permission checks are important for secure document sharing.
- Audit logs help track application activities.
- SHA-256 can help verify file integrity.
- Debugging and deployment helped me understand how a Flask application works.

**My Responsibility:** I used AI as a development assistant, reviewed the suggestions, tested the application, identified problems, and worked on corrections.
