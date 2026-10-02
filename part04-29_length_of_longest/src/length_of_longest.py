def length_of_longest(words: list) -> int:
    longest = ""
    for word in words:
        if len(word) > len(longest):
            longest = word
    return len(longest)

if __name__ == "__main__":
    my_list = ["first", "second", "fourth", "eleventh"]
    result = length_of_longest(my_list)
    print(result)