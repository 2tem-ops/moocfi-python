def read_input(statement: str, b1: int, b2: int) -> int:
    while True:
        try:
            number = int(input(statement))
        except ValueError:
            print(f"You must type in an integer between {b1} and {b2}")
            continue
        if number < b1 or number > b2:
            print(f"You must type in an integer between {b1} and {b2}")
            continue
        else:
            return number
            
if __name__ == "__main__":
    number = read_input("Please type in a number: ", 5, 10)
    print("You typed in:", number)