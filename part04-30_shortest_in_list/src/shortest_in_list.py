def shortest(words: list) -> str:
    shortest = "A" * 50
    for word in words:
        if len(word) < len(shortest):
            shortest = word
    return shortest

if __name__ == "__main__":
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(result)