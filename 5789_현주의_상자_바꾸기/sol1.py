import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, Q = map(int, input().split())
    result = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            result[j] = i+1

    result_str = ' '.join(map(str, result))

    print("#{} {}".format(tc, result_str))