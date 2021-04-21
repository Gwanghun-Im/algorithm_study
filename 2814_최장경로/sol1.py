import sys
sys.stdin = open("sample_input.txt")

T = int(input())


def dfs(idx,n):
    global cnt
    for i in node[idx]:
        if not visited[i]:
            visited[i] = 1
            dfs(i,n+1)
            visited[i] = 0
    if n > cnt:
        cnt = n

for tc in range(1, T+1):
    n, m = map(int, input().split())
    node = [[] for _ in range(11)]
    for i in range(m):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    visited = [0]*11
    cnt = 0
    for i in range(1, n+1):
        visited[i] = 1
        dfs(i, 1)
        visited[i] = 0
    print("#{} {}".format(tc, cnt))

