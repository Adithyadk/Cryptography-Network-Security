import random

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def mod_inverse(a, m):
    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        m, a = a % m, m
        x0, x1 = x1 - q * x0, x0
    return x1 + m0 if x1 < 0 else x1

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError("Both numbers must be prime.")
    elif p == q:
        raise ValueError("p and q cannot be equal.")

    n = p * q
    phi = (p - 1) * (q - 1)

    # Choose e such that 1 < e < phi and e is coprime with phi
    e = random.randrange(2, phi)
    while gcd(e, phi) != 1:
        e = random.randrange(2, phi)

    # Compute d, the modular multiplicative inverse of e (mod phi)
    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

def encrypt(message, public_key):
    e, n = public_key
    cipher = pow(message, e, n)
    return cipher

def decrypt(ciphertext, private_key):
    d, n = private_key
    plain = pow(ciphertext, d, n)
    return plain

def main():
    print("RSA Encryption and Decryption Program")

    while True:
        print("\nMenu:")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            # Step 1: Input prime numbers p and q
            p = int(input("Enter a large prime number (p): "))
            q = int(input("Enter another large prime number (q): "))

            # Generate public and private keys
            public_key, private_key = generate_keypair(p, q)
            print(f"\nPublic Key (e, n): {public_key}")
            print(f"Private Key (d, n): {private_key}")

            # Step 3: Input plaintext
            plaintext = int(input("\nEnter the plaintext to encrypt: "))

            # Step 4: Encrypt plaintext message using public key <e, n>
            ciphertext = encrypt(plaintext, public_key)
            print(f"\nEncrypted Ciphertext: {ciphertext}")

        elif choice == '2':
            # Step 5: Decrypt ciphertext message using private key <d, n>
            ciphertext = int(input("Enter the ciphertext to decrypt: "))
            decrypted_text = decrypt(ciphertext, private_key)
            print(f"\nDecrypted Plaintext: {decrypted_text}")

        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
