def line(length, char):
    if char == "":
        print(length * "*")
    else:
        print(length * char[0])

def shape(size, char, height, char2):
    triangle = 1
    while triangle <= size:
        line(triangle, char)
        triangle += 1
    while height > 0:
        line(size, char2)
        height -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")