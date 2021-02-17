import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())

    room = [0]*201

    goal = []
    for i in range(n):
        goal += [list(map(int, input().split()))]

    for temp in goal:
        temp.sort()
        for i in range(2):
            if temp[i] % 2:
                temp[i] += 1
            temp[i] //= 2
        for i in range(temp[0], temp[1]+1):
            room[i] += 1

    print("#{} {}".format(tc, max(room)))

