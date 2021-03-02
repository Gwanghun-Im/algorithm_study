import sys
sys.stdin = open("input.txt")

T = int(input())


def conquer(a, b):
    i = a
    if n_list[a-1] == 1 and n_list[b-1] == 2:
        i = b
    if n_list[a-1] == 2 and n_list[b-1] == 3:
        i = b
    if n_list[a-1] == 3 and n_list[b-1] == 1:
        i = b
    return i


def divide(start, end):
    if start == end:
        return start

    new_s = divide(start, (start+end)//2)
    new_e = divide((start+end)//2 + 1, end)
    return conquer(new_s, new_e)


for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    print("#{} {}".format(tc, divide(1, n)))

