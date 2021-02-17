import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    n = int(input())

    # 사다리를 저.장.
    arr = []
    for i in range(100):
        # 양옆에 -1을 준다 _인덱스에러 방지
        arr.append([-1, *list(map(int, input().split())), -1])

    # 맨 아래 존재하는 2의 위치를 찾는다.
    for i in range(101):
        if arr[99][i] == 2:
            row = i

    # 맨아래 깊이부터 차근차근 위로 올라가서 탐색한다.
    depth = 99
    while depth > 0:

        # 만약 오른쪽에 사다리가 있으면?
        if arr[depth][row+1] == 1 :
            # 사다리가 안나올때까지 반복하고
            while arr[depth][row+1] == 1:
                row += 1
            # 안 나오면 위로 전진한다.
            depth -= 1
            continue

        # 왼쪽의 경우
        if arr[depth][row-1] == 1 :
            while arr[depth][row-1] == 1:
                row -= 1
            depth -= 1
            continue

        # 위로 전.진.
        depth -= 1


    print("#{} {}".format(n, row-1))

