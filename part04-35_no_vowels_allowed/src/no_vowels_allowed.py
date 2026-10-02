def no_vowels(string: str) -> str:
    vowels = ["a", "e", "i", "o", "u"]
    result = ""
    
    for char in string:
        if char not in vowels:
            result += char
    return result

if __name__ == "__main__":
    my_string = "this is an example"
    print(no_vowels(my_string))