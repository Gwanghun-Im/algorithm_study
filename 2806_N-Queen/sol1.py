import sys
sys.stdin = open("input.txt")

T = int(input())

def chess(arr1, x, y, n):
    for i in range(n):
        for j in range(n):
            if i == x or j == y or i-x == j-y or i == n-j:
                arr1[i][j] = 1
    return arr1

def queen(arr2, n):
    cnt = 0
    temp = 0
    for k in range(n):
        temp = 0
        arr2 = chess(arr2, 0, k, n)
        temp += 1
        for i in range(1,n):
            for j in range(n):
                if arr2[i][j] == 0:
                    arr2 = chess(arr2, i, j, n)
                    temp += 1
                if temp == n:
                    cnt += 1
                    break

    return cnt


for tc in range(1, T+1):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    ans = queen(arr, n)

    print("#{} {}".format(tc, ans))

