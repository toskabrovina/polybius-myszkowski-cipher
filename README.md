# Cryptography Project: Myszkowski & Polybius Ciphers
Ky projekt përmban implementimin e dy algoritmeve klasike të kriptografisë në Python:
- Myszkowski Transposition Cipher
- Polybius Square Cipher

##### Të dy algoritmet mbështesin:
- Enkriptim (Encryption)
- Dekriptim (Decryption)
- Demo interaktive
---
## Myszkowski Transposition Cipher
###  Përshkrimi:

Myszkowski Cipher është një variant i columnar transposition cipher.

**Karakteristikat kryesore:**
- Teksti vendoset në një matricë sipas një keyword-i
- Kolonat lexohen sipas renditjes së shkronjave
- Shkronjat e njëjta në keyword trajtohen së bashku

**Si funksionon:**

1. Pastrohet plaintext (hiqen karakteret e panevojshme)
2. Teksti ndahet në rreshta sipas gjatësisë së keyword-it
3. Ndërtohet një matricë
4. Kolonat lexohen sipas renditjes së shkronjave
5. Formohet ciphertext

----
## Polybius Square Cipher
###  Përshkrimi:

Polybius Cipher është një metodë zëvendësimi që përdor një matricë 5x5.

**Karakteristikat kryesore:**

- Çdo shkronjë zëvendësohet me koordinata (rresht, kolonë)
- Mund të përdoret keyword për personalizim
- Përdor matricë 5x5

**Si funksionon:**

1. Ndërtohet matrica (me ose pa keyword)
2. Çdo shkronjë kthehet në koordinata
3. Formohet ciphertext si numra

----
**Si të Ekzekutohet Projekti:**

1. Klono repository-n:

git clone <https://github.com/toskabrovina/polybius-myszkowski-cipher.git>

2. Hape projektin në IDE (IntelliJ / PyCharm)

3. Ekzekuto:

python myszkowski.py

ose

python polybius.py

4. Ndiq menynë në terminal për:

- Enkriptim
- Dekriptim
- Demo

<img width="475" height="183" alt="image" src="https://github.com/user-attachments/assets/5f5ca102-0623-4ef8-ad1a-619758b935f6" />


