from cryptography.fernet import Fernet
def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    g = open('encoded.file','wb')
    g.write(encrypted_message)

if __name__ == "__main__":
    encrypt_message("encrypt this message")

def decrypt_message(message):

        key = load_key()
        f = Fernet(key)
        g = open('decrypted.mp4', 'wb')
        g.write(f.decrypt(message))
