import sys
sys.stdin = open("input.txt")

T = int(input())

dy = [0, 1, 0, -1]
dx = [-1, 0, 1, 0]


def bfs(n):
    # 큐가 없으면 만나지 못하고 끝난거다
    if not queue:
        # 그냥 리턴해서 실행시키지 말아라
        return
    global ans, flag, n_
    # 한번 실행하면 한칸을 전진한거라 생각
    ans += 1
    # 이번에 큐에 추가된횟수
    temp_n = 0
    # 이 전에 큐에 추가된 횟수만큼 반복
    for _ in range(n):
        now = queue.pop(0)
        y = now[0]
        x = now[1]
        visited[y][x] = True
        for i in range(4):
            temp_y = y + dy[i]
            temp_x = x + dx[i]
            if 0 <= temp_x < n_ and 0 <= temp_y < n_:
                if not visited[temp_y][temp_x] and (maze[temp_y][temp_x] == 0):
                    queue.append([temp_y, temp_x])
                    temp_n += 1
                elif maze[temp_y][temp_x] == 3:
                    flag = 1
    # 아직 목표지점을 못만났어? -> 그럼 한번더!
    if not flag:
        # 큐에 추가된만큼
        bfs(temp_n)


for tc in range(1, T+1):
    # 미로의 크기
    n_ = int(input())
    # 미로 만들기
    maze = [list(map(int, list(input()))) for _ in range(n_)]
    visited = [[False] * n_ for _ in range(n_)]
    # 출발 지점을 스택에 저장
    for i in range(n_):
        for j in range(n_):
            if maze[i][j] == 2:
                queue = [[i, j]]
    # 목표지점에 도달했는지 여부
    flag = 0
    # 몇번 전진했는지?
    ans = 0
    # 스택의 길이만큼 bfs 실행
    bfs(1)
    # 목표에 도달했으면 -1 한 후 출력, 아니면 0
    ans = 0 if not flag else ans-1
    print("#{} {}".format(tc, ans))

