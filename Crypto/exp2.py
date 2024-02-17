# Program for RSA cryptosystem

import math

class RSA:
    def __init__(self, p, q):
        self.p = p
        self.q = q
    
    def generateKey(self):
        self.n = self.p * self.q
        self.phi = (self.p - 1) * (self.q - 1)
        self.e = 2 
        while self.e < self.phi: 
            if math.gcd(self.e, self.phi) == 1: 
                break 
            else: 
                self.e += 1 
        self.k = 2
        self.d = (1 + (self.k * self.phi)) // self.e 
        print(f'Public key: ({self.e}, {self.n})') 
        print(f'Private key: ({self.d}, {self.n})') 

    def encrypt(self, msg):
        self.msg = msg
        self.enc = math.fmod(pow(self.msg, self.e), self.n) 
        print(f'Encrypted message: {self.enc}') 
        return self.enc

    def decrypt(self, enc_msg):
        self.enc = enc_msg
        self.dec = math.fmod(pow(self.enc, self.d), self.n) 
        print(f'Decrypted message: {self.dec}') 

# Example usage:
rsa = RSA(3, 7)
rsa.generateKey()
enc = rsa.encrypt(11)
rsa.decrypt(enc)
