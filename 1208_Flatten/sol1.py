import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    # 덤프 횟수
    dump = int(input())
    #상자의 높이값
    boxes = list(map(int, input().split()))
    # 상자의 가로길이는 할상 100이고 , 높이는 100 이하이므로
    # 100 x 100 크기만큼 빈 상자를 만들어 준다.
    boxes_2d = [[0 for _ in range(100)] for _ in range(100)]

    # 상자를 채워준다.
    # 2차원 공간으로 문제에 나온 그림과 같이 만들어준다.
    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            if boxes[j] > 0:
                boxes_2d[i][j] += 1
                boxes[j] -= 1

    # dump횟수만큼 반복한다.
    while dump > 0:

        # 예시)
        # boxes_2d 요소가 1 인것을 좌측 상단부터 찾는다.
        # -->[[ 0, 0, 0, 1, 0,],
        #     [ 1, 1, 0, 1, 0,],
        #     [ 1, 1, 0, 1, 0,],
        #     [ 1, 1, 1, 1, 0,],
        #     [ 1, 1, 1, 1, 1,]]<---
        #                        boxes_2d요소가 0인것을 우측하단부터 찾는다.

        brk = False
        for i in range(100):
            if brk:
                break
            for j in range(100):
                # i, j 가 1 일때
                if boxes_2d[i][j] == 1:
                    # 상자를 0으로 바꿔준다.
                    boxes_2d[i][j] = 0
                    brk = True
                    break

        brk = False
        for i in range(99,-1, -1):
            if brk:
                break
            for j in range(99, -1, -1):
                # i, j 가 0일때
                if boxes_2d[i][j] == 0:
                    # 1로 바꿔준다
                    boxes_2d[i][j] = 1
                    brk = True
                    break
        # dump 를 1회 반복할때마다 횟수를 줄여준다.
        dump -= 1

    # boxes_2d[i] 가 0 이상이면 상자가 하나라도 존재하는 최고증임을 알 수 있고
    high = 0
    for i in range(100):
        if sum(boxes_2d[i]) > 0:
            high = i
            break
    # boxes_2d[i]가 100보다 작으면 상자가 하나라도 빈 가장 낮은 층임을 알 수 있다.
    low = 0
    for i in range(99, -1, -1):
        if sum(boxes_2d[i]) < 100:
            low = i
            break
    # i가 0부터 시작해서 나오는 오차 1을 더해줌
    diff = low - high +1
    print("#{} {}".format(tc, diff))

