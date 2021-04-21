import sys
sys.stdin = open("input.txt")

T = int(input())


def chess(y,x):
    for i in range(x):
        if board[y][i] == 1:
            return False
    for i, j in zip(range(y, -1, -1), range(x, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(y, n, 1), range(x, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve(idx):
    global cnt
    if idx == n:
        cnt += 1
        return

    for i in range(n):
        if chess(i, idx):
            board[i][idx] = 1
            solve(idx+1)
            board[i][idx] = 0


for tc in range(1, T+1):
    n = int(input())
    board = [[0 for _ in range(n)] for _ in range(n)]
    cnt = 0
    solve(0)
    print("#{} {}".format(tc, cnt))

