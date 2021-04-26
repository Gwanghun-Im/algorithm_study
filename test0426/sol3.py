import sys
sys.stdin = open("문제3_input.txt")

T = int(input())

# 크루스칼 알고리즘
# 부모를 가져오는 함수
def get_parent(x):
    if p[x] != x:
        p[x] = get_parent(p[x])
    return p[x]

# 노드를 합치는 함수
def union_parent(x, y, w):
    global r
    a = get_parent(x)
    b = get_parent(y)
    if a == b:
        return
    if a > b:
        p[a] = b
    else:
        p[b] = a
    r += w

for tc in range(1, T+1):
    V, E, M = map(int, input().split())
    roads = [list(map(int, input().split())) for _ in range(E)]
    # 도로 정렬
    roads.sort(key=lambda x:x[2])
    # 사이클이 생기지 않도록 부모를 지정
    p = [i for i in range(V+1)]

    # 도로와 건설비용을 표시
    road_weight = [[0 for _ in range(V+1)] for _ in range(V+1)]

    # 선택된 도로 건설비용
    r = 0
    for road in roads:
        n1, n2, w = road
        # 크루스칼 알고리즘
        union_parent(n1, n2, w)
        # 도로와 건설비용 추가
        road_weight[n1][n2] = w
        road_weight[n2][n1] = w

    # 만약 크루스칼 알고리즘으로 도로가 선택 되었다면
    if r <= M:
        # 결과를 출력
        result = M-r
    else:
        # 다익스트라 알고리즘
        # 모든 갈수 있는 도로를 무한대로 설정
        dis = [float('inf') for _ in range(V+1)]
        # 1번에서 1번으로 갈때는 0
        dis[1] = 0
        # i = 도착지점
        for i in range(V + 1):
            # j = 출발지점
            for j in range(i):
                # 만약 도로가 존재하고, 더 싸게 건설할 수 있을때 업데이트 시켜준다
                if road_weight[j][i] and dis[i] > dis[j] + road_weight[j][i]:
                    dis[i] = dis[j] + road_weight[j][i]
        # result에서 검사하고, 만약 이래도 건설비용이 예산보다 비싸면 -1
        result = M - dis[-1] if dis[-1] <= M else -1
    print("#{} {}".format(tc, result))

