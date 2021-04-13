import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    stadium = [list(map(int, input().split())) for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if stadium[i][j] == 2:
                robot = [i, j]
            if stadium[i][j] == 3:
                red = [i, j]
            if stadium[i][j] == 4:
                green = [i, j]
            if stadium[i][j] == 5:
                blue = [i, j]
    while red or green or blue:
        red_dis = abs(robot[0]-red[0]) + abs(robot[1]-red[1]) if red else 1000000
        green_dis = abs(robot[0]-green[0]) + abs(robot[1]-green[1]) if green else 1000000
        blue_dis = abs(robot[0]-blue[0]) + abs(robot[1]-blue[1]) if blue else 1000000


    print("#{} ".format(tc, ))

