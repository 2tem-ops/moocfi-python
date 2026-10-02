def range_of_list(numbers: list) -> int:
    largest = max(numbers)
    smallest = min(numbers)
    return largest - smallest


if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    result = range_of_list(my_list)
    print(result)