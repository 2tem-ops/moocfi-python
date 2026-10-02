def list_of_stars(numbers: list):
    for number in numbers:
        print("*" * number)
        


if __name__ == "__main__":
    print(list_of_stars([3, 7, 1, 1, 2]))