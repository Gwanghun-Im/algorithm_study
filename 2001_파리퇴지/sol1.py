import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())

    # 파리가 들어갈 공간
    arr = []
    for _ in range(n):
        arr += [list(map(int, input().split()))]

    # 가장 많이 죽인 수
    kill_max = 0
    # n-m+1 만큼 반복
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 현재 위치에서 죽인파리를 담을 공간
            temp = 0
            # 현재위치에서 죽일수 있는 파리를 m길이만큼 더한다.
            for r in range(i, i+m):
                for c in range(j,j+m):
                    #파리를 죽인다.
                    temp += arr[r][c]
            # 만약 현재죽인 파리가 더 많다면 kill_max를 업데이트
            kill_max = temp if temp > kill_max else kill_max

    print("#{} {}".format(tc, kill_max))

