import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, X = map(int, input().split())
    forward = [[0 for _ in range(N)] for _ in range(N)]
    reverse = [[0 for _ in range(N)] for _ in range(N)]
    from_insu = [float('inf')] * N
    to_insu = [float('inf')] * N
    from_insu[X-1], to_insu[X-1] = 0, 0
    for _ in range(M):
        x, y, c = map(int, input().split())
        forward[x-1][y-1] = c
        reverse[y-1][x-1] = c
        if x == X:
            from_insu[y-1] = c
        if y == X:
            to_insu[x-1] = c

    # i = 도착지점
    # j = 출발지점
    for i in range(N):
        for j in range(N):
            # 가는길이 존재할때
            if forward[j][i] and from_insu[i] > from_insu[j]+forward[j][i]:
                from_insu[i] = from_insu[j] + forward[j][i]
            # 오는 길이 존재할 때
            if reverse[j][i] and to_insu[i] > to_insu[j] + reverse[j][i]:
                to_insu[i] = to_insu[j] + reverse[j][i]

    for i in range(N-1, 0, -1):
        for j in range(N-1, 0, -1):
            # 가는길이 존재할때
            if forward[j][i] and from_insu[i] > from_insu[j]+forward[j][i]:
                from_insu[i] = from_insu[j] + forward[j][i]
            # 오는 길이 존재할 때
            if reverse[j][i] and to_insu[i] > to_insu[j] + reverse[j][i]:
                to_insu[i] = to_insu[j] + reverse[j][i]

    for i in range(N):
        for j in range(N):
            # 가는길이 존재할때
            if forward[j][i] and from_insu[i] > from_insu[j]+forward[j][i]:
                from_insu[i] = from_insu[j] + forward[j][i]
            # 오는 길이 존재할 때
            if reverse[j][i] and to_insu[i] > to_insu[j] + reverse[j][i]:
                to_insu[i] = to_insu[j] + reverse[j][i]

    for i in range(N-1, 0, -1):
        for j in range(N-1, 0, -1):
            # 가는길이 존재할때
            if forward[j][i] and from_insu[i] > from_insu[j]+forward[j][i]:
                from_insu[i] = from_insu[j] + forward[j][i]
            # 오는 길이 존재할 때
            if reverse[j][i] and to_insu[i] > to_insu[j] + reverse[j][i]:
                to_insu[i] = to_insu[j] + reverse[j][i]
    for i in range(N):
        for j in range(N):
            # 가는길이 존재할때
            if forward[j][i] and from_insu[i] > from_insu[j]+forward[j][i]:
                from_insu[i] = from_insu[j] + forward[j][i]
            # 오는 길이 존재할 때
            if reverse[j][i] and to_insu[i] > to_insu[j] + reverse[j][i]:
                to_insu[i] = to_insu[j] + reverse[j][i]

    for i in range(N-1, 0, -1):
        for j in range(N-1, 0, -1):
            # 가는길이 존재할때
            if forward[j][i] and from_insu[i] > from_insu[j]+forward[j][i]:
                from_insu[i] = from_insu[j] + forward[j][i]
            # 오는 길이 존재할 때
            if reverse[j][i] and to_insu[i] > to_insu[j] + reverse[j][i]:
                to_insu[i] = to_insu[j] + reverse[j][i]

    r = 0
    for i in range(N):
        if r < from_insu[i]+to_insu[i]:
            r = from_insu[i]+to_insu[i]

    print("#{} {}".format(tc, r))

