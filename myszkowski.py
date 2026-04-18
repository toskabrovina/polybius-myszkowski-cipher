# Myszkowski Transposition Cipher

from typing import List, Dict

def clean_text(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalnum())

def validate_keyword(keyword: str) -> str:
    clean_key = "".join(ch.upper() for ch in keyword if ch.isalpha())

    if len(clean_key) < 2:
        raise ValueError("Çelësi duhet me pas të paktën 2 shkronja.")

    return clean_key

def get_myszkowski_ranks(keyword: str):
    key = validate_keyword(keyword)

    unique_letters_sorted = sorted(set(key))
    rank_map = {}

    for index, letter in enumerate(unique_letters_sorted, start=1):
        rank_map[letter] = index

    return [rank_map[ch] for ch in key]

def pad_text(text: str, columns: int, pad_char: str = "X"):
    remainder = len(text) % columns

    if remainder != 0:
        text += pad_char * (columns - remainder)

    return text

def build_matrix(text: str, columns: int):
    matrix = []

    for i in range(0, len(text), columns):
        row = list(text[i:i + columns])
        matrix.append(row)

    return matrix

def matrix_to_string(matrix: List[List[str]], keyword: str, ranks: List[int]) -> str:
    lines = []
    lines.append("Çelësi : " + " ".join(keyword))
    lines.append("Rendit : " + " ".join(str(x) for x in ranks))

    for row in matrix:
        lines.append("        " + " ".join(row))

    return "\n".join(lines)


def encrypt_myszkowski(plaintext: str, keyword: str, pad_char: str = "X") -> Dict:
    key = validate_keyword(keyword)
    cleaned_plaintext = clean_text(plaintext)

    ranks = get_myszkowski_ranks(key)
    padded_plaintext = pad_text(cleaned_plaintext, len(key), pad_char)
    matrix = build_matrix(padded_plaintext, len(key))

    ciphertext_chars = []
    for rank in sorted(set(ranks)):
        columns_with_same_rank = [i for i, value in enumerate(ranks) if value == rank]

        if len(columns_with_same_rank) == 1:
            col = columns_with_same_rank[0]
            for row in matrix:
                ciphertext_chars.append(row[col])
        else:
            for row in matrix:
                for col in columns_with_same_rank:
                    ciphertext_chars.append(row[col])

    ciphertext = "".join(ciphertext_chars)

    return {
        "keyword": key,
        "ranks": ranks,
        "normalized_plaintext": padded_plaintext,
        "matrix": matrix,
        "ciphertext": ciphertext
    }



def decrypt_myszkowski(ciphertext: str, keyword: str, pad_char: str = "X", remove_padding: bool = False) -> Dict:
    key = validate_keyword(keyword)
    cleaned_ciphertext = clean_text(ciphertext)
    ranks = get_myszkowski_ranks(key)

    columns = len(key)

    if len(cleaned_ciphertext) % columns != 0:
        raise ValueError("Ciphertext-i nuk ka gjatësi të vlefshme për këtë çelës.")

    rows = len(cleaned_ciphertext) // columns
    matrix = [["" for _ in range(columns)] for _ in range(rows)]

    index = 0

    for rank in sorted(set(ranks)):
        columns_with_same_rank = [i for i, value in enumerate(ranks) if value == rank]

        if len(columns_with_same_rank) == 1:
            col = columns_with_same_rank[0]
            for row in range(rows):
                matrix[row][col] = cleaned_ciphertext[index]
                index += 1
        else:
            for row in range(rows):
                for col in columns_with_same_rank:
                    matrix[row][col] = cleaned_ciphertext[index]
                    index += 1

    plaintext_with_padding = "".join("".join(row) for row in matrix)

    if remove_padding:
        plaintext = plaintext_with_padding.rstrip(pad_char)
    else:
        plaintext = plaintext_with_padding

    return {
        "keyword": key,
        "ranks": ranks,
        "ciphertext": cleaned_ciphertext,
        "matrix": matrix,
        "plaintext_with_padding": plaintext_with_padding,
        "plaintext": plaintext
    }


def demo_function():
    plaintext = "HELLO WORLD"
    keyword = "LETTER"

    encrypted = encrypt_myszkowski(plaintext, keyword)
    decrypted = decrypt_myszkowski(encrypted["ciphertext"], keyword)

    print("\n========== DEMO ==========")
    print("Plaintext :", plaintext)
    print("Keyword   :", keyword)
    print("Encrypted :", encrypted["ciphertext"])
    print("Decrypted :", decrypted["plaintext"])


def main():
    while True:
        print("-------Myszkowski Transposition-------")
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Demo")
        print("0. Exit")

        choice = input("Zgjidh opsionin: ").strip()

        if choice == "1":
            plaintext = input("Shkruaj plaintext: ")
            keyword = input("Shkruaj keyword: ")
            result = encrypt_myszkowski(plaintext, keyword)
            print("Encrypted text:", result["ciphertext"])

        elif choice == "2":
            ciphertext = input("Shkruaj ciphertext: ")
            keyword = input("Shkruaj keyword: ")
            result = decrypt_myszkowski(ciphertext, keyword)
            print("Decrypted text:", result["plaintext"])

        elif choice == "3":
            demo_function()

        elif choice == "0":
            print("Programi u mbyll.")
            break

        else:
            print("Opsion i pavlefshem. Provo perseri.")


if __name__ == "__main__":
    main()