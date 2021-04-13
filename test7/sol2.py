T = int(input())

# 자손을 세어주는 함수
def find(n):
    global cnt
    # 만약 자식이 있는경우
    if child[n]:
        # 자식의 숫자만큼 함수를 재귀로 실행
        for i in child[n]:
            find(i)
            # 한번 실행할 때마다. 결과에 1을 추가
            cnt += 1
    # 자식이 없으면 함수는 실행되지 않는다.

for tc in range(1, T+1):
    # 노드개수, 노드번호
    V, N = map(int, input().split())
    # 자손이 누구누구인지 알 수 있게 해주는 빈 리스트 생성
    child = [[] for _ in range(V+1)]
    # 간선정보
    edges = list(map(int, input().split()))
    # 간선의 길이만큼 2칸씩 전진한다.
    for i in range(0, len(edges), 2):
        # child의 부모 인덱스에 자식을 추가
        child[edges[i]].append(edges[i+1])
    # 결과를 담을 변수
    cnt = 0
    # 함수실행
    find(N)

    print("#{} {}".format(tc, cnt))

