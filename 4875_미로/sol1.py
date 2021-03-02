import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    maze = [list(map(int, list(input()))) for _ in range(n)]
    visited = [[False]*n for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    stack = []
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                stack.append((i,j))
    flag = 0
    while stack:
        now = stack.pop()
        visited[now[0]][now[1]] = True
        y = now[0]
        x = now[1]
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if 0 <= temp_x < n and 0 <= temp_y < n:
                if (visited[temp_y][temp_x] == False) and (maze[temp_y][temp_x] == 0):
                    stack.append((temp_y, temp_x))
                elif (visited[temp_y][temp_x] == False) and (maze[temp_y][temp_x] == 3):
                    flag = 1
    print("#{} {}".format(tc, flag))

