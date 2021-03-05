import sys
sys.stdin = open("input.txt")

T = int(input())


def bfs(n):
    global flag, result
    if not queue:
        return
    # 반복된 횟수 추가
    result += 1
    temp_n = 0
    # 큐에 추가된 만큼만 반복한다.
    for _ in range(n):
        node = queue.pop(0)
        visited[node] = True
        for i in edges[node]:
            if not visited[i]:
                queue.append(i)
                temp_n += 1
            if i == g:
                flag = 1
    # 목표지점과 못 만났으면 한번더
    if not flag:
        bfs(temp_n)


for tc in range(1, T+1):
    v, e = map(int, input().split())
    edges = [[] for _ in range(v+1)]
    for i in range(e):
        n1, n2 = map(int, input().split())
        edges[n1].append(n2)
        edges[n2].append(n1)
    s, g = map(int, input().split())
    # 방문여부
    visited = [False] * (v+1)
    queue = [s]
    result = 0
    # 목표지점과 만남?
    flag = 0
    bfs(1)
    result = 0 if not flag else result

    print("#{} {}".format(tc, result))

