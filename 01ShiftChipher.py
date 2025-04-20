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
