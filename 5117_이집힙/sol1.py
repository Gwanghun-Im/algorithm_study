import sys
sys.stdin = open("input.txt")

T = int(input())

def tree_insert(value,idx):
    p = idx//2
    if nodes[p] < value:
        nodes[idx] = value
    else:
        nodes[idx] = nodes[p]
        tree_insert(value, p)


for tc in range(1, T+1):
    n = int(input())
    vals = list(map(int, input().split()))
    nodes = [0]*(n+1)

    idx = 1
    for v in vals:
        tree_insert(v, idx)
        idx += 1

    res = 0
    while n:
        n = n // 2
        res += nodes[n]
    print("#{} {}".format(tc, res))

