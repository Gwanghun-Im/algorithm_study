import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    s, p, q, m = map(int, input().split())

    new_num = {s:0}
    arr = [s]
    i = 0

    while True:
        arr += [(p*arr[i] + q) % m]
        i += 1

        if arr[i] in new_num.keys():
            result = i - new_num[arr[i]]
            break
        new_num[arr[i]] = i
    print("#{} {}".format(tc, result))

