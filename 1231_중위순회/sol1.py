import sys
sys.stdin = open("input.txt")

# 중위순회
def in_order(idx):
    global result
    # 자식이 둘 다 있는 경우
    if len(nodes[idx])==2:
        in_order(nodes[idx][0])
        # 값을 뽑아옴
        result += node_v[idx]
        in_order(nodes[idx][1])
    # 자식노드가 하나인 경우
    elif len(nodes[idx])==1:
        # 자식 하나만 체크
        in_order(nodes[idx][0])
        # 값을 뽑아옴
        result += node_v[idx]
    # 자식노드가 없는경우
    else:
        # 값을 뽑아옴
        result += node_v[idx]


T = 10

for tc in range(1, T+1):
    n = int(input())
    # 자식노드만 저장할 곳 ,0번인덱스는 값이 없기때문에 0으로 초기화
    nodes = [0]
    # 값만 저장할 곳 , 0번인덱스는 값이 없기때문에 0으로 초기화
    node_v = [0]

    for i in range(n):
        temp = list(input().split())
        # 값만 append
        node_v.append(temp.pop(1))
        # 자식노드만 append
        nodes.append(list(map(int, temp[1:])))

    #결과를 담아줄 곳
    result = ''
    in_order(1)
    print("#{} {}".format(tc, result))

