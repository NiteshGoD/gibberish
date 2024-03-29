"""Test Scripts"""
import pytest
import os
import source.my_functions as my_functions
from source import Encryptor

def test_add():
    result = my_functions.add(a = 1, b = 5)
    assert result == 6
    
def test_txt_encryption():
    print("PRESENT WORKING DIRECTORY: ", os.getcwd())
    txt_to_encrypt = "Secret"
    encryptor = Encryptor()
    encrypted_txt = encryptor.encrypt_txt(txt_to_encrypt)
    decrypted_txt = encryptor.decrypt_txt(encrypted_txt)
    assert txt_to_encrypt == decrypted_txt
