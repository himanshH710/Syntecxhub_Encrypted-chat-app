from cryptography.fernet import Fernet

KEY = b'3KHFnm8P5oE0Z590-KbU2wSPnQkNMQEbSgn2-2KjwBM='

cipher = Fernet(KEY)

# Encrypt the message
def encrypt_message(message):
    return cipher.encrypt(message.encode()
    )

# Decrypt the message
def decrypt_message(encrypted_message):
    return cipher.decrypt(
        encrypted_message).decode()