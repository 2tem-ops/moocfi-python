def no_shouting(strings: list) -> list:
    pruned = []

    for string in strings:
        if not string.isupper():
            pruned.append(string)
            
    return pruned
            


if __name__ == "__main__":
    my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
    pruned_list = no_shouting(my_list)
    print(pruned_list)