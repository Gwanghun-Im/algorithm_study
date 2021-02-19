import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    uisuk = [input() for i in range(5)]

    result = ''
    for i in range(15):
        for j in range(5):
            try:
                result += uisuk[j][i]
            except:
                continue

    print("#{} {}".format(tc, result))

