items = int(input("How many items: "))
counter = 1
item_list = []

while counter <= items:
    value = int(input(f"Item {counter}: "))
    item_list.append(value)
    counter += 1

print(item_list)


