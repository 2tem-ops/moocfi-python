from random import choice, shuffle
from string import ascii_lowercase, digits as digit_chars

def generate_strong_password(length: int, numbers: bool, special_characters: bool) -> str:
    special_chars = "!?=+-()#"
    required = [ascii_lowercase]
    allowed = ascii_lowercase

    if numbers:
        required.append(digit_chars)
        allowed += digit_chars

    if special_characters:
        required.append(special_chars)
        allowed += special_chars

    password = [choice(characters) for characters in required]

    while len(password) < length:
        password.append(choice(allowed))

    shuffle(password)

    return "".join(password)


if __name__ == "__main__":
    print(generate_strong_password(5, True, True))