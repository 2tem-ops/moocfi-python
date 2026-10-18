def double_items(numbers: list) -> list:
    res = []
    for i in range(len(numbers)):
        res.append(numbers[i] * 2)
    return res
        
if __name__ == "__main__":
    numbers = [2, 4, 5, 3, 11, -4]
    numbers_doubled = double_items(numbers)
    print("original:", numbers)
    print("doubled:", numbers_doubled)