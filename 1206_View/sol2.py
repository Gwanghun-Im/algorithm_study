import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))
    result = 0

    for i in range(2, N-2):
        high_around = 0
        for j in range(i-2, i+3):
            if i == j:
                continue
            if building[j] > high_around:
                high_around = building[j]

        if building[i] > high_around:
            result += (building[i] - high_around)

    print("#{} {}".format(tc, result))

