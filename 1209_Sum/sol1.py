import sys
sys.stdin = open("input.txt")

T = 10


for _ in range(1, T+1):
    tc = int(input())
    arr = []
    # 빈공간
    for i in range(100):
        arr += [list(map(int, input().split()))]

    #세로방향 합
    sum_arr =[]
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        sum_arr += [temp]

    #가로방향합
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        sum_arr += [temp]

    #대각선방향 합
    temp = 0
    for i in range(100):
        temp += arr[i][i]
    sum_arr += [temp]

    #역대각선방향 합
    temp = 0
    for i in range(100):
        temp += arr[i][99 - i]
    sum_arr += [temp]

    #합을 비교한 후 최대값산정
    max_sum = 0
    for i in sum_arr:
        if i > max_sum:
            max_sum = i


    print("#{} {}".format(tc, max_sum))

