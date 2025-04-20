# Playfair cipher decryption with padding removal
def create_playfair_table(key):
    key = ''.join(sorted(set(key), key=key.index))  # Remove duplicates while maintaining order
    table = []
    alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"  # 'J' is omitted in Playfair cipher

    for char in key:
        if char not in table and char in alphabet:
            table.append(char)

    for char in alphabet:
        if char not in table:
            table.append(char)
    
    return [table[i:i+5] for i in range(0, len(table), 5)]

def get_position(c, table):
    for i in range(5):
        for j in range(5):
            if table[i][j] == c:
                return i, j

def decrypt_playfair(ciphertext, key):
    table = create_playfair_table(key.upper())
    ciphertext = ciphertext.upper().replace(" ", "")  # Remove spaces and make uppercase
    decrypted_text = []

    i = 0
    while i < len(ciphertext):
        char1, char2 = ciphertext[i], ciphertext[i + 1]
        i += 2
        
        row1, col1 = get_position(char1, table)
        row2, col2 = get_position(char2, table)

        if row1 == row2:
            # Same row: move to the left
            decrypted_text.append(table[row1][(col1 - 1) % 5])
            decrypted_text.append(table[row2][(col2 - 1) % 5])
        elif col1 == col2:
            # Same column: move up
            decrypted_text.append(table[(row1 - 1) % 5][col1])
            decrypted_text.append(table[(row2 - 1) % 5][col2])
        else:
            # Rectangle: swap the corners
            decrypted_text.append(table[row1][col2])
            decrypted_text.append(table[row2][col1])

    # Remove padding 'X' (if it's used in the original message)
    decrypted_message = ''.join(decrypted_text).replace('X', '')
    
    return decrypted_message

# Get inputs from the user
ciphertext = input("Enter the ciphertext: ")
key = input("Enter the key: ")

# Decrypt the ciphertext
decrypted_message = decrypt_playfair(ciphertext, key)
print(f"Decrypted message: {decrypted_message}")

'''
Enter the ciphertext: OMRMPCSGPTER
Enter the key: COMPUTER
Decrypted message: COMMUNICATE
'''

'''
The Playfair cipher is a digraph substitution cipher, meaning it encrypts pairs of letters instead of single letters. It was invented by Charles Wheatstone in 1854 but is named after Lord Playfair, who promoted its use.
How It Works
- A 5×5 grid is created using a keyword, filling in the remaining letters of the alphabet (I and J are treated as the same).
- The plaintext is split into pairs of letters (digraphs).
- Each pair is encrypted based on their positions in the grid:- If both letters are in the same row, replace them with the letters to their right.
- If both letters are in the same column, replace them with the letters below.
- If the letters form a rectangle, swap them with the letters in the opposite corners.


Advantages
- More secure than simple substitution ciphers.
- Harder to break using frequency analysis since it works on digraphs instead of single letters.

Disadvantages
- Still vulnerable to cryptanalysis with enough ciphertext.
- Requires memorizing or reconstructing the 5×5 grid for encryption and decryption.
'''