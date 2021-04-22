import sys
sys.stdin = open("sample_input.txt")

from  collections import deque

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]

for tc in range(1, T+1):
    n = int(input())
    Map = [list(map(int, input().split())) for _ in range(n)]
    dis = [[float('inf') for _ in range(n)] for _ in range(n)]
    dis[0][0] = 0
    q = deque()
    q.append((0, 0))
    while q:
        y, x = q.popleft()
        for i in range(4):
            my = y + dy[i]
            mx = x + dx[i]
            if 0 <= my < n and 0 <= mx < n:
                temp = 1 + (abs(Map[my][mx] - Map[y][x]) if Map[my][mx] > Map[y][x] else 0)
                if dis[y][x] + temp < dis[my][mx]:
                    dis[my][mx] = dis[y][x] + temp
                    q.append((my, mx))
    print("#{} {}".format(tc, dis[-1][-1]))

