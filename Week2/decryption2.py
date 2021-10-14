ciphertext = input("Input some ciphertext: ")
plainText = ""
ciphertextPosition = 0
while ciphertextPosition<len(ciphertext): #as plaintextPosition starts from 0, so we process each character in the plaintext until we have reached the end of the plaintext
    ciphertextChar = ciphertext[ciphertextPosition]
    ASCIIvalue = ord(ciphertextChar)
    ASCIIvalue = ASCIIvalue +3
    plainText = plainText + chr(ASCIIvalue)
    ciphertextPosition = ciphertextPosition + 1
print(plainText)
