import sys
sys.stdin = open("input.txt")

T = int(input())
A = [i for i in range(1, 13)]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    # 경우의 수를 세어준다.
    cnt = 0
    for i in range(1 << 12):
        # 부분집합을 담을 temp 형성
        temp = []
        for j in range(12):
            # temp의 길이가 N보다 크면 더 계산할 필요가 없다.
            if len(temp) > N:
                break
            if i & (1 << j):
                temp += [A[j]]
        #부분집합에 있는 값을 더해준다.
        temp_sum = 0
        for tmp in temp:
            temp_sum += tmp
        # 부분집합의 합이 K여야 하고, 길이가 N일때 경우의 수에 추가.
        if temp_sum == K and len(temp) == N:
            cnt += 1

    print("#{} {}".format(tc, cnt))