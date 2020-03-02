# Vigenere Cipher 
# based on source @ https://www.geeksforgeeks.org/vigenere-cipher/
  
# This function decrypts the encrypted text and returns the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text)) 

if __name__ == "__main__": 
    cipher = "UEUTCEVRRZXLJXKVFHJX"
    key = "REDREDREDREDREDREDRE"
    print("Original/Decrypted Text:" + originalText(cipher, key))

    #brute force attack:
    #possibleKeys = ["BLUEBLUEBLUEBLUEBLUE","GREENGREENGREENGREEN","REDREDREDREDREDREDRE"]
    #for x in range(len(possibleKeys)):
    #    key = possibleKeys[x]
    #    cipher = "UEUTCEVRRZXLJXKVFHJX"
    #    print("Possible Original/Decrypted Text:" + originalText(cipher, key))