import sys
sys.stdin = open("input.txt")

T = int(input())


class Node:
    def __init__(self, data, footprint):
        self.data = data
        self.footprint = footprint


for tc in range(1, T+1):
    n = int(input())//10

    stack = [Node(0,1)]
    cnt = 0

    while stack:
        now = stack.pop()

        if now.data+1 <= n:
            temp = Node(now.data+1,now.footprint*1)
            stack.append(temp)
            if temp.data == n:
                cnt += temp.footprint

        if now.data+2 <= n:
            temp = Node(now.data+2,now.footprint*2)
            stack.append(temp)
            if temp.data == n:
                cnt += temp.footprint

    print("#{} {}".format(tc, cnt))

