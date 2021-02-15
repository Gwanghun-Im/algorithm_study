import sys
sys.stdin = open("input.txt")

T = int(input())

def page(p, n):
    cnt = 1
    l = 1
    temp = int((l + p) / 2)

    while temp != n:
        if temp < n:
            l = temp
        else:
            p = temp
        temp = int((l + p) / 2)
        cnt += 1

    return cnt

for tc in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    result = 0
    cnt_a = page(P, Pa)
    cnt_b = page(P, Pb)
    if cnt_a != cnt_b:
        result = 'A' if cnt_a < cnt_b else 'B'

    print("#{} {}".format(tc, result))

