# Security Hardening Report

## HTTPS and Secure Settings Summary

- **HTTPS Redirect:** Enabled with `SECURE_SSL_REDIRECT = True`.
- **HSTS:** Configured with 1-year expiration, including subdomains and preload.
- **Cookies:** Session and CSRF cookies secured over HTTPS.
- **Headers:**
  - X-Frame-Options: DENY
  - Content-Type No Sniff: Enabled
  - XSS Filter: Enabled

## Deployment Notes

- SSL certificates are required for full HTTPS (suggest Let's Encrypt + Nginx).
- For managed platforms like Heroku, Django's settings enforce security internally.
