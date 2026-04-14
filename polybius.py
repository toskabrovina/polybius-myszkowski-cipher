# Polybius Cipher Encryption






























# Polybius Cipher Decryption

def polybius_decrypt(ciphertext: str) -> str:
    _, reverse_square = create_polybius_square()

    result = []
    parts = ciphertext.split()

    for part in parts:
        if part == "/":
            result.append(" ")
        elif part in reverse_square:
            result.append(reverse_square[part])

    return "".join(result)


# 🔹 Example usage
text = "HELLO WORLD"

encrypted = polybius_encrypt(text)
decrypted = polybius_decrypt(encrypted)

print("Original:", text)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)