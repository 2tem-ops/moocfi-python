from random import choice
from string import ascii_lowercase

def generate_password(length: int) -> str:
    password = ""
    
    for _ in range(length):
        ltr = choice(ascii_lowercase)
        password += ltr
        
    return password
        
if __name__ == "__main__":
    print(generate_password(8))
    