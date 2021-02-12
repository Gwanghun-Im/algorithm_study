import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))

    my_min = 0
    my_max = 0
    for i in range(len(A)):
        if i == 0 :
            my_max = A[i]
            my_min = A[i]
            continue
        if my_max < A[i]:
            my_max = A[i]
        if my_min > A[i]:
            my_min = A[i]
    result = my_max - my_min

    print("#{} {}".format(tc, result))

