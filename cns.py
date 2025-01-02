def remove_duplicates(key):
    result = []
    for char in key:
        if char not in result and char != ' ':
            result.append(char)
    return ''.join(result)

# Function to display matrices for visual understanding
def display_matrix(message, key):
    matrix = [list(message[i:i+len(key)]) for i in range(0, len(message), len(key))]
    for row in matrix:
        print(" ".join(row))
    print("\n")

# Function to perform transposition encryption
def transpose(message, key):
    while len(message) % len(key) != 0:
        message += "X"
    matrix = [list(message[i:i+len(key)]) for i in range(0, len(message), len(key))]
    key_order = sorted([(char, i) for i, char in enumerate(key)], key=lambda x: x[0])
    transposed = []
    for _, col_idx in key_order:
        for row in matrix:
            transposed.append(row[col_idx])
    return "".join(transposed)

# Function to perform transposition decryption
def reverse_transpose(message, key):
    num_rows = len(message) // len(key)
    matrix = [[''] * len(key) for _ in range(num_rows)]
    key_order = sorted([(char, i) for i, char in enumerate(key)], key=lambda x: x[0])
    idx = 0
    for _, col_idx in key_order:
        for row_idx in range(num_rows):
            matrix[row_idx][col_idx] = message[idx]
            idx += 1
    return "".join("".join(row) for row in matrix)

# Encryption function
def encrypt_message(message, key1, key2):
    print("\n--- ENCRYPTION ---")
    print("Original Message: ", message)
    print("Key 1 for first encryption: ", key1)
    print("Matrix for first encryption: ")
    display_matrix(message, key1)
    encrypted_once = transpose(message, key1)
    print("Message after first encryption: ", encrypted_once)

    print("\nKey 2 for second encryption: ", key2)
    print("Matrix for second encryption: ")
    display_matrix(encrypted_once, key2)
    encrypted_message = transpose(encrypted_once, key2)
    print("Message after second encryption: ", encrypted_message)
    return encrypted_message

# Decryption function
def decrypt_message(encrypted_message, key1, key2):
    print("\n--- DECRYPTION ---")
    print("Encrypted Message: ", encrypted_message)
    decrypted_once = reverse_transpose(encrypted_message, key2)
    print("Message after reversing second encryption: ", decrypted_once)

    decrypted_message = reverse_transpose(decrypted_once, key1)
    print("Message after reversing first encryption: ", decrypted_message)
    return decrypted_message

# Main menu loop
def double_transposition_cipher():
    while True:
        print("\n--- Double Transposition Cipher ---")
        print("1. Encrypt a Message")
        print("2. Decrypt a Message")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':  # Encryption
            message = input("Enter the message to be encrypted: ").upper().replace(" ", "").replace(".", "")
            key1 = remove_duplicates(input("Enter the first key: ").upper())
            key2 = remove_duplicates(input("Enter the second key: ").upper())
            encrypted_message = encrypt_message(message, key1, key2)

        elif choice == '2':  # Decryption
            encrypted_message = input("Enter the encrypted message to be decrypted: ").upper()
            key1 = remove_duplicates(input("Enter the first key: ").upper())
            key2 = remove_duplicates(input("Enter the second key: ").upper())
            decrypted_message = decrypt_message(encrypted_message, key1, key2)

        elif choice == '3':  # Exit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")

if __name__ == "__main__":
    double_transposition_cipher()
