import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())

    ab_list = []
    for _ in range(N):
        ab_list.append(list(map(int, input().split())))

    P = int(input())
    C_list = []
    for _ in range(P):
        C_list.append(int(input()))

    new_C_list = [0]*5001

    for ab in ab_list:
        for i in range(ab[0], ab[1]+1):
            new_C_list[i] += 1

    result_str = ''
    for i in C_list:
        result_str += ' {}'.format(new_C_list[i])

    print("#{}{}".format(tc, result_str))