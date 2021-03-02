import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    # 오셀로 만들기
    othello = [[0]*n for _ in range(n)]
    # 오셀로 초기 값
    othello[n//2 - 1][n//2 - 1], othello[n//2][n//2] = 2, 2
    othello[n//2][n//2 - 1], othello[n//2 - 1][n//2] = 1, 1
    # 12시부터 시계방항으로 만듦
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]

    # 말을 놓는 횟수만큼
    for i in range(m):
        # 좌표(x, y) 그리고 컬러 (c)
        x, y, c = map(int, input().split())
        # 오셀로 좌표가 1,1 ㅂ무터 시작하기에 -1씩 해준다.
        y -= 1
        x -= 1
        # 일단 거기에 컬러를 넣어줌
        othello[y][x] = c
        # 8방향 탐색
        for j in range(8):
            temp_x = x + dx[j]
            temp_y = y + dy[j]
            box = []
            # 만약 그쪽 방향으로 탐색할때 나와 다른 색인 경우
            while 0 <= temp_y < n and 0 <= temp_x < n and othello[temp_y][temp_x] and othello[temp_y][temp_x] != c:
                # 일단 box에 좌표를 추가
                box.append((temp_y, temp_x))
                # 한칸 더 전진
                temp_y += dy[j]
                temp_x += dx[j]
                # 어 나와 색이 같아? 그러면
                if 0 <= temp_y < n and 0 <= temp_x < n and othello[temp_y][temp_x] and othello[temp_y][temp_x] == c:
                    # 박스 안에 저장했던거 전부 바꿔버려
                    for b in box:
                        othello[b[0]][b[1]] = c
                    break

    # 갯수를 세자
    black = 0
    white = 0
    for i in range(n):
        for j in range(n):
            if othello[i][j] == 1:
                black += 1
            elif othello[i][j] == 2:
                white += 1
    print('#{} {} {}'.format(tc+1, black, white))
