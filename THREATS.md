# THREATS.md

# TrustVault — Security Threat Analysis

## 1. Introduction

TrustVault is a secure document-sharing application developed using Python Flask and SQLite.

This document identifies possible security threats, the protections implemented in the application, and areas that need further improvement.

## 2. Identified Security Threats

### Threat 1: Unauthorized Document Access

**Risk:** A user may try to access another user's private documents.

**Protection:** TrustVault checks document ownership and sharing permissions on the server before allowing access.

**Status:** Implemented; tested with separate user accounts.

### Threat 2: Unauthorized Document Downloads

**Risk:** Someone may change a document ID in a download URL to access a document without permission.

**Protection:** Server-side authorization checks are used before downloading documents.

**Status:** Implemented; unauthorized access was tested.

### Threat 3: Password Theft

**Risk:** Attackers may try to obtain user passwords.

**Protection:** TrustVault uses Werkzeug password hashing instead of storing plain-text passwords.

**Status:** Password hashing implemented. Two-factor authentication is a future improvement.

### Threat 4: Malicious File Uploads

**Risk:** Attackers may upload unsupported or potentially harmful files.

**Protection:** TrustVault restricts supported file extensions and limits uploads to 10 MB.

**Status:** Basic file validation implemented. Strong content inspection and malware scanning are future improvements.

### Threat 5: File Tampering

**Risk:** A document may be modified after upload.

**Protection:** SHA-256 fingerprints are used to help verify document integrity.

**Status:** SHA-256 functionality implemented. Verification should be tested against modified files.

### Threat 6: Unauthorized Document Sharing

**Risk:** A user may try to share documents they do not own.

**Protection:** Document-sharing operations should verify ownership and the intended recipient on the server.

**Status:** Basic sharing implemented and tested. Further authorization testing is recommended.

### Threat 7: Audit Log Manipulation

**Risk:** A user may attempt to modify or delete activity records.

**Protection:** TrustVault records important user and document activities in an audit trail.

**Status:** Audit logging implemented. Tamper-resistant or externally stored logs are future improvements.

### Threat 8: Session Security

**Risk:** An attacker may try to misuse an authenticated user's session.

**Protection:** TrustVault uses Flask-Login to manage authenticated sessions.

**Status:** Basic session management implemented. Additional cookie security settings and session-hardening tests are recommended.

## 3. Security Testing

The following checks were performed during development:

| Test | Result |
|---|---|
| User registration and login | Tested |
| Password hashing | Tested |
| Document upload | Tested |
| Authorized document download | Tested |
| Unauthorized document download | Tested |
| Document sharing | Tested |
| Audit trail | Tested |
| Admin dashboard access | Tested |

These results describe the development tests performed. They do not represent a complete professional security audit.

## 4. Known Limitations

- No two-factor authentication.
- No malware scanning for uploaded files.
- No dedicated encryption-at-rest implementation.
- No permanent cloud file storage.
- Audit logs are not protected against all forms of tampering.
- Additional automated security tests are required.

## 5. Future Security Improvements

- Implement two-factor authentication.
- Add malware scanning and stronger file validation.
- Improve encryption and secure key management.
- Use persistent cloud database and file storage.
- Protect audit logs against unauthorized modification.
- Add automated authorization and security tests.
- Improve session and cookie security.

## 6. Conclusion

TrustVault demonstrates important security concepts, including authentication, server-side authorization, controlled document sharing, SHA-256 file integrity verification, and audit logging.

Security is an ongoing process. Identifying threats, testing protections, and improving known limitations are important steps toward building a more secure application.
