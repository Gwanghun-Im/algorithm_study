import sys
sys.stdin = open("input.txt")

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

def dfs(y, x, sum_num):
    global r
    if sum_num > r:
        return
    if y == x == n-1:
        r = sum_num
    for i in range(4):
        my = y+dy[i]
        mx = x+dx[i]
        if 0<= my<n and 0<=mx<n and not visited[my][mx]:
            visited[my][mx] = 1
            dfs(my, mx, sum_num + Map[my][mx])
            visited[my][mx] = 0

for tc in range(1, T+1):
    n = int(input())
    Map = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    r = float('inf')
    visited[0][0] = 1
    dfs(0, 0, Map[0][0])

    print("#{} {}".format(tc, r))

