import sys
sys.stdin = open("input.txt")

T = 10

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]

for _ in range(10):
    tc = input()
    maze = [list(map(int, list(input()))) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]
    queue = []
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                queue.append((i, j))
    flag = 0
    while queue:
        y, x = queue.pop(0)
        visited[y][x] = True
        for i in range(4):
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            if not visited[temp_y][temp_x] and (maze[temp_y][temp_x] == 0):
                queue.append((temp_y, temp_x))
            elif maze[temp_y][temp_x] == 3:
                flag = 1
    print("#{} {}".format(tc, flag))

