import sys
sys.stdin = open("sample_input.txt")

T = int(input())

def dfs(n):
    if v[n]:
        return False
    v[n] = 1
    for i in g[n]:
        dfs(i)
    return True


for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    g = [[] for _ in range(n+1)]
    v = [0] * (n+1)
    for i in range(0, m*2, 2):
        g[li[i]].append(li[i+1])
        g[li[i+1]].append(li[i])

    cnt = 0
    for i in range(1, n+1):
        if dfs(i):
            cnt += 1

    print("#{} {}".format(tc, cnt))

