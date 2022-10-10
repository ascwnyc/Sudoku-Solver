# main.py

board = [
    [0, 0, 0, 2, 6, 0, 7, 0, 1],
    [6, 8, 0, 0, 7, 0, 0, 9, 0],
    [1, 9, 0, 0, 0, 4, 5, 0, 0],
    [8, 2, 0, 1, 0, 0, 0, 4, 0],
    [0, 0, 4, 6, 0, 2, 9, 0, 0],
    [0, 5, 0, 0, 0, 3, 0, 2, 8],
    [0, 0, 9, 3, 0, 0, 0, 7, 4],
    [0, 4, 0, 0, 5, 0, 0, 3, 6],
    [7, 0, 3, 0, 1, 8, 0, 0, 0]
]

def valid(bo, num, pos):

    # Check through each element in the row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check through each element in the column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check each 3x3 box in the Sudoku grid
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False

    # If all checks pass, return True
    return True

def solve(bo):

    # Base case of recursion
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    # Loop through each number 1-9
    for i in range(1,10):
        
        # Check if the solution is valid
        if valid(bo, i, (row, col)):
            
            # If true, add number to board
            bo[row][col] = i

            # Recursively call solve() to solve the rest of the board
            if solve(bo):
                return True
            
            # If the solution is not valid, reset the value to 0
            bo[row][col] = 0
    
    # If no solution is found, return false
    return False

def print_board(bo):

    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i, j) # return tuple: row, column

    return None

print(" ")
print("Unsolved Board")
print(" ")
print_board(board)
solve(board)
print(" ")
print("Solved Board")
print(" ")
print_board(board)