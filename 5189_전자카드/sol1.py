import sys
sys.stdin = open('sample_input.txt')

T = int(input())

def solve(now, n, distance):
    global N, r
    if n == N-1:
        distance += country_club[now][0]
        if distance < r:
            r = distance
    else:
        for i in range(1, N):
            if not visited[i]:
                visited[i] = 1
                solve(i, n+1, distance+country_club[now][i])
                visited[i] = 0
for tc in range(1, T + 1):
    N = int(input())
    country_club = [list(map(int, input().split())) for _ in range(N)]
    r = 100000
    visited = [0] * (N)
    visited[0] = 1
    solve(0, 0, 0)
    print('#{} {}'.format(tc, r))
