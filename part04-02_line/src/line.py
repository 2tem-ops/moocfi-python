def line(length, char):
    if char == "":
        print(length * "*")
    else:
        print(length * char[0])




# Write your solution here
# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "")