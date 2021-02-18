import sys
sys.stdin = open("input.txt")

T = 10


def is_abba(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return 0
    return len(string)


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
                if is_abba(temp_str):
                    result += [is_abba(temp_str)]

            temp_str = ''
            for i in range(x, n):
                temp_str += string[y][i]
                if is_abba(temp_str):
                    result += [is_abba(temp_str)]

    result = max(result)
    print("#{} {}".format(tc, result))