"""Script for Symmetric Encryption text"""
from cryptography.fernet import Fernet

class Encryptor():
    """Text Encryptor
    """
    def __init__(self,key = Fernet.generate_key()):
        self.key = key
        self.fernet = Fernet(self.key)
        self.encrypted_byte_string = None
        self.decrypted_byte_string = None
    
    def encrypt_txt(self,txt : str):
        """Encrypts the string and returns the encrypted txt"""
        txt_byte_string = txt.encode()
        encrypted_byte_string = self.fernet.encrypt(txt_byte_string)
        return encrypted_byte_string.decode()
    
    def decrypt_txt(self, txt_to_decrypt: str ):
        """Decrypts the encrypted text"""
        decrypted_byte_str = self.fernet.decrypt(txt_to_decrypt.encode())
        return decrypted_byte_str.decode()

# key = Fernet.generate_key()
# f = Fernet(key)
# msg_to_encrypt = "THIS IS A SECRET!"
# token = f.encrypt(msg_to_encrypt.encode())
# print(token.decode())
# print("DECRYPTED: ",f.decrypt(token).decode())
