def greatest_number(x: int, y: int, z: int):
    if x >= y and x >= z:
        return x
    elif y >= x and y >= z:
        return y
    elif z >= x and z >= y:
        return z



# You can test your function by calling it within the following block
if __name__ == "__main__":
    greatest = greatest_number(1, 1, -100)
    print(greatest)