import streamlit as st
import hashlib
from cryptography.fernet import Fernet
import os

# Load or generate encryption key
def load_key():
    if os.path.exists("secret.key"):
        with open("secret.key", "rb") as file:
            return file.read()
    else:
        key = Fernet.generate_key()
        with open("secret.key", "wb") as file:
            file.write(key)
        return key

KEY = load_key()
cipher = Fernet(KEY)

# Initialize session state variables
if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}  # {encrypted_text: {"passkey": hashed_passkey}}

if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = 0

if 'redirected' not in st.session_state:
    st.session_state.redirected = False

if 'is_logged_in' not in st.session_state:
    st.session_state.is_logged_in = False

# Hash passkey
def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt data
def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

# Decrypt data
def decrypt_data(encrypted_text, passkey):
    hashed = hash_passkey(passkey)
    data_entry = st.session_state.stored_data.get(encrypted_text)

    if data_entry and data_entry["passkey"] == hashed:
        st.session_state.failed_attempts = 0
        st.session_state.redirected = False  # Reset redirect state after success
        return cipher.decrypt(encrypted_text.encode()).decode()
    else:
        st.session_state.failed_attempts += 1
        return None

# Stylish Header
st.markdown("""
    <style>
        h1 {
            text-align: center;
            color: #4CAF50;
            font-size: 36px;
            font-weight: bold;
        }
        h2 {
            color: #0078d4;
        }
        .stTextArea textarea {
            border-radius: 8px;
            padding: 10px;
        }
        .stButton button {
            background-color: #4CAF50;
            color: white;
            border-radius: 8px;
            padding: 10px 20px;
        }
    </style>
    <h1>🔐 Secure Data Encryption System</h1>
    <p style='text-align: center; font-size: 18px; color: #8B8B8B;'>Developed by <strong>Muhammad Soman Amir</strong></p>
""", unsafe_allow_html=True)

# Rerun protection: redirect after 3 failed attempts
if st.session_state.failed_attempts >= 3 and not st.session_state.redirected:
    st.session_state.redirected = True
    st.rerun()

# Navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("📂 Navigation", menu)

# Home Page
if choice == "Home":
    st.subheader("🏠 Welcome to the Secure Data System")
    st.write("Use this app to **securely store and retrieve data** using encryption and passkeys.")
    st.markdown("🔐 Built with Python, Streamlit, and cryptography.")
    if st.session_state.is_logged_in:
        st.success("🟢 You are logged in. Only retrieval is allowed.")
    else:
        st.info("🔒 Please log in to access the full features.")

# Store Data
elif choice == "Store Data":
    if st.session_state.is_logged_in:
        st.subheader("📦 Store Your Data Securely")
        user_data = st.text_area("Enter Data to Encrypt:", height=150)
        passkey = st.text_input("Create a Passkey:", type="password")

        if st.button("🔐 Encrypt & Save", disabled=not (user_data and passkey)):
            hashed_pass = hash_passkey(passkey)
            encrypted = encrypt_data(user_data)
            st.session_state.stored_data[encrypted] = {"passkey": hashed_pass}
            st.success("✅ Data encrypted and stored successfully!")
            st.code(encrypted, language="text")
    else:
        st.warning("⚠️ Please log in first to store data.")
        st.write("You need to log in to store and encrypt data. Please use the Login option in the sidebar.")

# Retrieve Data
elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Your Data")

    encrypted_text = st.text_area("Paste Encrypted Data:")
    passkey = st.text_input("Enter Your Passkey:", type="password")

    if st.button("🔓 Decrypt", disabled=not (encrypted_text and passkey)):
        decrypted = decrypt_data(encrypted_text, passkey)

        if decrypted:
            st.success("✅ Data Decrypted Successfully!")
            st.code(decrypted, language="text")
        else:
            remaining = max(0, 3 - st.session_state.failed_attempts)
            st.error(f"❌ Incorrect passkey! Attempts remaining: {remaining}")

            if st.session_state.failed_attempts >= 3:
                st.warning("🔒 Too many failed attempts! Redirecting to Login Page...")
                st.rerun()

# Login Page
elif choice == "Login":
    st.subheader("🔑 Admin Login")

    master_password = st.text_input("Enter Master Password:", type="password")

    if st.button("Login"):
        if master_password == "admin123":  # Replace with secure logic in real app
            st.session_state.failed_attempts = 0
            st.session_state.redirected = False
            st.session_state.is_logged_in = True
            st.success("✅ Logged in successfully!")
        else:
            st.error("❌ Incorrect master password.")

# Optional logout button
st.sidebar.markdown("---")
if st.session_state.is_logged_in:
    if st.sidebar.button("🚪 Logout"):
        st.session_state.is_logged_in = False
        st.success("🔁 Logged out. You can now store new data again.")
        st.rerun()
