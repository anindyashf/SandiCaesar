def caesar(plaintext, shift, alphabet):
    
    dictionary= {}

    for i in range(0, len(alphabet)):
        dictionary[alphabet[i]] = alphabet[(i+shift) % len(alphabet)]
    
    ciphertext= ""
    for j in plaintext:
        if j in dictionary:
            j = dictionary[j]
        ciphertext+=j
    return ciphertext
    
def decipher_caesar(plaintext, shift, alphabet):
    
    dictionary= {}
       for i in range(0, len(alphabet)):
        dictionary[alphabet[(i+shift) % len(alphabet)]] = alphabet[i % len(alphabet)]
    ciphertext= ""
    for j in plaintext:
        if j in dictionary:
            j = dictionary[j]
        ciphertext+=j
    return ciphertext

alphabet = [" ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l",
    "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
    "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    
plaintext= "I eat sandwich"
shiftTimes = 3
cipher = caesar(plaintext, shiftTimes, alphabet)
print("Ciphered caesar encrypted text:", cipher)
decipher = decipher_caesar(cipher, shiftTimes, alphabet)
print("Deciphered caesar encrypted text:", decipher)
