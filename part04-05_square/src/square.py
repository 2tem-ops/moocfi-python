def line(length, char):
    if char == "":
        print(length * "*")
    else:
        print(length * char[0])

def square(size: int, character: str):
    square = size
    while square > 0:
        line(size, character)
        square -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "x")