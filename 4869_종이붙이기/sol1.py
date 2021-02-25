import sys
sys.stdin = open("input.txt")

T = int(input())

# 노드(트리를 만듦)
class Node:
    def __init__(self, data, footprint):
        # 세로 길이
        self.data = data
        # 경우의 수
        self.footprint = footprint


for tc in range(1, T+1):
    # 보기 편하려고 10으로 나눔
    n = int(input())//10

    # 가장 처음 노드를 만든다
    # 길이는 0, 경우의 수는 아무것도 없는 상태이기 때문에 1
    stack = [Node(0,1)]
    # 길이가 n인 것의 개수를 센다
    cnt = 0

    # 스택에 존재할때
    while stack:
        # 스택에서 꺼내오고
        now = stack.pop()

        # 스택에 있는 길이에 1을 더할때 n보다 작으면
        if now.data+1 <= n:
            #노드를 만들고
            # 길이가 1인것을 추가하면 경우의 수는 그대로이다
            temp = Node(now.data+1,now.footprint*1)
            # 스택에 저장한다.
            stack.append(temp)
            # 만든 노드가 n과 같으면 cnt변수에 추가
            if temp.data == n:
                cnt += temp.footprint

        # 스택에 있는 길이에 2를 더할 경우
        if now.data+2 <= n:
            # 길이가 2인것을 더하면 경우의 수는 2배가 된다
            # (정사각형 하나를 놓거나, 2개의 직사각형을 세로로 놓는다)
            temp = Node(now.data+2,now.footprint*2)
            stack.append(temp)
            if temp.data == n:
                cnt += temp.footprint

    print("#{} {}".format(tc, cnt))

