import sys
sys.stdin = open("input.txt")

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def dfs(li):
    global line,n
    if not li:
        temp = 0
        for i in range(len(cell)):
            for j in range(len(cell[0])):
                if cell[i][j] == 2:
                    temp += 1
        if temp < line:
            line = temp
    else:
        now = li[0]
        for d in range(4):
            y = now[0]
            x = now[1]
            go = 0
            while True:
                y += dy[d]
                x += dx[d]
                if not(0 <= y < n) or not(0 <= x < n):
                    dfs(li[1:])
                    break
                elif cell[y][x]:
                    break
                else:
                    cell[y][x] = 2
                    go += 1
            while go:
                y -= dy[d]
                x -= dx[d]
                cell[y][x] = 0
                go -= 1


for tc in range(1, T+1):
    n = int(input())
    cell = [list(map(int, input().split())) for _ in range(n)]
    line = n**2
    queue = []
    for i in range(len(cell)):
        for j in range(len(cell[0])):
            if cell[i][j]:
                queue.append([i,j])
    dfs(queue)

    print("#%d %d"%(tc, line))

