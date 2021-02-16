import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr += [list(map(int, input().split()))]

    # 가로방향으로 탐색
    cnt = 0
    for i in range(n):
        temp1 = 0
        temp2 = 0
        for j in range(n):
            if arr[i][j] == 0:
                cnt += 1 if temp1 == k else 0
                temp1 = 0
            elif arr[i][j] == 1:
                temp1 += 1
            if arr[j][i] == 0:
                cnt += 1 if temp2 == k else 0
                temp2 = 0
            elif arr[j][i] == 1:
                temp2 += 1
        cnt += 1 if temp1 == k else 0
        cnt += 1 if temp2 == k else 0

    print("#{} {}".format(tc, cnt))

