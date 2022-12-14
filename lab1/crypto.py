#!/usr/bin/env python3 -tt
"""
File: crypto.py
---------------
Assignment 1: Cryptography
Course: CS 41
Name: Gyorgy Viktor
SUNet: ????????

Replace this with a description of the program.
"""
from winsound import PlaySound
import utils
import math

# Caesar Cipher
caesar_key = 3

def encrypt_caesar(plaintext : str):
    newText = []
    for char in plaintext:
        if char.isalpha():
            char = ((ord(char) - ord('A')) + caesar_key) % 26 + ord('A')
        newText.append(chr(char))
    return ''.join(newText)


def decrypt_caesar(ciphertext : str):
    newText = []
    for char in ciphertext:
        if char.isalpha():
            char = ((ord(char) - ord('A')) - caesar_key) % 26 + ord('A')
        newText.append(chr(char))
    return ''.join(newText)

def encrypt_caesar_file(plainbytes : bytes):
    key = 5
    newbytes = bytearray(plainbytes)
    for i in range(len(plainbytes)):
        newbytes[i] = (int(plainbytes[i]) + key) % 256
    return newbytes

def decrypt_caesar_file(cipherbytes : bytes):
    key = 5
    newbytes = bytearray(cipherbytes)
    for i in range(len(cipherbytes)):
        newbytes[i] = (int(cipherbytes[i]) - key) % 256
    return newbytes
    
    

# Vigenere Cipher

def encrypt_vigenere(plaintext: str, keyword: str):
    newText = []
    i = 0
    for char in plaintext:
        if char.isalpha():
            k = keyword[i]
            char = ((ord(char) - ord('A')) + (ord(k) - ord('A'))) % 26 + ord('A')
        newText.append(chr(char))
        i = (i + 1) % len(keyword)
    return ''.join(newText)


def decrypt_vigenere(ciphertext, keyword):
    newText = []
    i = 0
    for char in ciphertext:
        if char.isalpha():
            k = keyword[i]
            char = ((ord(char) - ord('A')) - (ord(k) - ord('A'))) % 26 + ord('A')
        newText.append(chr(char))
        i = (i + 1) % len(keyword)
    return ''.join(newText)

def encrypt_scytale(plaintext: str, circumference: int):
    chars = []
    n = len(plaintext)

    for i in range(circumference):
        chars = chars + [plaintext[i + circumference * j] for j in range(math.floor(n / circumference) + (i < n % circumference))]

    return ''.join(chars)

def decrypt_scytale(ciphertext, circumference):
    n = len(ciphertext)
    chars = ["" for _ in range(circumference)]
    
    index = 0
    for i in range(circumference):
        for j in range(math.floor(n / circumference) + (i < n % circumference)):
            chars[i] = chars[i] + ciphertext[index]
            
            index += 1

    solution = ""

    for j in range(math.ceil(n / circumference)):
        for i in range(circumference):
            if j >= len(chars[i]):
                continue
            
            solution += chars[i][j]

    return solution

def encrypt_railfence(plaintext, num_rails):
    strings = ["" for _ in range(num_rails)]

    i = 0
    it = 1
    for char in plaintext:
        strings[i] += char

        if(i == 0):
            it = 1
        elif i == num_rails - 1:
            it = -1

        i += it
    
    return ''.join(strings)

def decrypt_railfence(ciphertext, num_rails):
    strings = ["" for _ in range(num_rails)]

    n = len(ciphertext)
    number_in_part = 2 * (num_rails - 1)
    start = 0
    end = math.ceil(n / number_in_part)
    strings[0] = ciphertext[start:end]
    start = end
    for i in range(1, num_rails - 1):
        end = start + 2 * math.floor(n / number_in_part) + (i < (n % number_in_part)) + ((number_in_part - i) < n % number_in_part)
        strings[i] = ciphertext[start:end]

        start = end

    strings[num_rails - 1] = ciphertext[start:n]


    ind_szel = 0
    ind_kozep = -1
    i = 0
    it = 1
    
    solution = ""

    for _ in range(n):
        if  i == 0:
            solution += strings[i][ind_szel]
            it = 1
            ind_kozep += 1
        elif i == (num_rails - 1):
            solution += strings[i][ind_szel]
            ind_szel += 1
            it = -1
            ind_kozep += 1
        else:
            solution += strings[i][ind_kozep]

        i += it

    return solution


# Merkle-Hellman Knapsack Cryptosystem

def generate_private_key(n=8):
    """Generate a private key for use in the Merkle-Hellman Knapsack Cryptosystem.

    Following the instructions in the handout, construct the private key components
    of the MH Cryptosystem. This consistutes 3 tasks:

    1. Build a superincreasing sequence `w` of length n
        (Note: you can check if a sequence is superincreasing with `utils.is_superincreasing(seq)`)
    2. Choose some integer `q` greater than the sum of all elements in `w`
    3. Discover an integer `r` between 2 and q that is coprime to `q` (you can use utils.coprime)

    You'll need to use the random module for this function, which has been imported already

    Somehow, you'll have to return all of these values out of this function! Can we do that in Python?!

    @param n bitsize of message to send (default 8)
    @type n int

    @return 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.
    """
    raise NotImplementedError  # Your implementation here

def create_public_key(private_key):
    """Create a public key corresponding to the given private key.

    To accomplish this, you only need to build and return `beta` as described in the handout.

        beta = (b_1, b_2, ..., b_n) where b_i = r ?? w_i mod q

    Hint: this can be written in one line using a list comprehension

    @param private_key The private key
    @type private_key 3-tuple `(w, q, r)`, with `w` a n-tuple, and q and r ints.

    @return n-tuple public key
    """
    raise NotImplementedError  # Your implementation here


def encrypt_mh(message, public_key):
    """Encrypt an outgoing message using a public key.

    1. Separate the message into chunks the size of the public key (in our case, fixed at 8)
    2. For each byte, determine the 8 bits (the `a_i`s) using `utils.byte_to_bits`
    3. Encrypt the 8 message bits by computing
         c = sum of a_i * b_i for i = 1 to n
    4. Return a list of the encrypted ciphertexts for each chunk in the message

    Hint: think about using `zip` at some point

    @param message The message to be encrypted
    @type message bytes
    @param public_key The public key of the desired recipient
    @type public_key n-tuple of ints

    @return list of ints representing encrypted bytes
    """
    raise NotImplementedError  # Your implementation here

def decrypt_mh(message, private_key):
    """Decrypt an incoming message using a private key

    1. Extract w, q, and r from the private key
    2. Compute s, the modular inverse of r mod q, using the
        Extended Euclidean algorithm (implemented at `utils.modinv(r, q)`)
    3. For each byte-sized chunk, compute
         c' = cs (mod q)
    4. Solve the superincreasing subset sum using c' and w to recover the original byte
    5. Reconsitite the encrypted bytes to get the original message back

    @param message Encrypted message chunks
    @type message list of ints
    @param private_key The private key of the recipient
    @type private_key 3-tuple of w, q, and r

    @return bytearray or str of decrypted characters
    """
    raise NotImplementedError  # Your implementation here

