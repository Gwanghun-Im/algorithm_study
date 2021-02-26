import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    values = []
    for i in range(n):
        values.append(list(map(int, list(input()))))

    new_values = 0
    for i in range(n//2):
        for j in range(n//2):
            if i+j < n//2:
                values[i][j] = 0
                values[-(i+1)][j] = 0
                values[i][-(j+1)] = 0
                values[-(i+1)][-(j + 1)] = 0
    for i in values:
        for j in i:
            new_values += j
    print("#{} {}".format(tc, new_values))

