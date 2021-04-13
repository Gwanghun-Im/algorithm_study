T = int(input())

# 4방향을 표시하기 위한 deltaX, deltaY
dy = [-1, -1, 1, 1]
dx = [-1, 1, 1, -1]


for tc in range(1, T+1):
    # 지도의크기, 폭탄의 개수
    n, m = map(int, input().split())
    # 지도를 받아옴
    my_map = [list(map(int, input().split())) for _ in range(n)]
    # 폭탄 정보를 받아옴
    bomb = [list(map(int, input().split())) for _ in range(m)]

    # 적군 패해 인원을 중복으로 받아오면 안되기 때문에 visited를 사용
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 총 피해인원 기록
    r = 0

    # 폭탄의 개수만큼 반복
    for b in bomb:
        # y축, x축, power
        y, x, p = b
        # (y, x)에 있는 인구수만큼 r에 추가
        r += my_map[y][x]
        # 방문표시
        visited[y][x] = 1

        # power의 크기만큼 대각선으로 퍼진다.
        for i in range(1, p+1):
            # 4방향으로 퍼진다
            for j in range(4):
                # 파워크기를 deltaX와 deltaY에 곱하고 x, y에 더한다.
                temp_y = y+dy[j]*i
                temp_x = x+dx[j]*i
                # 지도의 크기를 벗어나는지 확인하고
                if 0 <= temp_y < n and 0 <= temp_x < n:
                    # 만약 방문을하지 않았다면
                    if not visited[temp_y][temp_x]:
                        # 맵에 있는 인구수를 더한다.
                        r += my_map[temp_y][temp_x]

                    # 방문표시를 해준다.
                    visited[temp_y][temp_x] = 1

    print("#{} {}".format(tc, r))

