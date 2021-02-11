import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    boxes = list(map(int, input().split()))
    boxes_2d = [[0 for _ in range(N)] for _ in range(N)]

    #상자를 2d 로 바꿔준다
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            if boxes[j] > 0:
                boxes_2d[i][j] += 1
                boxes[j] -= 1

    # 최대낙차를 저장
    result = 0
    #현재 낙차를 저장
    temp = 0
    for i in range(N):
        for j in range(N):
            temp = 0
            if boxes_2d[i][j] == 1:
                for v in range(j, N):
                    if boxes_2d[i][v] == 0:
                        temp += 1
            if result < temp :
                result = temp


    print("#{} {}".format(tc, result))

