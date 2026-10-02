def first_word(string: str):
    index = 0
    mass = ""
    while True:
        mass += string[index]
        index += 1
        if string[index] == " ":
             break
    return mass

def second_word(string: str):
    firstword = len(first_word(string))
    index = firstword + 1
    mass = ""
    while index < len(string):
        if string[index] == " ":
            break
        mass += string[index]
        index += 1
    return mass

def last_word(string: str):
    index = -1
    mass = ""
    while True:
        index -= 1
        if string[index] == " ":
            break
    while True:
        index += 1
        mass += string[index]
        if index == -1:
            break
    return mass


# You can test your function by calling it within the following block
if __name__ == "__main__":
    sentence = "first second"
    print(first_word(sentence))
    print(second_word(sentence))
    print(last_word(sentence))