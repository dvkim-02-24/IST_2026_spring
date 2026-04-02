import typing as tp
import string

def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    ciphertext = ""
    shift = shift % 26
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    table = str.maketrans(lower + upper, lower[shift:] + lower[:shift] + upper[shift:] + upper[:shift])
    return plaintext.translate(table)


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    plaintext = ""
    return encrypt_caesar(ciphertext, -shift)

def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    best_shift = 0
    max_matches = 0
    for shift in range(26):
        decrypted = decrypt_caesar(ciphertext, shift)
        matches = sum(1 for word in decrypted.split() if word.lower() in dictionary)
        if matches > max_matches:
            max_matches = matches
            best_shift = shift
    return best_shift

print(caesar_breaker_brute_force("“wfcehcqvy’cefscprr,mn.xlcyxaj!”"))