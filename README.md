# vigenere-cipher
The Vigenère cipher uses a simple form of polyalphabetic substitution. A polyalphabetic cipher is any cipher based on substitution using multiple offset alphabets. The source text is encrypted using the Vigenère table. The table consists of alphabets (array of characters) written out 26 times in different rows (for English alphabet), each alphabet is cyclically shifted to the left compared to the previous alphabet.
	



The encryption is done as follows:
Ci = (P i+ Kj) mod 26,
where Kj is the j-th letter of the key, 
Pi is і-th letter of the original message, and
Ci is the i-th letter of the ciphertext.

Pseudo-code:

```text
m <-- length of key 
for index, character in plaintext:
    ciphertext[index] <-- (character + key[index % m]) % 26


return ciphertext

```
