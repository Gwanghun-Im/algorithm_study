import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    v, e = map(int, input().split())
    edges = [[0] * (v+1) for _ in range(v+1)]
    for i in range(e):
        x, y = map(int, input().split())
        edges[x][y] = 1

    s, g = map(int, input().split())
    stack = [s]
    visited = [False] * (v+1)

    while stack:
        now = stack.pop()

        if not visited[now]:
            visited[now] = True

            for i in range(v+1):
                if not visited[i] and edges[now][i]:
                    stack.append(i)

    result = 1 if visited[g] else 0

    print("#{} {}".format(tc, result))

