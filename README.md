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

```
How to Use the Application
1. Home Page
On the Home page, you will be greeted with a welcome message and a brief description of the app.

2. Store Data
In this section, you can input the data you want to store securely.

You will need to provide a passkey to encrypt and save the data.

Once encrypted, the app will store the encrypted data, and you can use it later to retrieve the data.

3. Retrieve Data
To retrieve your stored data, enter the encrypted data and the passkey you used during encryption.

If the passkey is correct, the app will decrypt the data and display it.

If there are 3 failed decryption attempts, the app will redirect you to the Login Page for reauthorization.

4. Login Page
The Login Page requires a master password to reset failed decryption attempts and proceed with the app's usage.

The default master password is "admin123" (for demo purposes). You should replace this with a more secure authentication method in production.

How the System Works
Encryption:

When data is stored, the system hashes the passkey using SHA-256 and encrypts the data using the Fernet encryption method.

Both the encrypted data and the hashed passkey are saved in-memory.

Decryption:

When you try to retrieve your data, the system compares the passkey against the stored hashed passkey.

If they match, the encrypted data is decrypted and shown.

Failed Attempts:

The system limits the number of decryption attempts to 3.

After 3 failed attempts, the system will redirect to the Login Page for reauthorization to protect against brute-force attacks.

Security Considerations
Encryption Key:

The secret encryption key (secret.key) is generated dynamically during runtime. In a production environment, this key should be securely stored and managed.

Passkey Management:

The passkeys are hashed using SHA-256, meaning the raw passkey is never stored, improving security.

Protection from Brute Force:

After 3 failed decryption attempts, the system will block further access and redirect the user to the Login Page.

Customization
Master Password:

The current master password is hardcoded as "admin123". You should replace it with a more secure, dynamic password authentication mechanism for production use.

Key Storage:

The encryption key is stored temporarily in memory. You should consider using a secure key management system for storing it securely in production.

Future Improvements
User Authentication:

Implement user-specific authentication (e.g., username and password) for multiple users with separate data storage.

Database Support:

Replace in-memory storage with a secure database to store user data persistently.

Cloud Deployment:

Deploy the application on platforms like Streamlit Cloud or other cloud services for wider accessibility.

License
This project is licensed under the MIT License.

