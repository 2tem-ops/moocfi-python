def same_chars(word: str, index1: int, index2: int):
    if index1 >= len(word) or index2 >= len(word):
        return False
    elif word[index1] == word[index2]:
        return True
    else:
        return False


# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("programmer", 1, 10))