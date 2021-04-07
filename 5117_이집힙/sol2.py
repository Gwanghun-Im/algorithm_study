import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    V = int(input())
    temp = list(map(int, input().split()))
    temp.insert(0, 0)
    print(temp)
    while True:
        count = 0
        if V % 2 != 0:
            for i in range(V // 2):
                if temp[i] > temp[i * 2]:
                    temp[i], temp[i * 2] = temp[i * 2], temp[i]
                    count += 1

            for i in range(V // 2):
                if temp[i] > temp[i * 2 + 1]:
                    temp[i], temp[i * 2 + 1] = temp[i * 2 + 1], temp[i]
                    count += 1
            if count == 0:
                break

        else:
            for i in range(V // 2 + 1):
                if temp[i] > temp[i * 2]:
                    temp[i], temp[i * 2] = temp[i * 2], temp[i]
                    count += 1

            for i in range(V // 2):
                if temp[i] > temp[i * 2 + 1]:
                    temp[i], temp[i * 2 + 1] = temp[i * 2 + 1], temp[i]
                    count += 1
            if count == 0:
                break

    print(temp)
    result = 0
    while V:
        num = V // 2
        result += temp[num]
        V //= 2

    print("#{} {}".format(tc, result))