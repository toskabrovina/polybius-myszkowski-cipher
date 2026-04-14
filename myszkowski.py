# Myszkowski Transposition Cipher

from typing import List, Dict

def clean_text(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalnum())

def validate_keyword(keyword: str) -> str:
    clean_key = "".join(ch.upper() for ch in keyword if ch.isalpha())

    if len(clean_key) < 2:
        raise ValueError("Çelësi duhet me pas të paktën 2 shkronja.")

    return clean_key


def get_keyword_order(keyword: str) -> List[int]:
    unique_letters = sorted(set(keyword))
    letter_to_number: Dict[str, int] = {}

    for i, letter in enumerate(unique_letters):
        letter_to_number[letter] = i + 1

    order = []
    for letter in keyword:
        order.append(letter_to_number[letter])

    return order


def create_matrix_for_encryption(text: str, columns: int) -> List[List[str]]:
    rows = len(text) // columns
    if len(text) % columns != 0:
        rows += 1

    while len(text) < rows * columns:
        text += "X"

    matrix = []
    index = 0

    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append(text[index])
            index += 1
        matrix.append(row)

    return matrix


def encrypt_myszkowski(plaintext: str, keyword: str) -> str:
    plaintext = clean_text(plaintext)
    keyword = validate_keyword(keyword)

    order = get_keyword_order(keyword)
    matrix = create_matrix_for_encryption(plaintext, len(keyword))

    ciphertext = ""
    used_numbers = sorted(set(order))

    for number in used_numbers:
        same_columns = []

        for i in range(len(order)):
            if order[i] == number:
                same_columns.append(i)

        if len(same_columns) == 1:
            col = same_columns[0]
            for row in matrix:
                ciphertext += row[col]
        else:
            for row in matrix:
                for col in same_columns:
                    ciphertext += row[col]

    return ciphertext


def decrypt_myszkowski(ciphertext: str, keyword: str) -> str:
    ciphertext = clean_text(ciphertext)
    keyword = validate_keyword(keyword)

    order = get_keyword_order(keyword)
    columns = len(keyword)
    rows = len(ciphertext) // columns

    if len(ciphertext) % columns != 0:
        rows += 1

    matrix = []
    for _ in range(rows):
        row = []
        for _ in range(columns):
            row.append("")
        matrix.append(row)

    index = 0
    used_numbers = sorted(set(order))

    for number in used_numbers:
        same_columns = []

        for i in range(len(order)):
            if order[i] == number:
                same_columns.append(i)

        if len(same_columns) == 1:
            col = same_columns[0]
            for row in range(rows):
                if index < len(ciphertext):
                    matrix[row][col] = ciphertext[index]
                    index += 1
        else:
            for row in range(rows):
                for col in same_columns:
                    if index < len(ciphertext):
                        matrix[row][col] = ciphertext[index]
                        index += 1

    plaintext = ""
    for row in matrix:
        for char in row:
            plaintext += char

    return plaintext.rstrip("X")


def main():
    print("Myszkowski Transposition Cipher")

    keyword = input("Shkruaj celesin: ")
    message = input("Shkruaj mesazhin: ")

    encrypted = encrypt_myszkowski(message, keyword)
    print("Mesazhi i enkriptuar:", encrypted)

    decrypted = decrypt_myszkowski(encrypted, keyword)
    print("Mesazhi i dekriptuar:", decrypted)


if __name__ == "__main__":
    main()