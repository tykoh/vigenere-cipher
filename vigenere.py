"""
A method to take in plain text and a key and encrypt the plain text via vigenere table
"""


def create_vigenere_table():
    # create a vigenere table
    global vigenere_table
    vigenere_table = []
    # loop through the letters of the alphabet
    for i in range(26):
        # create a row
        row = []
        # loop through the letters of the alphabet
        for j in range(26):
            # add the letter of the alphabet to the row
            row.append(chr((i + j) % 26 + ord("A")))
        # add the row to the vigenere table
        vigenere_table.append(row)
    # return the vigenere table
    return vigenere_table


# create a vigenere table
vigenere_table = create_vigenere_table()


def make_letter_same_case(letter, original_letter):
    # check if the original letter is uppercase
    if original_letter.isupper():
        # return the uppercase letter
        return letter.upper()
    else:
        # return the lowercase letter
        return letter.lower()


def is_alphebetical(letter):
    # check if the letter is alphabetical
    if letter.isalpha():
        return True
    else:
        return False


def encrypt(plain_text, key):
    # create a cipher text string
    cipher_text = ""
    key_len = len(key)
    # loop through the plain text
    char_idx = 0
    for i in range(len(plain_text)):
        if is_alphebetical(plain_text[i]):
            # get the row index
            row_index = ord(key[char_idx % key_len].upper()) - ord("A")
            # get the column index
            col_index = ord(plain_text[i].upper()) - ord("A")
            # get the letter from the vigenere table
            letter = vigenere_table[row_index][col_index]
            # add the letter to the cipher text
            cipher_text += make_letter_same_case(letter, plain_text[i])
            char_idx += 1
        else:
            cipher_text += plain_text[i]

    # return the cipher text
    return cipher_text


def decrypt(cipher_text, key):
    # create a plain text string
    plain_text = ""
    key_len = len(key)
    # loop through the cipher text
    char_idx = 0
    for i in range(len(cipher_text)):
        if is_alphebetical(cipher_text[i]):
            # get the row index
            row_index = ord(key[char_idx % key_len].upper()) - ord("A")
            # get the column index
            row = vigenere_table[row_index]
            col_index = row.index(cipher_text[i].upper())
            # get the letter from the vigenere table
            letter = vigenere_table[0][col_index]
            # add the letter to the plain text
            plain_text += make_letter_same_case(letter, cipher_text[i])
            char_idx += 1
        else:
            plain_text += cipher_text[i]

    # return the plain text
    return plain_text


print("Vigenere Cipher. Enter plain text and key to encrypt.")
# add main method
def main():
    # get the plain text
    plain_text = input("Enter plain text: ")
    # get the key
    key = input("Enter key: ")
    # encrypt the plain text
    cipher_text = encrypt(plain_text, key)
    # print the cipher text
    print(f"Cipher text: {cipher_text}")
    # decrypt the cipher text
    plain_text = decrypt(cipher_text, key)
    # print the plain text
    print(f"Plain text: {plain_text}")


if __name__ == "__main__":
    main()
