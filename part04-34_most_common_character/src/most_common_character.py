def most_common_character(string: str) -> str:
    best = string[0]
    for char in string:
        if string.count(char) > string.count(best):
            best = char
    return best

if __name__ == "__main__":
    first_string = "abcdbde"
    print(most_common_character(first_string))

    second_string = "exemplaryelementary"
    print(most_common_character(second_string))