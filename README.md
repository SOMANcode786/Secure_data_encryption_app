# Secure Data Encryption System

This is a **Secure Data Encryption System** built with **Streamlit**, **Fernet Encryption** (from the `cryptography` library), and **SHA-256 hashing** to securely store and retrieve data using a passkey.

## Features
- **Data Encryption:** Encrypt user-provided data using a secret passkey.
- **Data Decryption:** Retrieve encrypted data by entering the correct passkey.
- **Master Login:** Reauthorize to reset failed decryption attempts.
- **Protection:** Limits decryption attempts to 3 and redirects to the login page after too many failed attempts.

## Tech Stack
- **Streamlit:** For building the web interface.
- **Cryptography (Fernet):** For encrypting and decrypting data.
- **Hashlib (SHA-256):** For securely hashing the passkeys.
- **Python:** Backend logic and data handling.

## Requirements
Before running the app, make sure to install the required libraries:

```bash
pip install streamlit cryptography
git clone https://github.com/SOMANcode786/secure-data-encryption.git
cd secure-data-encryption
pip install -r requirements.txt
streamlit run secure_app.py

