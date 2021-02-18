import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    str1 = input()
    n = len(str1)
    str2 = input()
    m = len(str2)

    result = 0
    for i in range(m - n + 1):
        temp = 0
        for j in range(n):
            if str1[j] == str2[i+j]:
                if j == n - 1:
                    result = 1
                continue
            break
        if result == 1:
            break

    print("#{} {}".format(tc, result))