def matrix_sum() -> int:
    total = 0
    
    with open("matrix.txt") as matrix:
        for line in matrix:
            line = [int(i) for i in line.replace('\n', '').split(",")]
            for num in line:
                total += num
                
    return total

def matrix_max() -> int:
    largest = -1000
    
    with open("matrix.txt") as matrix:
        for line in matrix:
            line = [int(i) for i in line.replace('\n', '').split(",")]
            for num in line:
                if num > largest:
                    largest = num
                    
    return largest
                

def row_sums() -> list[int]:
    res = []
    
    with open("matrix.txt") as matrix:
        for line in matrix:
            line = [int(i) for i in line.replace('\n', '').split(",")]
            res.append(sum(line))
            
    return res

if __name__ == "__main__":
    print(matrix_sum())
    print(matrix_max())
    print(row_sums())