list = [1, 2, 3, 4, 5]

while True:
    index = int(input("Index: "))
    if str(index) == "-1":
        break
    value = int(input("New value: "))
    list[index] = value
    print(list)
