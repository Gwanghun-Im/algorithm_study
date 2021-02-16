import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    T = int(input())

    for tc in range(1, T + 1):
        N = int(input())
        arr = list(map(int, input().split()))
        sign = ['>', '<']
        for i in range(len(arr) - 1):
            temp = i
            for j in range(i + 1, len(arr)):
                exec('if arr[j] {} arr[temp] : temp = j'.format(sign[i % 2]))

            arr[i], arr[temp] = arr[temp], arr[i]

        print("#{} {}".format(tc, arr))
    print("#{} ".format(tc, ))

