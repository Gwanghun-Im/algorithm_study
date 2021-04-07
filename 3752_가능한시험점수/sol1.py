import sys
sys.stdin = open("input.txt")

T = int(input())


def dfs(idx, r):
    global n, cnt
    if visited[idx][r]:
        return
    visited[idx][r] = True
    if idx == n:
        cnt += 1
    else:
        dfs(idx+1, r)
        dfs(idx+1, r + scores[idx])


for tc in range(1, T+1):
    n = int(input())
    scores = list(map(int, input().split()))
    visited = [[False]*(sum(scores)+1) for _ in range(n+1)]
    cnt = 0
    dfs(0, 0)

    print("#{} {}".format(tc, cnt))

