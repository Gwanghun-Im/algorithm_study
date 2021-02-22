import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    x = 1
    k = 1
    winner = ['Alice', 'Bob']

    while n > 2:
        n = n // 2 + k
        k = -k

    if n == 1:
        i = 1
    else:
        i = 0

    print("#{} {}".format(tc, winner[i]))

