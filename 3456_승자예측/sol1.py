import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    x = 1
    k = 1
    winner = ['Alice', 'Bob']

    while n > 9:
        n = n / 2 + k
        k = -k

    if n == 1 or 6 <= n <= 9:
        i = 1
    else:
        i = 0

    if int(n) == n:
        print('ㅇㅇ')
        pass

    # else:
    #     if i: i = 0
    #     else: i = 1

    print("#{} {}".format(tc, winner[i]))

