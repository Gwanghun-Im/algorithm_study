import sys
sys.stdin = open("input.txt")

T = int(input())


def is_sdoku(arr):
    # 사각형 체크
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            # 숫자가 있는지 체크
            visit = [0]*10
            for y in range(3):
                for x in range(3):
                    if visit[arr[i+y][j+x]]:
                        return 0
                    else:
                        visit[arr[i + y][j + x]] = 1
    # 행으로 체크
    for i in range(9):
        visit = [0]*10
        for j in range(9):
            if visit[arr[i][j]]:
                return 0
            else:
                visit[arr[i][j]] = 1
    # 열로 체크
    for i in range(9):
        visit = [0] * 10
        for j in range(9):
            if visit[arr[j][i]]:
                return 0
            else:
                visit[arr[j][i]] = 1
    return 1


for tc in range(1, T+1):
    puzzle = [list(map(int, input().split())) for _ in range(9)]


    print("#{} {}".format(tc, is_sdoku(puzzle)))

