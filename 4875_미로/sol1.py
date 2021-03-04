import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    # 미로 만들기
    maze = [list(map(int, list(input()))) for _ in range(n)]
    # 방문여부 확인
    visited = [[False]*n for _ in range(n)]
    dy = [0, 1, 0, -1]
    dx = [-1, 0, 1, 0]
    stack = []
    # 출발 지점을 스택에 저장
    for i in range(n):
        for j in range(n):
            if maze[i][j]==2:
                stack.append((i,j))
    # 도착지점에 도달했는지 체크하기 위한 변수
    flag = 0
    # 스택에 있을때 꼐속 실행
    while stack:
        # 스택을 pop하고
        now = stack.pop()
        # 방문했다.
        visited[now[0]][now[1]] = True
        y = now[0]
        x = now[1]
        # 4방향 탐색
        for i in range(4):
            # 4방향 만큼 임시 x,y를 만들고
            temp_x = x + dx[i]
            temp_y = y + dy[i]
            # 인덱스에러방지
            if 0 <= temp_x < n and 0 <= temp_y < n:
                # 만약 방문하지않았고, 진행할 수 (0)있을때
                if (visited[temp_y][temp_x] == False) and (maze[temp_y][temp_x] == 0):
                    # 스택에 추가
                    stack.append((temp_y, temp_x))
                # 만약 방문하지 않았고, 도착지점(3)일때
                elif (visited[temp_y][temp_x] == False) and (maze[temp_y][temp_x] == 3):
                    # flag로 도착여부 체크
                    flag = 1
    print("#{} {}".format(tc, flag))

