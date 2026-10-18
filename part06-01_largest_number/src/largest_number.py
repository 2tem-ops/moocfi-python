def largest() -> int:
    with open("numbers.txt") as file:
        return max([int(i) for i in file])
        
        
if __name__ == "__main__":
    largest()