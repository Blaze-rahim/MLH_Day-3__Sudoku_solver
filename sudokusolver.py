matrix_size = 9

def printing(arr):
    for i in range(matrix_size):
        for j in range(matrix_size):
            print(arr[i][j], end = " ")
        print()


def checker(board, row, colmn, num):
  
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][colmn] == num:
            return False

    startRow = row - row % 3
    startcolmn = colmn - colmn % 3
    
    for i in range(3):
        for j in range(3):
            if board[i + startRow][j + startcolmn] == num:
                return False
    
    return True


def sudoku_solver(board, row, colmn):
  
    if (row == matrix_size - 1 and colmn == matrix_size):
        return True

    if colmn == matrix_size:
        row += 1
        colmn = 0

    if board[row][colmn] > 0:
        return sudoku_solver(board, row, colmn + 1)
    
    for num in range(1, matrix_size + 1, 1):
      
        if checker(board, row, colmn, num):
          
            board[row][colmn] = num

            if sudoku_solver(board, row, colmn + 1):
                return True

        board[row][colmn] = 0
    
    return False

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

if (sudoku_solver(board, 0, 0)):
    printing(board)

else:
    print("no solution")