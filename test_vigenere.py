import unittest
import random
from unittest import TestCase
from vigenere import encrypt, decrypt


def generate_random_string_of_characters(length):
    # generate random string of characters
    ret_val = ""
    for i in range(length):
        ret_val += chr(random.randint(97, 122))

    return ret_val


class Test(TestCase):
    def test_encrypt(self):
        for i in range(100):
            # get the plain text
            # generate random characters in the alphabets as plain text input
            plain_text = generate_random_string_of_characters(16)

            # get the key
            key = "Vigenere"
            # encrypt the plain text
            cipher_text = encrypt(plain_text, key)
            # assert the cipher text
            decrypted_text = decrypt(cipher_text, key)
            self.assertEqual(plain_text, decrypted_text)

    if __name__ == "__main__":
        unittest.main()
