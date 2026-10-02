def distinct_numbers(nums: list) -> list:
    original = nums
    result = []
    for i in nums:
        if i not in result:
            result.append(i)
    return sorted(result)

if __name__ == "__main__":
    my_list = [1, 10, 1, 100, 1, 1000]
    print(distinct_numbers(my_list)) # [1, 2, 3]