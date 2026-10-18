def print_sudoku(sudoku: list):
    count = 2
    for row in sudoku:
        count += 1
        if count == 3:
            print()
            count = 0
        for square in row:
            if square > 0:
                print(f" {square}", end="")
            else:
                print(" _", end="")
        print()

def add_number(sudoku: list, row_no: int):
    pass

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

    print_sudoku(sudoku)
    #add_number(sudoku, 0, 0, 2)
    #add_number(sudoku, 1, 2, 7)
    #add_number(sudoku, 5, 7, 3)
    #print()
    #print("Three numbers added:")
    #print()
    #print_sudoku(sudoku)