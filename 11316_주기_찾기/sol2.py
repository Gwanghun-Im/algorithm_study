import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    s, p, q, m = map(int, input().split())
    arr = [-1] * m
    arr[s] = 0
    i = 1
    temp = s

    while True:
        temp = (temp * p + q) % m
        if arr[temp] >= 0:
            result = i - arr[temp]
            break

        arr[temp] = i
        i += 1

    print("#{} {}".format(tc, result))

