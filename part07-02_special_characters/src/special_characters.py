from string import ascii_letters, punctuation

def separate_characters(my_string: str):
    res1 = []
    res2 = []
    res3 = []
    for i in my_string:
        if i in ascii_letters:
            res1.append(i)
        elif i in punctuation:
            res2.append(i)
        else:
            res3.append(i)
    return "".join(res1), "".join(res2), "".join(res3)

if __name__ == "__main__":
    parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
    print(parts[0])
    print(parts[1])
    print(parts[2])