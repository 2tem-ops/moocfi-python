def row_correct(sudoku: list, row_no: int) -> bool:
    row = sudoku[row_no]
    filter = [item for item in row if item != 0]
    return len(filter) == len(set(filter))

def column_correct(sudoku: list, column_no: int) -> bool:
    numbers = []
    
    for row in sudoku:
        if row[column_no] > 0 and row[column_no] in numbers:
            return False
        numbers.append(row[column_no])
        
    return True

def block_correct(sudoku: list, row_no: int, column_no: int) -> bool:
    numbers = []
    start_row = (row_no // 3) * 3
    start_col = (column_no // 3) * 3
    
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            value = sudoku[r][c]
            
            if value == 0:
                continue
            
            if value in numbers:
                return False
            
            numbers.append(value)
            
    return True

def sudoku_grid_correct(sudoku: list) -> bool:
    flag = False
    check1, check2, check3 = [], [], []
    
    for i in range(len(sudoku)):
        check1.append(row_correct(sudoku, i))
        check2.append(column_correct(sudoku, i))
        
    block_check = [
        [0, 0], [0, 3], [0, 6],
        [3, 0], [3, 3], [3, 6],
        [6, 0], [6, 3], [6, 6]
    ]
    
    for row in block_check:
        check3.append(block_correct(sudoku, row[0], row[1])) 
        
    if all(check1) == True and all(check2) == True and all(check3) == True:
        flag = True
        
    if flag:
        return True
    return False
        
        


if __name__ == "__main__":
    sudoku1 = [
  [9, 0, 0, 0, 8, 0, 3, 0, 0],
  [2, 0, 0, 2, 5, 0, 7, 0, 0],
  [0, 2, 0, 3, 0, 0, 0, 0, 4],
  [2, 9, 4, 0, 0, 0, 0, 0, 0],
  [0, 0, 0, 7, 3, 0, 5, 6, 0],
  [7, 0, 5, 0, 6, 0, 4, 0, 0],
  [0, 0, 7, 8, 0, 3, 9, 0, 0],
  [0, 0, 1, 0, 0, 0, 0, 0, 3],
  [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    
    print(sudoku_grid_correct(sudoku1))
    
    sudoku2 = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    print(sudoku_grid_correct(sudoku2))