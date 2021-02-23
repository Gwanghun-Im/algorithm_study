import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    v, e = map(int, input().split())
    # edges = [[0] * (v+1) for _ in range(v+1)]
    # for i in range(e):
    #     x, y = map(int, input().split())
    #     edges[x][y] = 1
    edges = [[] for _ in range(v+1)]
    for i in range(e):
        x, y = map(int, input().split())
        edges[x].append(y)
    s, g = map(int, input().split())

    stack = [s]
    visited = [False] * (v+1)

    while stack:
        now = stack.pop()

        if visited[now]:
            pass
        else:
            visited[now] = True
            for edge in edges[now]:
                if not visited[edge]:
                    stack.append(edge)
    if visited[g]:
        result = 1
    else:
        result = 0

    print("#{} {}".format(tc, result))

