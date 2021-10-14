plaintext = input("Input some plaintext: ")
cipherText = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
plaintextPosition = 0
while plaintextPosition<len(plaintext): #as plaintextPosition starts from 0, so we process each character in the plaintext until we have reached the end of the plaintext
    plaintextChar = plaintext[plaintextPosition]
    alphabetPosition = 3
    while plaintextChar!= alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1
    alphabetPosition = alphabetPosition -3
    cipherText = cipherText + alphabet[alphabetPosition]
    plaintextPosition = plaintextPosition + 1

print(cipherText)
