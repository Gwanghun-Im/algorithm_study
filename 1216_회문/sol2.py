import sys
sys.stdin = open("input.txt")

T = 10


for _ in range(1, T + 1):
    tc = int(input())
    n = 100
    string = [input() for i in range(n)]
    result = []

    for y in range(n):
        for x in range(n):

            temp_str = ''
            for i in range(y, n):
                temp_str += string[i][x]
                k = True
                for i in range(len(temp_str) // 2):
                    if temp_str[i] != temp_str[-(i + 1)]:
                        k = False
                        break
                if k:
                    result += [temp_str]

            temp_str = ''
            for i in range(x, n):
                temp_str += string[y][i]
                k = True
                for i in range(len(temp_str) // 2):
                    if temp_str[i] != temp_str[-(i + 1)]:
                        k = False
                        break
                if k:
                    result += [temp_str]
    result = max(result)
    print("#{} {}".format(tc, result))