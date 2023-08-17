# Print the board
def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()


# Joining '.' and 'Q'
# making combined 2D Array
# For output in desired format
def add_sol(board, ans, n):  # converts my soln board from a 2-d array to a list of strings and adds it to ans
    temp = []
    for i in range(n):
        string = ""
        for j in range(n):
            string += board[i][j]
        temp.append(
            string)  # temp here is a list of strings where each string represents a row in the board to be added to ans
    ans.append(temp)  # ans is a list of temps where each temp represents a solution board


# We need to check in three directions
# 1. in the same column above the current position
# 2. in the left top diagonal from the given cell
# 3. in the right top diagonal from the given cell
def is_safe(row, col, board, n):
    x = row
    y = col

    # Check for same upper col
    while (x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1

    # Check for Upper Right Diagonal
    x = row
    y = col
    while (y < n and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            y += 1
            x -= 1

    # Check for Upper Left diagonal
    x = row
    y = col
    while (y >= 0 and x >= 0):
        if board[x][y] == "Q":
            return False
        else:
            x -= 1
            y -= 1
    return True


# Function to solve n queens
# solveNQueens function here will fill the queens
# 1. there can be only one queen in one row
# 2. if we filled the final row in the board then row will
# be equal to total number of rows in board
# 3. push that board configuration in answer set because
# there will be more than one answers for filling the board
# with n-queens
def solveNQueens(row, ans, board, n):
    # Base Case
    # Queen is depicted by "Q"
    # adding solution to final answer array
    if row == n:
        add_sol(board, ans, n)
        return

    # Solve 1 case and rest recursion will follow
    for col in range(n):

        # For each position check if it is safe and if it
        # is safe make a recursive call with
        # row+1, board[i][j]='Q' and then revert the change
        # in board that is make the board[i][j]='.' again to
        # generate more solutions
        if is_safe(row, col, board, n):
            # If placing Queen is safe
            board[row][col] = "Q"
            solveNQueens(row + 1, ans, board, n)

            # Backtrack
            board[row][col] = "."

n = 4

board = [["." for i in range(n)] for j in range(n)]
ans = []
solveNQueens(0, ans, board, n)

if ans == []:
    print("Solution does not exist")
else:
    for i in range(len(ans)):
        print_board(ans[i], n)
        print()
