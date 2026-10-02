def line(length, char):
    if char == "":
        print(length * "*")
    else:
        print(length * char[0])

def square_of_hashes(size):
    square = size
    while size > 0:
        line(square, "#")
        size -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(3)
