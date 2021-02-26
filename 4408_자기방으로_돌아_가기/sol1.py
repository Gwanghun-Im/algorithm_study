import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    n = int(input())

    # 복도
    hallway = [0] * 201

    # 각자 시작과 목표방
    goal = []
    for i in range(n):
        goal += [list(map(int, input().split()))]

    for temp in goal:
        temp.sort()
        # 방 번호를 하나로 묶었다.
        for i in range(2):
            if temp[i] % 2:
                temp[i] += 1
            temp[i] //= 2
        # 복도에 색칠하기
        for i in range(temp[0], temp[1] + 1):
            hallway[i] += 1

    print("#{} {}".format(tc, max(hallway)))