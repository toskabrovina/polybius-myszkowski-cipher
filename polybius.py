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


def demo_polybius():

    keyword = input("  Keyword (Press \"<ENTER>\" for basic Latin alphabet): ").strip()
    ps = PolybiusSquare(keyword)
       
    plaintext = input("  Plaintext: ").strip()
    encrypted = ps.encrypt(plaintext)

    print(f"\n  Original Text : {plaintext.upper()}")
    print(f"  Encrypted Text: {encrypted}")


def main():
    print("=" * 50)
    print(" Polybius Square Cipher")
    print("=" * 50)
    
    demo_polybius()


if __name__ == "__main__":
    main()