def everything_reversed(strings: list) -> list:
    result = []
    
    for string in strings:
        result.append(string[::-1])

    return result[::-1]


if __name__ == "__main__":
    my_list = ["Hi", "there", "example", "one more"]
    new_list = everything_reversed(my_list)
    print(new_list)