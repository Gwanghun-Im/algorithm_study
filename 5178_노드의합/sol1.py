import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    n, m, l = map(int, input().split())
    nodes = [0] * (n+1)

    for i in range(m):
        idx, val = map(int, input().split())
        nodes[idx] = val

    for i in range(n, 0, -1):
        if nodes[i]:
            continue
        left = nodes[i*2] if i*2 <= n else 0
        right = nodes[i*2 + 1] if i*2 + 1 <= n else 0

        nodes[i] = left + right

    print("#{} {}".format(tc, nodes[l]))

