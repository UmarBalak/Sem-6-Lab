# Python program to demonstrate Substitution Cipher 

import string 
# A list containing all characters 
letters= string.ascii_letters
print(f"All letters: '{letters}'\n")

class SubstitutionCipher:
    def encrypt(self, pTxt, key = 4):
        self.dict = {}
        for i in range(len(letters)): 
            self.dict[letters[i]] = letters[(i+key) % len(letters)] 
        cipher_txt_list = [] 
        for char in pTxt: 
            if char in letters: 
                temp = self.dict[char] 
                cipher_txt_list.append(temp) 
            else: 
                temp = char 
                cipher_txt_list.append(temp)
        cTxt = "".join(cipher_txt_list) 
        return cTxt, key

    def decrypt(self, cTxt, key = 4):
        self.dict = {}
        for i in range(len(letters)): 
            self.dict[letters[i]] = letters[(i-key) % len(letters)] 
        pTxtList = [] 
        for char in cTxt: 
            if char in letters: 
                temp = self.dict[char] 
                pTxtList.append(temp) 
            else: 
                temp = char 
                pTxtList.append(temp)
        pTxt = "".join(pTxtList) 
        return pTxt, key
    

pTxt = "Cryptography And System Security"
print(f"Original Text is: '{pTxt}'\n")

subCipher = SubstitutionCipher()
cTxt, key = subCipher.encrypt(pTxt)
print(f"Cipher/Encrypted Text is: '{cTxt}'\nKey for encryption is: '{key}'\n")

pTxt, key = subCipher.decrypt(cTxt)
print(f"Plain/Decrypted Text is: '{pTxt}'\nKey for decryption is: '{key}'")

