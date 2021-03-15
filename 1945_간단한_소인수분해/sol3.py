import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    number = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while number != 1:
        if number % 2 == 0:
            number = number // 2
            a += 1
        if number % 3 == 0:
            number = number // 3
            b += 1
        if number % 5 == 0:
            number = number // 5
            c += 1
        if number % 7 == 0:
            number = number // 7
            d += 1
        if number % 11 == 0:
            number = number // 11
            e += 1



    
    print("#{} {} {} {} {} {}".format(tc, a, b, c, d, e))

