def all_the_longest(words: list) -> list:
    longest = ""
    best = []
    for word in words:
        if len(word) > len(longest):
            longest = word
    for word in words:
        if len(word) == len(longest):
            best.append(word)
    return best


if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['dorothy', 'richard']