items = []

while True:
    new = int(input("New item: "))
    if new == 0:
        break
    
    items.append(new)
    print(f"The list now: {items}")
    print(f"The list in order: {sorted(items)}")

print("Bye!")

