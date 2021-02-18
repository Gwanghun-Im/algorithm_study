import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    a, b = input().split()

    cnt = 0
    for i in range(len(a)-len(b)+1):
        b_in_a = True
        for j in range(len(b)):
            if a[i+j] != b[j]:
                b_in_a = False
                break
        if b_in_a == True:
            a = a[:i+j] + '#' + a[i+j+1:]
            cnt += 1

    print("#{} {}".format(tc, len(a) - (len(b) - 1) * cnt))