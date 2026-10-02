def sum_of_positives(numbers: list) -> int:
    helper = []
    for i in numbers:
        if i > 0:
            helper.append(i)
    return sum(helper)

if __name__ == "__main__":
    my_list = [1, 2, -2, -5, -4, 3, 6, 8]
    print(sum_of_positives(my_list))