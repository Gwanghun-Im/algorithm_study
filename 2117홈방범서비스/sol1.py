import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())
    city = [list(map(int, input().split())) for _ in range(n)]
    ans = 0
    for i in city:
        if sum(i):
            ans = 1
            break

    for i in range(n):
        for j in range(n):
            for k in range(n+1):
                temp = 0
                for l in range(i-k, i+k+1):
                    for o in range(j-k, j+k+1):
                        if 0 <= l < n and 0 <= o < n and abs(l-i)+abs(o-j) <= k and city[l][o]:
                            temp += 1
                if (k+1)*(k+1) + k**2 < temp * m and temp > ans:
                    ans = temp
                    print(i,j,k,temp)

    print("#{} {}".format(tc, ans))
    break