"""
Implementimi i Polybius Square cipher ne Python.

Cdo shkronje e plaintext'i do te zevendesohet me koordinatat e saj ne nje matrice 5x5.
Shkronja "J" do te trajtohet si "I" per te pershtatur alfabetin ne 25 shkronja.(Rregull standarde per Polybius Square).
"""


class PolybiusSquare:

    def __init__(self, keyword: str = ""):
        self.square, self.reverse = self._build_square(keyword)

    # ------------------------------------------------------------------
    def _build_square(self, keyword: str):
        """
        Ndertimi i matrices 5x5.
        Nese jepet keyword, shkronjat e tij do te jene te para ne matrice, 
        ndjekur nga shkronjat e mbetura te alfabetit.
        """
        keyword = keyword.upper().replace("J", "I")
        seen = []
        for ch in keyword:
            if ch.isalpha() and ch not in seen:
                seen.append(ch)
        for ch in "ABCDEFGHIKLMNOPQRSTUVWXYZ":
            if ch not in seen:
                seen.append(ch)

        square = {}
        reverse = {}
        for idx, ch in enumerate(seen):
            row, col = divmod(idx, 5)
            square[ch] = (row + 1, col + 1)
            reverse[(row + 1, col + 1)] = ch
        return square, reverse

    # ------------------------------------------------------------------
    def encrypt(self, plaintext: str) -> str:
        """Kthe tekstin e shifruar si cifte koordinatash te ndara me hapesire."""
        plaintext = plaintext.upper().replace("J", "I")
        result = []
        for ch in plaintext:
            if ch.isalpha():
                r, c = self.square[ch]
                result.append(f"{r}{c}")
            else:
                result.append(ch)
        return " ".join(result)

    def decrypt(self, ciphertext: str) -> str:
        tokens = ciphertext.split()
        result = []
        for token in tokens:
            if token.isdigit() and len(token) == 2:
                r, c = int(token[0]), int(token[1])
                result.append(self.reverse.get((r, c), "?"))
            else:
                result.append(token)
        return "".join(result)

    # ------------------------------------------------------------------
    def display_square(self):
        print("\n  Polybius Square:")
        print("    1  2  3  4  5")
        for row in range(1, 6):
            letters = [self.reverse[(row, col)] for col in range(1, 6)]
            print(f"  {row} {'  '.join(letters)}")
        print()


def separator(title: str = ""):
    line = "─" * 50
    print(f"\n{line}")
    if title:
        print(f"  {title}")
        print(line)


def demo_polybius():

    keyword = input("  Keyword (Press \"<ENTER>\" for basic Latin alphabet): ").strip()
    ps = PolybiusSquare(keyword)
    ps.display_square()
       
    plaintext = input("  Plaintext: ").strip()
    encrypted = ps.encrypt(plaintext)
    decrypted = ps.decrypt(encrypted)

    print(f"\n  Original Text : {plaintext.upper()}")
    print(f"  Encrypted Text: {encrypted}")
    print(f"  Decrypted Text: {decrypted}")

def main():
    print("=" * 50)
    print(" Polybius Square Cipher")
    print("=" * 50)
    print("\n  1. Polybius Square Cipher")
    print("  2. Demo automatik")
    print("  0. Dil")

    choice = input("\n  Zgjidhni opsionin: ").strip()
    
    if choice == "1":
    demo_polybius()
    elif choice == "2":
        # Demo automatik
        separator("DEMO AUTOMATIK — POLYBIUS SQUARE")
        ps = PolybiusSquare("KEYWORD")
        ps.display_square()
        sample = "HELLO WORLD"
        enc = ps.encrypt(sample)
        dec = ps.decrypt(enc)
        print(f"  Plaintext : {sample}")
        print(f"  Encrypted : {enc}")
        print(f"  Decrypted : {dec}")
    elif choice == "0":
        print("\n  Mirupafshim!")
    else:
        print("\n  Opsion i pavlefshëm.")

if __name__ == "__main__":
    main()
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
