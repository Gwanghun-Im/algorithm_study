import sys
sys.stdin = open("sample_input.txt")

T = int(input())


def get_parent(x):
    if p[x] != x:
        p[x] = get_parent(p[x])
    return p[x]


def union_parent(x, y, w):
    global r
    a = get_parent(x)
    b = get_parent(y)
    if a == b:
        return
    if a > b:
        p[a] = b
    else:
        p[b] = a
    r += w

for tc in range(1, T+1):
    v, e = map(int, input().split())
    p = [i for i in range(v+1)]
    edges = [list(map(int, input().split())) for _ in range(e)]
    edges.sort(key=lambda x: -x[2])

    r = 0
    while edges:
        n1, n2, w = edges.pop()
        union_parent(n1, n2, w)

    print("#{} {}".format(tc, r))

