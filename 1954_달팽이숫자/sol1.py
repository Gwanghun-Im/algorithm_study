import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 정사각형의 크기
    n = int(input())

    # 정사각형 크기의 2차원 배열을 만들어준다
    arr = [[0 for _ in range(n)] for _ in range(n)]

    # x, y 인덱스 값
    x, y = 0, 0

    #    ▶
    #    1 0 0 0 1 ▼
    #    0 0 0 0 0
    #    0 0 0 0 0
    #    0 0 0 0 0
    #  ▲1 0 0 0 1
    #            ◀
    # 각 모서리의 좌표 , 모서리를 만날때 마다 x, y 방향의 delta가 바뀐다.
    left_top = [0, 0]
    right_top = [0, n-1]
    left_bottom = [n-1, 0]
    right_bottom = [n-1, n-1]

    # 값은 n의 제곱만큽 들어간다.
    for i in range(1, n**2 + 1):

        # 인덱스에 값을 삽입
        arr[y][x] = i

        #만약 왼쪽상단 모서리일 경우
        if [y, x] == left_top :
            # delta x를 1만큼 증가
            dx = 1
            dy = 0

        #만약 오른쪽상단 모서리일 경우
        elif [y, x] == right_top :
            # delta y을 1만큼 증가
            dx = 0
            dy = 1

        #만약 오른쪽하단 모서리일 경우
        elif [y, x] == right_bottom :
            # delta x를 1만큼 감소
            dx = -1
            dy = 0

        # 만약 왼쪽하단 모서리일 경우
        elif [y, x] == left_bottom:
            # delta y을 1만큼 감소
            dx = 0
            dy = -1

            # 각 좌표를 업데이트 한다.
            # 좌측상단모서리의 좌표는 현재 좌측하단모서리의 행과 일치시키고 난 후에
            # 좌측하단 모서리의 값을 엡데이트 하는게 핵심
            left_top = [left_top[0]+1, left_bottom[1]]
            right_top = [right_top[0]+1, right_top[1]-1]
            right_bottom = [right_bottom[0]-1, right_bottom[1]-1]
            left_bottom = [left_bottom[0]-1, left_bottom[1] + 1]

        # x, y 인덱스를 delta만큼 업데이트 시켜준다.
        y += dy
        x += dx

    print("#{}".format(tc))
    for i in arr:
        print(*i)

import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 정사각형의 크기
    n = int(input())

    # 정사각형 크기의 2차원 배열을 만들어준다
    arr = [[0 for _ in range(n)] for _ in range(n)]

    # x, y 인덱스 값
    x, y = 0, 0

    #    ▶
    #    1 0 0 0 1 ▼
    #    0 0 0 0 0
    #    0 0 0 0 0
    #    0 0 0 0 0
    #  ▲1 0 0 0 1
    #            ◀
    # 각 모서리의 좌표 , 모서리를 만날때 마다 x, y 방향의 delta가 바뀐다.
    left_top = [0, 0]
    right_top = [0, n-1]
    left_bottom = [n-1, 0]
    right_bottom = [n-1, n-1]

    # 값은 n의 제곱만큽 들어간다.
    for i in range(1, n**2 + 1):

        # 인덱스에 값을 삽입
        arr[y][x] = i

        #만약 왼쪽상단 모서리일 경우
        if [y, x] == left_top :
            # delta x를 1만큼 증가
            dx = 1
            dy = 0

        #만약 오른쪽상단 모서리일 경우
        elif [y, x] == right_top :
            # delta y을 1만큼 증가
            dx = 0
            dy = 1

        #만약 오른쪽하단 모서리일 경우
        elif [y, x] == right_bottom :
            # delta x를 1만큼 감소
            dx = -1
            dy = 0

        # 만약 왼쪽하단 모서리일 경우
        elif [y, x] == left_bottom:
            # delta y을 1만큼 감소
            dx = 0
            dy = -1

            # 각 좌표를 업데이트 한다.
            # 좌측상단모서리의 좌표는 현재 좌측하단모서리의 행과 일치시키고 난 후에
            # 좌측하단 모서리의 값을 엡데이트 하는게 핵심
            left_top = [left_top[0]+1, left_bottom[1]]
            right_top = [right_top[0]+1, right_top[1]-1]
            right_bottom = [right_bottom[0]-1, right_bottom[1]-1]
            left_bottom = [left_bottom[0]-1, left_bottom[1] + 1]

        # x, y 인덱스를 delta만큼 업데이트 시켜준다.
        y += dy
        x += dx

    print("#{}".format(tc))
    for i in arr:
        print(*i)

