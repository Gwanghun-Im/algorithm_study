import sys
sys.stdin = open("input.txt")

T = 10


def order(node):
    if node.data == '+':
        node.data = order(nodes[node.left]) + order(nodes[node.right])
    elif node.data == '-':
        node.data = order(nodes[node.left]) - order(nodes[node.right])
    elif node.data == '*':
        node.data = order(nodes[node.left]) * order(nodes[node.right])
    elif node.data == '/':
        node.data = order(nodes[node.left]) / order(nodes[node.right])

    return int(node.data)


class Node:
    def __init__(self, idx, data, left=0, right=0):
        self.idx = idx
        self.data = data
        self.left = int(left)
        self.right = int(right)


for tc in range(1, T+1):
    n = int(input())
    nodes = [0]
    for i in range(n):
        nodes.append(Node(*input().split()))
    print("#{} {}".format(tc, order(nodes[1])))

