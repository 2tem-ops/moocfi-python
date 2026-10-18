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



if __name__ == "__main__":
    sudoku = [
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
    
    print(block_correct(sudoku, 0, 0))
    print(block_correct(sudoku, 1, 2))