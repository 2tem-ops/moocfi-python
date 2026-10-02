def list_sum(num1: list, num2: list) -> list:
    index = 0
    work = num1
    work2 = num2
    while index != len(work):
        work[index] += work2[index]
        index += 1
    return work


if __name__ == "__main__":
    a = [1, 2, 3]
    b = [7, 8, 9]
    print(list_sum(a, b)) # [8, 10, 12]