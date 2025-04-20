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

'''
he Vigenère cipher is a polyalphabetic substitution cipher that encrypts text using a series of Caesar ciphers based on the letters of a keyword. Unlike the simple shift cipher, it uses multiple shifts, making it much harder to break.
How It Works
- Choose a keyword (e.g., "KEY").
- Repeat the keyword to match the length of the plaintext.
- Each letter in the plaintext is shifted based on the corresponding letter in the keyword.
- The encryption formula is:[ E(x) = (x + k) \mod 26 ]where:- ( x ) is the plaintext letter’s position in the alphabet.
- ( k ) is the keyword letter’s position.
- ( \mod 26 ) ensures wrap-around.


Example
If the plaintext is HELLO and the keyword is KEY, the encryption works as follows:
| Plaintext | H | E | L | L | O | 
| Keyword | K | E | Y | K | E | 
| Shifted | R | I | J | V | S | 


So, HELLO becomes RIJVS.
Advantages
- Stronger than simple substitution ciphers.
- Harder to break using frequency analysis.

Disadvantages
- Vulnerable to Kasiski examination (a method to find the keyword length).
- If the keyword is short, it behaves like a simple shift cipher.
'''