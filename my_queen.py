def print_board(board,n):
    for i in range(n):
        for j in range(n):
            print(board[i][j],end=" ")
        print()

def is_safe(board,n,row,col):
    x = row
    y = col
    while(x>=0):
        if (board[x][y] == "Q"):
            return False
        else:
            x = x-1
    x = row
    y = col
    while(x>=0 and y>=0):
        if (board[x][y] == "Q"):
            return False
        else:
            x = x-1
            y = y-1
    x = row
    y = col
    while(x>=0 and y<n):
        if (board[x][y] == "Q"):
            return False
        else:
            x = x-1
            y = y+1
    return True

def add_ans(board,n,ans):
    temp = []
    for i in range(n):
        string =""
        for j in range(n):
            string+=board[i][j]
        temp.append(string)
    ans.append(temp)



def solveNqueens(board,n,row,ans):
    if (row == n):
        add_ans(board,n,ans)
        return
    for col in range(n):
        if is_safe(board,n,row,col):
            board[row][col] = "Q"
            solveNqueens(board,n,row + 1,ans)
            board[row][col] = "."

n = 4 
ans = []
board = [["." for i in range(n)] for j in range(n)]
solveNqueens(board,n,0,ans)

if ans == []:
    print("no soln")
else:
    for i in range(len(ans)):
        print_board(ans[i],n)
        print()
