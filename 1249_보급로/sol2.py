import sys
sys.stdin = open("input.txt")

from collections import deque

T = int(input())

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]


def bfs():
    queue = deque()
    queue.append((0, 0))
    while queue:
        y, x = queue.popleft()
        for i in range(4):
            my = y + dy[i]
            mx = x + dx[i]
            if 0 <= my < n and 0 <= mx < n:
                if dp[my][mx] > dp[y][x] + Map[my][mx]:
                    queue.append((my, mx))
                    dp[my][mx] = dp[y][x] + Map[my][mx]



for tc in range(1, T+1):
    n = int(input())
    Map = [list(map(int, list(input()))) for _ in range(n)]
    dp = [[float('inf') for _ in range(n)] for _ in range(n)]
    dp[0][0] = Map[0][0]
    bfs()

    print("#{} {}".format(tc, dp[-1][-1]))

