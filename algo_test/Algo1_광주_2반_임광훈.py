import sys
sys.stdin = open("1번_input.txt")

T = int(input())


for tc in range(1, T+1):
    # n, m 을 입력
    n, m = map(int ,input().split())

    # 정원에 들어갈 나무의 가격을 알려주는 trees
    trees = []
    for i in range(n):
        trees += [list(map(int, input().split()))]

    # 정원에 실제로 들어갈 나무만 보여주는 garden
    # 크기는 n x m 으로 만든다.
    garden = [[0]*m for _ in range(n)]

    #나무를 심는 총 비용
    cost = 0
    # 심은 나무의 수
    cnt_tree = 0
    # 가장 비싼 나무의 가격
    max_cost = 0
    # 가장비싼 나무가 심어진 열
    max_col = 0

    # 정원의 행길이 n 만큼 반복
    for i in range(n):
        # 정원의 열크기 m 만큼 반복
        for j in range(m):
            # 만약 정원이 홀수번때 행이라면 나무는 저장되지 않고 아래 코드는 실행되지 않는다.
            if j % 2:
                continue
            # 정원에 나무 심기
            garden[i][j] = trees[i][j]
            # 심은 나무의 가격을 비용에 업데이트
            cost += trees[i][j]
            # 나무개수를 세어준다.
            cnt_tree += 1
            # 이 전까지 가장 비싼 나무와 현재 심은 나무를 비교해서,
            # 현재 나무가 더 크다면
            if max_cost <= trees[i][j]:
                # 가장 비싼 나무의 가격을 업데이트 한다.
                max_cost = trees[i][j]
                # 가장 비싼 나무의 열을 저장하고
                # +1을 해준다, (배열이 0부터 시작하기 때문에)
                max_col = j + 1


    print("#{} {} {} {} {}".format(tc, cost, cnt_tree, max_cost, max_col))

