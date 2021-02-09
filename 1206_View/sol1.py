import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    N = int(input())
    building = list(map(int, input().split()))
    building_2d = [[0 for _ in range(N)] for _ in range(255)]
    cnt = 0
    for i in range(254, -1, -1):
        for j in range(N-1, -1, -1):
            if building[j] > 0:
                building_2d[i][j] += 1
                building[j] -= 1
    for i in range(255):
        for j in range(N):
            if j > 1 or j < N-1:
                if building_2d[i][j]==1:
                    if building_2d[i][j-1] == building_2d[i][j-2] == building_2d[i][j+1] == building_2d[i][j+2] == 0 :
                        cnt += 1


    print("#{} {}".format(tc, cnt))

