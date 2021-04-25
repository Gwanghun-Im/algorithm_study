import sys
sys.stdin = open("input.txt")

T = int(input())


def dfs(num, mysum):
    global r

    if mysum > r:
        return
        
    if num == n-1:
        r = mysum
        return
    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(num+1, mysum + matrix[num+1][i])
            visited[i] = 0

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    # 각 열마다 1개씩 선택될 것을 방문체크
    visited = [0] * n
    r = float('inf')


    for i in range(n):
        # 일단 열을 방문체크
        visited[i] = 1
        dfs(0, matrix[0][i])
        visited[i] = 0
    
    print("#{} {}".format(tc, r))

