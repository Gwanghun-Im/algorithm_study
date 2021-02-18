import sys
sys.stdin = open("input.txt")

T = int(input())

def is_abba(n, string):
    for i in range(n//2):
        if string[i] != string[-(i+1)]:
            return 0
    return 1



for tc in range(1, T+1):
    n, m = map(int, input().split())
    string = [input() for i in range(n)]
    result = ''

    for y in range(n):
        for x in range(n):
            temp_str = ''
            if n-y >= m:
                for i in range(y, n):
                    temp_str += string[i][x]
                result += temp_str if is_abba(m, temp_str) else ''
            temp_str = ''
            if n-x >= m:
                for i in range(x, n):
                    temp_str += string[y][i]
                result += temp_str if is_abba(m, temp_str) else ''
        if result:
            break

    print("#{} {}".format(tc, result))

