# Multiplicative Cipher

#Encryption
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            encrypted_char = chr(((ord(char) - shift) * key % 26) + shift)
            ciphertext += encrypted_char
        else:
            ciphertext += char
    return ciphertext.upper()  

#Decryption
def decrypt(ciphertext, key):
    plaintext = ""
    
    inverse_key = 0
    for i in range(1, 26):
        if (key * i) % 26 == 1:
            inverse_key = i
            break
    for char in ciphertext:
        if char.isalpha():
            shift = ord('A') if char.isupper() else ord('a')
            decrypted_char = chr(((ord(char) - shift) * inverse_key % 26) + shift)
            plaintext += decrypted_char
        else:
            plaintext += char
    return plaintext.lower()  # Convert to all lowercase

#Main Function
while True:
    print("Choose an option:")
    print("1. Encryption")
    print("2. Decryption")
    print("3. Exit")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        plaintext = input("Enter the plaintext: ")
        key = int(input("Enter the key: "))
        ciphertext = encrypt(plaintext, key)
        print("The Cipher text is:")
        print(ciphertext)

    elif choice == '2':
        ciphertext = input("Enter the ciphertext: ")
        key = int(input("Enter the key: "))
        plaintext = decrypt(ciphertext, key)
        print("The plaintext is:")
        print(plaintext)

    elif choice == '3':
        print("Exiting the program.")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
