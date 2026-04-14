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