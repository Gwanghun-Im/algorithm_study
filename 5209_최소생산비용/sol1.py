import sys
sys.stdin = open("sample_input.txt")

T = int(input())


def solve(idx, p):
    global best, n

    if p > best:
        return

    if idx == n:
        best = p
        return

    for i in range(n):
        if not v[i]:
            v[i] = 1
            solve(idx + 1, p + fac[idx][i])
            v[i] = 0

for tc in range(1, T+1):
    n = int(input())
    fac = [list(map(int, input().split())) for _ in range(n)]
    v = [0] * n
    best = 99*n
    solve(0,0)

    print("#{} {}".format(tc, best))

