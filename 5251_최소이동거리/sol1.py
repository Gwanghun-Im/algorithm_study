import sys
sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T+1):
    n, e = map(int, input().split())
    arr = [[0 for _ in range(n+1)] for _ in range(n+1)]
    dis = [float('inf')] * (n+1)
    dis[0] = 0
    for i in range(e):
        a, b, w = map(int, input().split())
        arr[a][b] = w
    for i in range(n+1):
        for j in range(i):
            if arr[j][i] and dis[i] > dis[j]+arr[j][i]:
                dis[i] = dis[j]+arr[j][i]
    print(dis)
    print("#{} {}".format(tc, dis[-1]))

