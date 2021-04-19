import sys
sys.stdin = open("sample_input.txt")

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())
    a = sorted(list(map(int, input().split())))
    b = list(map(int, input().split()))
    cnt = 0
    for i in b:
        left = 0
        right = n-1

        f = 0
        while left <= right:
            mid = (left+right)//2
            if i == a[mid]:
                cnt += 1
                break
            elif i > a[mid]:
                left = mid+1
                if f == 1: break
                f = 1

            else:
                right = mid-1
                if f == -1: break
                f = -1
    print("#{} {}".format(tc, cnt))

