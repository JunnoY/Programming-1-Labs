plaintext = input("Input some plaintext: ")
cipherText = ""
plaintextPosition = 0
while plaintextPosition<len(plaintext): #as plaintextPosition starts from 0, so we process each character in the plaintext until we have reached the end of the plaintext
    plaintextChar = plaintext[plaintextPosition]
    ASCIIvalue = ord(plaintextChar)
    ASCIIvalue = ASCIIvalue -3
    cipherText = cipherText + chr(ASCIIvalue)
    plaintextPosition = plaintextPosition + 1
print(cipherText)
