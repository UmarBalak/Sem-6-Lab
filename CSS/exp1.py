# Python program to demonstrate Substitution Cipher 

import string 
# A list containing all characters 
all_letters= string.ascii_letters
print(f"All letters: '{all_letters}'\n")

class SubstitutionCipher:
    def encrypt(self, plainText, key = 4):
        self.dict = {}
        for i in range(len(all_letters)): 
            self.dict[all_letters[i]] = all_letters[(i+key) % len(all_letters)] 
        cipher_txt_list = [] 
        for char in plainText: 
            if char in all_letters: 
                temp = self.dict[char] 
                cipher_txt_list.append(temp) 
            else: 
                temp = char 
                cipher_txt_list.append(temp)
        cipherText = "".join(cipher_txt_list) 
        return cipherText, key

    def decrypt(self, cipherText, key = 4):
        self.dict = {}
        for i in range(len(all_letters)): 
            self.dict[all_letters[i]] = all_letters[(i-key) % len(all_letters)] 
        plain_txt_list = [] 
        for char in cipherText: 
            if char in all_letters: 
                temp = self.dict[char] 
                plain_txt_list.append(temp) 
            else: 
                temp = char 
                plain_txt_list.append(temp)
        plainText = "".join(plain_txt_list) 
        return plainText, key
    

plainText = "Cryptography And System Security"
print(f"Original Text is: '{plainText}'\n")

subCipher = SubstitutionCipher()
cipherText, key = subCipher.encrypt(plainText)
print(f"Cipher/Encrypted Text is: '{cipherText}'\nKey for encryption is: '{key}'\n")

plainText, key = subCipher.decrypt(cipherText)
print(f"Plain/Decrypted Text is: '{plainText}'\nKey for decryption is: '{key}'")

