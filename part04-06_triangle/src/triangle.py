def line(length, char):
    if char == "":
        print(length * "*")
    else:
        print(length * char[0])

def triangle(size):
    triangle = 1
    while triangle <= size:
        line(triangle, "#")
        triangle += 1
        

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(3)
