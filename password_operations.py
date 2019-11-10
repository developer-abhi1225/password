import base64
import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
from salt_operations import Salt
import json
import sys

input_file = "config.json"
output_file = "pass.encrypted"


class Pass:

    @staticmethod
    def encrypt_pass(self, passphrase):
        # STEP 1 :- READ SALT FILE
        # STEP 2 :- GET SALT
        password = passphrase[::-1].encode()
        salt = Salt.decrypt_salt(Salt, passphrase)

        try:
            # STEP 3 :- GENERATE SALT KEY
            kdf = PBKDF2HMAC(
                algorithm=hashes.SHA256(),
                length=32,
                salt=salt,
                iterations=100000,
                backend=default_backend()
            )
            # GENERATING KEY FROM KDF
            key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

            # STEP 4 :- READ INPUT_FILE
            with open(input_file, 'rb') as fo:
                data = fo.read()

            # STEP 5 :- ENCRYPT DATA USING SALT KEY
            enc_data = Fernet(key).encrypt(data)

            # STEP 6 :- WRITE TO OUTPUT FILE
            with open(output_file, 'wb') as fo:
                fo.write(enc_data)

            # STEP 7 :- DELETE INPUT FILE
            #os.remove(input_file)
            print("Passwords encrypted!")

        except Exception as err:
            print("Error generating key while encrypting pass", err)
        return

    @staticmethod
    def decrypt_pass(self, passphrase):

        # STEP 1 :- READ SALT FILE
        # STEP 2 :- GET SALT
        salt = Salt.decrypt_salt(Salt, passphrase)

        if not salt:
            return

        password = passphrase[::-1].encode()

        # STEP 3 :- GENERATE SALT KEY
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=salt,
            iterations=100000,
            backend=default_backend()
        )
        # GENERATING KEY FROM KDF
        key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once

        # STEP 4 :- READ OUTPUT FILE
        with open(output_file, 'rb') as fo:
            enc_data = fo.read()

        # STEP 5 :- DECRYPT DATA USING KEY
        data = Fernet(key).decrypt(enc_data)

        print(json.loads(data))


if __name__ == "__main__":
    p = Pass
    #p.encrypt_pass(p, "bura.html")
    p.decrypt_pass(p, "bura.html")
