def generate_vigenere_square():
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    vigenere_square = {}
    for i, char in enumerate(alphabet):
        vigenere_square[char] = alphabet[i:] + alphabet[:i]
    return vigenere_square

def vigenere_encrypt(plaintext, key):
    plaintext = plaintext.upper()
    key = key.upper()
    vigenere_square = generate_vigenere_square()
    encrypted_text = ''
    key_index = 0

    for char in plaintext:
        if char.isalpha():
            encrypted_text += vigenere_square[char][ord(key[key_index]) - 65]
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += char

    return encrypted_text

def vigenere_decrypt(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    vigenere_square = generate_vigenere_square()
    decrypted_text = ''
    key_index = 0

    for char in ciphertext:
        if char.isalpha():
            decrypted_text += chr((vigenere_square[key[key_index]].index(char)) + 65)
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += char

    return decrypted_text

def main():
    choice = input("Enter 'E' to Encrypt or 'D' to Decrypt: ").upper()

    if choice == 'E':
        message = input("Enter the message to encrypt: ")
        key = input("Enter the key: ")

        encrypted_message = vigenere_encrypt(message, key)
        print("Encrypted message:", encrypted_message)

    elif choice == 'D':
        encrypted_message = input("Enter the message to decrypt: ")
        key = input("Enter the key: ")

        decrypted_message = vigenere_decrypt(encrypted_message, key)
        print("Decrypted message:", decrypted_message)

    else:
        print("Invalid choice. Please enter 'E' to Encrypt or 'D' to Decrypt.")

if __name__ == "__main__":
    main()
