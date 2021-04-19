import sys
sys.stdin = open("input.txt")

T = int(input())

def solve(idx, p):
    global prop,n

    if p <= prop:
        return

    if idx == n:
        prop = p
        return

    for i in range(n):
        if not v[i]:
            v[i] = 1
            solve(idx+1, p*P[idx][i]/100)
            v[i] = 0

for tc in range(1, T+1):
    n = int(input())
    P = [list(map(int, input().split())) for _ in range(n)]
    v = [0]*n
    prop = 0
    solve(0,1)
    print("#{} {:6f}".format(tc, prop*100))

