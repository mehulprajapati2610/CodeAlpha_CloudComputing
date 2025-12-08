import os
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from dotenv import load_dotenv

load_dotenv()
KEY = base64.b64decode(os.getenv("AES_KEY_BASE64"))

def encrypt(text):
    cipher = AES.new(KEY, AES.MODE_CBC)
    ct = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + ct).decode()

def decrypt(enc_text):
    data = base64.b64decode(enc_text)
    iv = data[:16]
    ct = data[16:]
    cipher = AES.new(KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(ct), AES.block_size).decode()
