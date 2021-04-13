import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())
    new_m = ''
    while m :
        new_m = str(m%2) + new_m
        m //= 2

    if len(new_m) < n:
        new_m = '0'*(n-len(new_m)) + new_m

    r = 'OFF' if '0' in new_m[-1:-(n+1):-1] else 'ON'

    print("#{} {}".format(tc, r))

