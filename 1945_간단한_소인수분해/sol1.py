import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    result = [0, 0, 0, 0, 0]
    while N != 1:
        if N//2 == N/2 :
            result[0] += 1
            N = N//2
        if N//3 == N/3 :
            result[1] += 1
            N = N//3
        if N//5 == N/5 :
            result[2] += 1
            N = N//5
        if N//7 == N/7 :
            result[3] += 1
            N = N//7
        if N//11 == N/11 :
            result[4] += 1
            N = N//11

    result_str = ''
    for i in result:
        result_str += ' {}'.format(i)


    print("#{}{}".format(tc, result_str))

