import sys
sys.stdin = open("input.txt")

# a,b의 부모를 찾는다
def find_root(a, b):
    a_parent = []
    b_parent = []

    temp = a
    while True:
        tp = temp.parent
        # 부모가 없는 루트노드의 경우 멈춤
        if not tp:
            break
        a_parent.append(tp)
        temp = tp

    temp = b
    while True:
        tp = temp.parent
        # 부모가 없는 루트노드의 경우 멈춤
        if not tp:
            break
        b_parent.append(tp)
        temp = tp

    # a,b의 조상중의 공통 조상을 찾음
    for i in a_parent:
        for j in b_parent:
            if i == j:
                return i

# 자식노드 개수 찾는 함수
def find_num_child(a):
    l = 0
    r = 0
    if a:
        l = find_num_child(a.left)
        r = find_num_child(a.right)
        return 1 + l + r
    return 0


#클래스로 스택 자료형 표현
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


T = int(input())

for tc in range(1, T+1):
    # 간선, 노드, a, b
    v, e, a, b = map(int, input().split())
    # 먼저 노드를 클래스로 구현
    nodes = [Node(i) for i in range(1, v+2)]
    # 간선정보를 input으로 받아옴
    edges = list(map(int, input().split()))

    # 간선이 2개씩 묶어서 나오기 때문에 2*e만큼을 2칸씩 전진
    for i in range(0, 2*e, 2):
        # 부모
        p = nodes[edges[i]]
        # 자식
        c = nodes[edges[i+1]]

        # 자식과 부모 연결
        c.parent = p
        # 부모와 자식 연결
        if p.left:
            p.right = c
        else:
            p.left = c

    rootab = find_root(nodes[a], nodes[b])
    fnc = find_num_child(rootab)

    print("#{} {} {}".format(tc, rootab.data-1, fnc))
