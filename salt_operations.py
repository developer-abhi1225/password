import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

salt_file = "salt.encrypted"


class Salt:

    def __init__(self):
        self.salt_file = salt_file

    @staticmethod
    def encrypt_salt(self, passphrasae):

        enc_salt = False
        try:
            salt = b'Cr0ssBar==2.1.0'
            password = passphrasae[::-1].encode()
            salt_key = base64.urlsafe_b64encode(PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            ).derive(password))
            enc_salt = Fernet(salt_key).encrypt(os.urandom(16))
        except Exception as err:
            print("error in encrypting salt", err)
        return enc_salt

    @staticmethod
    def save_salt(self, passphrase):
        try:

            enc_salt = self.encrypt_salt(self, passphrase)  # CHANGE IT TO API BODY PARAMETERS
            with open(salt_file, 'wb') as fo:
                fo.write(enc_salt)

        except Exception as err:
            print("Error while storing salt", err)

    @staticmethod
    def decrypt_salt(self, passphrase):
        dec_salt = ''
        try:

            with open(salt_file, 'rb') as fo:
                enc_salt = fo.read()

            salt = b'Cr0ssBar==2.1.0'
            password = passphrase[::-1].encode()
            salt_key = base64.urlsafe_b64encode(PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            ).derive(password))
            dec_salt = Fernet(salt_key).decrypt(enc_salt)
            print(dec_salt)
        except Exception as err:
            print("error in encrypting salt", err)

        return dec_salt


if __name__ == "__main__":

    s = Salt()
    s.save_salt(s, "bura.html")
    s.decrypt_salt(s,"bura.html")
