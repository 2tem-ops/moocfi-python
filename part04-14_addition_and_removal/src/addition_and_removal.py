numbers = []

while True:
    print(f"The list is now {numbers}")
    operation = input("a(d)d, (r)emove or e(x)it: ")
    if operation.upper() == "D":
        numbers.append(len(numbers) + 1)
    elif operation.upper() == "R":
        if numbers:
            numbers.remove(len(numbers))
        else:
            continue
    elif operation.upper() == "X":
        break

print("Bye!")