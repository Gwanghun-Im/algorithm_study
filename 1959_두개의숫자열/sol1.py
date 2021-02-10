import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    if N > M :
        N, M = M, N
        a, b = b, a

    max_ = 0
    for i in range(M - N + 1):
        temp = 0
        for j in range(N):
            temp += a[j] * b[i+j]
        if temp > max_:
            max_ = temp


    print("#{} {}".format(tc, max_))

