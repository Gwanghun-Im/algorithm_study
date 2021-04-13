import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = float(input())
    r = ''
    for i in range(1, 13):
        if not n:
            break
        if n >= 2**(-i):
            n -= 2**(-i)
            r += '1'
        else:
            r += '0'
    if n:
        r = 'overflow'

    print("#{} {}".format(tc, r))

