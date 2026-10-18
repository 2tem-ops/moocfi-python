def read_fruits() -> dict:
    res = {}
    with open("fruits.csv") as file:
        for line in file:
            line = line.replace("\n", "").split(";")
            fruit = line[0]
            price = line[1]
            res[fruit] = float(price)
    return res

if __name__ == "__main__":
    print(read_fruits())