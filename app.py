import streamlit as st
from cns import remove_duplicates, encrypt_message, decrypt_message

def main():
    st.title("Double Transposition Cipher")

    menu = ["Encrypt a Message", "Decrypt a Message"]
    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Encrypt a Message":
        st.subheader("Encryption")

        message = st.text_input("Enter the message to encrypt:", placeholder="Enter your message here")
        key1 = st.text_input("Enter the first key:", placeholder="Enter first key")
        key2 = st.text_input("Enter the second key:", placeholder="Enter second key")

        if st.button("Encrypt"):
            if not message or not key1 or not key2:
                st.error("Please fill in all fields.")
            else:
                key1_processed = remove_duplicates(key1.upper())
                key2_processed = remove_duplicates(key2.upper())
                encrypted_message = encrypt_message(message.upper().replace(" ", "").replace(".", ""), key1_processed, key2_processed)
                st.success(f"Encrypted Message: {encrypted_message}")

    elif choice == "Decrypt a Message":
        st.subheader("Decryption")

        encrypted_message = st.text_input("Enter the encrypted message to decrypt:", placeholder="Enter encrypted message here")
        key1 = st.text_input("Enter the first key:", placeholder="Enter first key")
        key2 = st.text_input("Enter the second key:", placeholder="Enter second key")

        if st.button("Decrypt"):
            if not encrypted_message or not key1 or not key2:
                st.error("Please fill in all fields.")
            else:
                key1_processed = remove_duplicates(key1.upper())
                key2_processed = remove_duplicates(key2.upper())
                decrypted_message = decrypt_message(encrypted_message.upper(), key1_processed, key2_processed)
                st.success(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
