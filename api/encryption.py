#This is a temparary solution, the end solution will be using zero knowledge
from Crypto.Cipher import AES
import base64

SECRET_KEY = 'your_very_secret_key'  # TODO add key

def encrypt_message(message):
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX)
    nonce = cipher.nonce
    ciphertext, tag = cipher.encrypt_and_digest(message.encode('utf-8'))
    return base64.b64encode(nonce + tag + ciphertext).decode('utf-8')

def decrypt_message(encrypted_message):
    decoded_message = base64.b64decode(encrypted_message)
    nonce, tag, ciphertext = decoded_message[:16], decoded_message[16:32], decoded_message[32:]
    cipher = AES.new(SECRET_KEY, AES.MODE_EAX, nonce=nonce)
    return cipher.decrypt_and_verify(ciphertext, tag).decode('utf-8')

# TODO encryption and decryption errors handeling
