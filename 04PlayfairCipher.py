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