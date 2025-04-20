def encrypt(plaintext, key):
    ciphertext = ''
    key = key.lower()  # Make sure key is in lowercase
    key_index = 0
    
    for char in plaintext:
        if char.isalpha():  # Only process alphabetic characters
            shift = ord(key[key_index % len(key)]) - ord('a')  # Get the shift from the key
            if char.islower():
                ciphertext += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
            elif char.isupper():
                ciphertext += chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
            key_index += 1  # Move to the next character in the key
        else:
            ciphertext += char  # Non-alphabetic characters remain unchanged
    
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ''
    key = key.lower()  # Make sure key is in lowercase
    key_index = 0
    
    for char in ciphertext:
        if char.isalpha():  # Only process alphabetic characters
            shift = ord(key[key_index % len(key)]) - ord('a')  # Get the shift from the key
            if char.islower():
                plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            elif char.isupper():
                plaintext += chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            key_index += 1  # Move to the next character in the key
        else:
            plaintext += char  # Non-alphabetic characters remain unchanged
    
    return plaintext

if __name__ == '__main__':
    message = "MEET"
    key = "BDUF"

    encrypted_message = encrypt(message, key)
    print(f"Encrypted message: {encrypted_message}")

    decrypted_message = decrypt(encrypted_message, key)
    print(f"Decrypted message: {decrypted_message}")

'''
Encrypted message: NHYY
Decrypted message: MEET
'''

'''
I think you meant the Vernam cipher, also known as the one-time pad! It's one of the most secure encryption methods ever devised.
How It Works
- Each letter in the plaintext is converted to a numerical value (A = 0, B = 1, ..., Z = 25).
- A random key (equal in length to the plaintext) is generated.
- Each letter in the plaintext is encrypted using the formula:[ E(x) = (x \oplus k) \mod 26 ]where:- ( x ) is the plaintext letter's numerical value.
- ( k ) is the key letter's numerical value.
- ( \oplus ) represents the XOR operation.

- Decryption is done using the same XOR operation with the key.

Advantages
- Perfect secrecy - If the key is truly random and used only once, the cipher is unbreakable.
- No patterns - Since the key is random, frequency analysis is useless.

Disadvantages
- Key management - The key must be as long as the message and must be securely shared.
- One-time use - If the same key is reused, the encryption can be broken.
'''