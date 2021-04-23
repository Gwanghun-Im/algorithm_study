import sys
sys.stdin = open("input.txt")

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
    n = int(input())
    x_li = list(map(int, input().split()))
    y_li = list(map(int, input().split()))
    e = float(input())
    p = [i for i in range(n)]
    edges = []
    for i in range(n):
        for j in range(i):
            edges.append((i, j, e*((x_li[i] - x_li[j])**2+(y_li[i]-y_li[j])**2)))
    edges.sort(key=lambda x: -x[2])
    r = 0
    while edges:
        n1, n2, w = edges.pop()
        union_parent(n1, n2, w)
    print("#{} {:.0f}".format(tc, r))

