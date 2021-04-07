import sys
sys.stdin = open("input.txt")

T = int(input())


def find_num_child(a):
    l = 0
    r = 0
    if a:
        l = find_num_child(a.left)
        r = find_num_child(a.right)
        return 1 + l + r
    return 0

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

for tc in range(1, T+1):
    e, n = map(int, input().split())
    edges = list(map(int, input().split()))
    nodes = [Node(i) for i in range(e+2)]

    for i in range(0, 2*e, 2):
        p = nodes[edges[i]]
        c = nodes[edges[i+1]]

        c.parent = p
        if p.left:
            p.right = c
        else:
            p.left = c

    fnc = find_num_child(nodes[n])

    print("#{} {}".format(tc, fnc))

