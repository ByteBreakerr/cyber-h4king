#!/bin/python3

import hashlib
from cryptography.hazmat.primitives.asymmetric import rsa
import base64
from cryptography.hazmat.primitives import serialization

def generate_onion_address():
   pem = rsa.generate_private_key(
           key_size=4096,
           public_exponent=65537,
           )
   public_key = pem.public_key()
   public_pem = public_key.public_bytes(
           encoding=serialization.Encoding.PEM,
           format=serialization.PublicFormat.SubjectPublicKeyInfo
           )
   SHA1_hash = hashlib.sha1(public_pem).digest()
   base32_enc = base64.b32encode(SHA1_hash).decode().lower()

   ONION_ADDRESS = base32_enc + ".onion"
   return ONION_ADDRESS

def main():
    if __name__ == '__main__':
        for num in range(int(input("Enter the number of addresses to generate: "))):
            print()
            GENERATED_ADDR = generate_onion_address()
            print(GENERATED_ADDR)
main()

