import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    for i in range(len(arr) - 1):
        temp = i
        for j in range(i + 1, len(arr)):
            if i%2:
                if arr[j] < arr[temp] : temp = j
                continue
            if arr[j] > arr[temp]: temp = j
        arr[i], arr[temp] = arr[temp], arr[i]

    result = ' '.join(map(str,arr[:10]))
    print("#{} {}".format(tc, result))

