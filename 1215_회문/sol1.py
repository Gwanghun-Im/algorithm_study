import sys
sys.stdin = open("input.txt")

T = 10

def is_abba(string):
    for i in range(len(string) // 2):
        if string[i] != string[-(i + 1)]:
            return 0
    return len(string)

for tc in range(1, T+1):
    n = 8
    m = int(input())
    string = [input() for i in range(n)]
    result = 0

    for y in range(n):
        for x in range(n):
            if n-y >= m :
                temp_str = ''
                for i in range(y, y+m):
                    temp_str += string[i][x]
                if is_abba(temp_str):
                    result += 1
            if n-x >= m :
                temp_str = ''
                for i in range(x, x+m):
                    temp_str += string[y][i]
                if is_abba(temp_str):
                    result += 1

    print("#{} {}".format(tc, result))

