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
git clone https://github.com/yourusername/secure-data-encryption.git
cd secure-data-encryption
pip install -r requirements.txt
streamlit run secure_app.py
How to Use
1. Home Page
On the Home page, you are greeted with a welcome message and an introduction to the app.

2. Store Data
You can enter any data you want to store securely.

You need to provide a passkey to encrypt and save your data.

The system will display the encrypted data that you can later use to retrieve it.

3. Retrieve Data
To retrieve encrypted data, enter the encrypted data and the correct passkey.

If the passkey is correct, the data will be decrypted and shown.

After 3 failed attempts to decrypt, the system will redirect you to the Login Page for reauthorization.

4. Login Page
A master password ("admin123") is required to reset failed attempts and continue with the system.

How it Works
Encryption:

When you store data, the passkey is hashed using SHA-256, and the data is encrypted using the Fernet encryption method.

Both the encrypted data and the hashed passkey are stored in an in-memory session.

Decryption:

When you attempt to retrieve data, the system checks the passkey against the stored hash.

If it matches, the encrypted data is decrypted and displayed.

Security Measures:

The system limits failed decryption attempts to 3.

After 3 failed attempts, it will redirect to the login page to reset the attempts.

Security Considerations
Encryption Key:

The secret encryption key (secret.key) is saved locally. In production, this key should be stored securely (e.g., in a secret management system).

Passkey Management:

The passkeys are securely hashed (using SHA-256), and the raw passkey is never stored.

Redirect Protection:

After 3 failed decryption attempts, the system will automatically redirect to the login page to prevent brute-force attacks.

Customization
Master Password:

The current master password is hardcoded as "admin123". For better security, you should replace it with a more secure, dynamic password authentication mechanism.

Key Storage:

The encryption key (secret.key) is saved in the project directory for simplicity. In production, store it securely.

Future Improvements
User Authentication:

Implement user authentication (e.g., username and password) to allow multiple users with separate data.

Database Support:

Store data securely in a database instead of in-memory, so data persists across sessions.

Cloud Deployment:

Deploy the application on Streamlit Cloud or any cloud platform to make it accessible from anywhere.

License
This project is licensed under the MIT License.
