def shift_cipher(text, shift, option):
    result = ""
    if option.lower() == "encrypt":
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    result += chr((ord(char) - ord('a') + shift_amount) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') + shift_amount) % 26 + ord('A'))
            else:
                result += char
    elif option.lower() == "decrypt":
        for char in text:
            if char.isalpha():
                shift_amount = shift % 26
                if char.islower():
                    result += chr((ord(char) - ord('a') - shift_amount) % 26 + ord('a'))
                else:
                    result += chr((ord(char) - ord('A') - shift_amount) % 26 + ord('A'))
            else:
                result += char
    else:
        return "Invalid option. Please choose 'encrypt' or 'decrypt'."
    return result

text = input("Enter the text: ")
shift = int(input("Enter the shift value: "))
option = input("Choose 'encrypt' or 'decrypt': ")

print("Result:", shift_cipher(text, shift, option))


'''
This part to be done on https://cse29-iiith.vlabs.ac.in/

PART 1
Ciphertext to be decrypted:
haahjr ha khdu

PART 3
Plaintext:
attack at dawn
Ciphertext
haahjr ha khdu

PART 4
Enter your solution Plaintext and shift key here:
attack at dawn
'''

'''
Theory:

The Caesar cipher is a substitution cipher where each letter in the plaintext is shifted a certain number of places down or up the alphabet. For example, with a shift of 1, A would be replaced by B, B would become C, and so on. The method is named after Julius Caesar, who used it to communicate with his generals.
The Caesar cipher is a simple and effective way to encrypt messages, but it is also easy to break with modern computing power. It is not recommended for use in secure communications today. However, it is a great introduction to the concepts of encryption and decryption.

The shift cipher, also known as the Caesar cipher, is one of the simplest encryption techniques. It works by shifting each letter in the plaintext a fixed number of places down or up the alphabet. For example, with a shift of 3, the letter A becomes D, B becomes E, and so on.
Mathematically, encryption in a shift cipher can be represented as:
[ E(x) = (x + n) \mod 26 ]
where:
- ( x ) is the position of the plaintext letter in the alphabet (starting from 0 for A),
- ( n ) is the shift value (key),
- ( \mod 26 ) ensures the shift wraps around the alphabet.

Decryption follows a similar formula:
[ D(y) = (y - n) \mod 26 ]
where ( y ) is the position of the ciphertext letter.
While historically used by Julius Caesar for military communication, the shift cipher is not secure today because it can be easily broken using frequency analysis or brute force (since there are only 25 possible shifts).

The shift cipher (or Caesar cipher) has its own set of advantages and disadvantages, making it a fundamental but outdated encryption method.
Advantages
- Simplicity - It is easy to understand and implement, making it a great introduction to cryptography.
- Low computational cost - Requires minimal computing resources, making it efficient for basic encryption.
- Historical significance - Used by Julius Caesar for secure communication, making it an important part of cryptographic history.
- Basic security - Provides a simple way to obscure text from casual observers who are unfamiliar with encryption.

Disadvantages
- Easily breakable - Since there are only 25 possible shifts, it can be brute-forced quickly.
- Vulnerable to frequency analysis - Since letter frequencies remain unchanged, an attacker can analyze the most common letters and deduce the shift.
- Not suitable for modern security - It lacks complexity and is ineffective against even basic cryptographic attacks.

How It Can Be Analyzed
- Brute Force Attack - Since there are only 25 possible shifts, an attacker can try all shifts to decrypt the message.
- Frequency Analysis - By analyzing letter frequencies, an attacker can determine the shift value and decrypt the text.
- Known Plaintext Attack - If an attacker knows part of the plaintext, they can deduce the shift and decrypt the rest.

'''