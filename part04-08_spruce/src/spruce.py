def spruce(size):
    print("a spruce!")
    row = "*"
    final = size - 1

    while size > 0:
        print(" " * (size - 1) + row)
        row += "**"
        size -= 1
    print(" " * final + "*")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)