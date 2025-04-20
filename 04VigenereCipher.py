def vigenere_decrypt(ciphertext, key):
    decrypted_text = []
    key_index = 0
    key = key.lower()  # Ensure the key is in lowercase

    for char in ciphertext:
        if char.isalpha():
            # Calculate the shift based on the key character
            shift = ord(key[key_index % len(key)]) - ord('a')
            
            if char.isupper():
                # Decrypt for uppercase letters
                decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
            else:
                # Decrypt for lowercase letters
                decrypted_char = chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
            
            decrypted_text.append(decrypted_char)
            key_index += 1
        else:
            # If the character is not a letter, just add it as is (e.g. spaces or punctuation)
            decrypted_text.append(char)

    return ''.join(decrypted_text)

# Example usage
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

decrypted_message = vigenere_decrypt(ciphertext, key)
print("Decrypted message:", decrypted_message)


'''
Enter the ciphertext: ZICVTWQNGRZGVTWAVZHCQYGLMGJ
Enter the key: DECEPTIVE
Decrypted message: WEAREDISCOVEREDSAVEYOURSELF
'''