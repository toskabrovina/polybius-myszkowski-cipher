# Myszkowski Transposition Cipher
# Implementim per enkriptim dhe dekriptim

from typing import List, Dict
def clean_text(text: str) -> str:
    return "".join(ch.upper() for ch in text if ch.isalnum())

def validate_keyword(keyword: str) -> str:
    clean_key = "".join(ch.upper() for ch in keyword if ch.isalpha())

    if len(clean_key) < 2:
        raise ValueError("Çelësi duhet me pas të paktën 2 shkronja.")

    return clean_key