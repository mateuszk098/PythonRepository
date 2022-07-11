'''
    Generate an RSA keypair with an exponent of 65537 in PEM format
    param: bits The key length in bits
    Return private key and public key
    
    IMPORTANT! INSTALL PyCryptodome
    
    ---->  pip3 install -U PyCryptodome  <----
    
    Bits length of the RSA key is the first argument e.g. 
    
    ---->  python3 rsa.py 1024  <----
'''

import sys
from Crypto.PublicKey import RSA


def generate_RSA(bits_length):

    new_key = RSA.generate(bits_length, e=65537)
    public_key = new_key.publickey().exportKey("PEM")
    private_key = new_key.exportKey("PEM")
    return private_key, public_key


bits_length = int(sys.argv[1])
RSA_KEY = open("RSA_KEY.txt", "w")
RSA_KEY.write(str(generate_RSA(bits_length)))
RSA_KEY.close()