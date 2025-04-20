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