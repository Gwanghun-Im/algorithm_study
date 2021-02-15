import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    palette = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    cnt = 0

    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                palette[i][j] += color

    for i in range(len(palette)):
        for j in range(len(palette[0])):
            if palette[i][j] == 3:
                cnt += 1


    print("#{} {}".format(tc, cnt))

