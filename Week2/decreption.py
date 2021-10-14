ciphertext = input("Input some ciphertext: ")
plainText = ""
alphabet = "XYZABCDEFGHIJKLMNOPQRSTUVWXYZABC"
ciphertextPosition = 0
while ciphertextPosition<len(ciphertext): #as plaintextPosition starts from 0, so we process each character in the plaintext until we have reached the end of the plaintext
    ciphertextChar = ciphertext[ciphertextPosition]
    alphabetPosition = 3
    while ciphertextChar!= alphabet[alphabetPosition]:
        alphabetPosition = alphabetPosition + 1
    alphabetPosition = alphabetPosition +3
    plainText = plainText + alphabet[alphabetPosition]
    ciphertextPosition = ciphertextPosition + 1

print(plainText)
