import sys
sys.stdin = open("input.txt")

T = 10


for _ in range(1, T+1):
    tc = int(input())
    arr = []
    for i in range(100):
        arr += [list(map(int, input().split()))]

    sum_arr =[]
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[i][j]
        sum_arr += [temp]

    for i in range(100):
        temp = 0
        for j in range(100):
            temp += arr[j][i]
        sum_arr += [temp]

    temp = 0
    for i in range(100):
        temp += arr[i][i]
    sum_arr += [temp]

    temp = 0
    for i in range(100):
        temp += arr[i][99 - i]
    sum_arr += [temp]

    max_sum = 0
    for i in sum_arr:
        if i > max_sum:
            max_sum = i


    print("#{} {}".format(tc, max_sum))

