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
1.Pastrohet plaintext (hiqen karakteret e panevojshme)
2.Teksti ndahet në rreshta sipas gjatësisë së keyword-it
3.Ndërtohet një matricë
4.Kolonat lexohen sipas renditjes së shkronjave
5.Formohet ciphertext

----
**Si të Ekzekutohet Projekti:**
Klono repository-n:
git clone <https://github.com/toskabrovina/polybius-myszkowski-cipher.git>
Hape projektin në IDE (IntelliJ / PyCharm)
Ekzekuto:
python myszkowski.py

ose

python polybius.py
Ndiq menynë në terminal për:
- Enkriptim
- Dekriptim
- Demo

