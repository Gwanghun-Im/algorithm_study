import sys
sys.stdin = open("input.txt")

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def solve(y,x,c,s):
    if c == 6:
        r.add(s)
        return
    for d in range(4):
        ty, tx = y+dy[d], x+dx[d]
        if 0<=ty<4 and 0<=tx<4:
            solve(ty, tx, c+1, s+grid[ty][tx])

for tc in range(1, T+1):
    grid = [list(input().split())for i in range(4)]
    r = set()
    for i in range(4):
        for j in range(4):
            solve(i, j, 0, grid[i][j])
    print("#{} {}".format(tc, len(r)))

