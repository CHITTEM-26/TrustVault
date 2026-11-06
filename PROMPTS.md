# PROMPTS.md

# TrustVault — AI-Assisted Development Record

**Project:** TrustVault — Secure Document Sharing with a Real Audit Trail  
**Challenge:** Snovasys Fresher Hiring Challenge 2026 — RISE  
**Technology:** Python, Flask, SQLite, HTML, CSS  
**AI Tool:** ChatGPT

## Important Note

This document was prepared retrospectively on November 6, 2026, using my development notes and actual project history. It does not claim to be a record created during each development session.

---

## Entry 1 — Application Structure and Authentication

**Date:** November 2, 2026

**What I asked AI:**  
Help me develop a beginner-friendly Flask application with user registration, login, and secure document management.

**What AI produced:**  
Guidance and code examples for Flask application structure, database models, user authentication, and password hashing.

**What needed improvement:**  
The generated code needed to be integrated into my project and tested in my local environment.

**What I did:**  
I installed the required Python packages, organized the project folders, configured Flask and SQLite, and tested user registration and login.

**Evidence:** Initial project source code commit in the GitHub repository.

---

## Entry 2 — Fixing TemplateNotFound Error

**Date:** November 5, 2026

**What I asked AI:**  
Help me understand and fix the Flask TemplateNotFound error on the registration page.

**What AI produced:**  
An explanation of Flask template loading and the correct template naming.

**What went wrong:**  
The registration template was saved as `register.html.txt` instead of `register.html`.

**What I did:**  
I identified the incorrect file extension, renamed the file to `register.html`, and tested the registration page again.

**Evidence:** Template correction in the project development history.

---

## Entry 3 — Document Sharing and Authorization

**Date:** November 5, 2026

**What I asked AI:**  
Help me implement document sharing and prevent unauthorized users from downloading private documents.

**What AI produced:**  
Guidance and code for document-sharing routes and server-side permission checks.

**What went wrong:**  
The dashboard referred to a `share_document` endpoint that was not available at that stage, causing a Flask BuildError.

**What I did:**  
I corrected the route integration and tested sharing using two different user accounts. I checked that an authorized user could download a shared document and that an unshared document was blocked.

**Evidence:** Document-sharing implementation in the project source code.

---

## Entry 4 — SHA-256 and Audit Trail

**Date:** November 5, 2026

**What I asked AI:**  
Explain how SHA-256 file integrity verification and audit logging can be used in TrustVault.

**What AI produced:**  
Guidance for generating SHA-256 fingerprints and recording important user and document activities.

**What needed improvement:**  
I needed to understand how file integrity verification works and why recording user activities is important for security.

**What I did:**  
I reviewed the implementation and tested the available document and audit features. I learned how SHA-256 fingerprints can help identify file modifications and how audit logs record application activities.

**Evidence:** SHA-256 and audit functionality in the project source code.

---

## Entry 5 — Deployment and Testing

**Date:** November 6, 2026

**What I asked AI:**  
Help me deploy my Flask application on Render and understand deployment errors.

**What AI produced:**  
Guidance for configuring dependencies, the Gunicorn start command, and Render deployment.

**What needed improvement:**  
The application needed to be checked after deployment to ensure that it started and its pages worked correctly.

**What I did:**  
I deployed TrustVault on Render, checked deployment logs, opened the live website, and tested login and dashboard access.

**Evidence:** Live deployment and project repository.

---

## What I Learned

1. AI-generated code must be reviewed and tested before implementation.
2. Authentication and authorization are different security concepts.
3. Server-side permission checks are important for secure document sharing.
4. SHA-256 helps verify file integrity.
5. Audit logs help track important application activities.
6. Debugging errors improved my understanding of Flask.
7. Deployment helped me understand how a web application works online.

## My Responsibility

I used ChatGPT as an AI development assistant for understanding requirements, generating guidance, and troubleshooting errors. I reviewed the suggestions, integrated code into my project, tested the application, and worked on correcting problems.

This project helped me gain practical experience with Python Flask, SQLite, authentication, authorization, document sharing, and deployment.
