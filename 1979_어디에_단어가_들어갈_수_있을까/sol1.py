import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, k = map(int, input().split())
    arr = []
    for _ in range(n):
        arr += [list(map(int, input().split()))]

    cnt = 0
    # 2차원 배열 탐색
    for i in range(n):
        # 행으로 세기
        temp1 = 0
        # 열로 세기
        temp2 = 0
        for j in range(n):
            #0 을 만나면 채워질 수 없는 칸이기에
            # 지금까지 더해온것을 확인한다
            if arr[i][j] == 0:
                # 만약 길이가 k 와 같다면 1더하고 아니면 0을 더해서 그대로 놔둔다.
                cnt += 1 if temp1 == k else 0
                # 그리고 다시 0으로 초기화 해 준다.
                temp1 = 0
            elif arr[i][j] == 1:
                temp1 += 1


            # 열 방향
            if arr[j][i] == 0:
                cnt += 1 if temp2 == k else 0
                temp2 = 0
            elif arr[j][i] == 1:
                temp2 += 1

        # 한 줄이 끝나면
        # 지금까지 더해온것을 확인하고
        # 만약 길이가 k 와 같다면 1더하고 아니면 0을 더해서 그대로 놔둔다.
        cnt += 1 if temp1 == k else 0
        cnt += 1 if temp2 == k else 0

    print("#{} {}".format(tc, cnt))

