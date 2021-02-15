import sys
sys.stdin = open("input.txt")

T = int(input())
A = [i for i in range(1, 13)]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    cnt = 0
    for i in range(1 << 12):
        temp = []
        for j in range(12):
            if len(temp) > N:
                break
            if i & (1 << j):
                temp += [A[j]]
        if sum(temp) == K and len(temp) == N:
            cnt += 1

    print("#{} {}".format(tc, cnt))