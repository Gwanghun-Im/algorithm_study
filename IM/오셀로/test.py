import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    othello = [[0]*n for _ in range(n)]
    othello[n//2 - 1][n//2 - 1], othello[n//2][n//2] = 2, 2
    othello[n//2][n//2 - 1], othello[n//2 - 1][n//2] = 1, 1
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    for i in range(m):
        x, y, c = map(int, input().split())
        y -= 1
        x -= 1
        othello[y][x] = c
        for j in range(8):
            temp_x = x + dx[j]
            temp_y = y + dy[j]
            box = []
            while 0 <= temp_y < n and 0 <= temp_x < n and othello[temp_y][temp_x] and othello[temp_y][temp_x] != c:
                box.append((temp_y, temp_x))
                temp_y += dy[j]
                temp_x += dx[j]
                if 0 <= temp_y < n and 0 <= temp_x < n and othello[temp_y][temp_x] and othello[temp_y][temp_x] == c:
                    for b in box:
                        othello[b[0]][b[1]] = c
                    break

    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if othello[i][j] == 1:
                black += 1
            elif othello[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc+1, black, white))
