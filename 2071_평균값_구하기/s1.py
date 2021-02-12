import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    X = list(map(int, input().split()))
    my_sum = 0
    my_len = 0
    for x in X:
        my_sum += x
        my_len += 1
    result = round(my_sum / my_len)
    print( '#{} {}'.format(tc, result))