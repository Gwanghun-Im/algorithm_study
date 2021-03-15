import sys
sys.stdin = open("input.txt")

T = int(input())


dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

tunnel = [[],
          [0, 1, 2, 3],
          [0, 2],
          [1, 3],
          [0, 1],
          [1, 2],
          [2, 3],
          [3, 0]]

can_i = [[1, 2, 5, 6],
         [1, 3, 6, 7],
         [1, 2, 4, 7],
         [1, 3, 4, 5]
         ]
for tc in range(1, T+1):
    n, m, r, c, l = map(int, input().split())
    underground = [list(map(int, input().split())) for _ in range(n)]
    visited = [[False] * m for _ in range(n)]
    cnt = 0
    stack = [[] for _ in range(l+1)]
    stack[0].append([r, c])
    visited[r][c] = True
    for i in range(l):
        while stack[i]:
            now = stack[i].pop()
            position = underground[now[0]][now[1]]
            cnt += 1
            for d in tunnel[position]:
                temp_y = now[0]+dy[d]
                temp_x = now[1]+dx[d]
                if 0 <= temp_y < n and 0 <= temp_x < m and (underground[temp_y][temp_x] in can_i[d]) and (not visited[temp_y][temp_x]):
                    visited[temp_y][temp_x] = True
                    stack[i+1].append([temp_y, temp_x])

    print("#{} {}".format(tc, cnt))

