# NQUEENS PROBLEM
global N
N = int(input("enter a value for n:"))

def structure(board):  # structure of board
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()


def issafe(board, col, row):  # checking where to place the queen
    for i in range(
        col
    ):  # i is a variable do not consider it as row,col is the final point,intial point is 0 by default,step count is 1 by default
        if board[row][i] == 1:  # checking the left side part
            return False
    for i, j in zip(
        range(row, -1, -1), range(col, -1, -1)
    ):  # checking upper left diagonal ,range(intial,final,step count)
        if board[i][j] == 1:
            return False
    for i, j in zip(
        range(row, N, 1), range(col, -1, -1)
    ):  # checking the lower diagonal,range(intial,final,step count)
        if board[i][j] == 1:
            return False
    return True


def checking(board, col):
    if col >= N:  # stoping when a queen is placed (or after getting solution)
        structure(board)  # prints solution board
        print()
        return True
    res = False  # if no solution then false
    for i in range(N):
        if issafe(board, col, i):
            board[i][col] = 1

            res = (
                checking(board, col + 1) or res
            )  # recursion, res gets updated if true otherwise just retains the previous solution returns res=false
            board[i][
                col
            ] = 0  # backtracking(erasing one and replacing it back with zero)
    return res


def solution():
    board = [[0] * N for _ in range(N)]
    if checking(board, 0) == False:
        print("solution does not exist")
        return False


solution()
