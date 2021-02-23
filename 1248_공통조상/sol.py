import sys
sys.stdin = open("input.txt")


def find_root(a, b):
    a_parent = []
    b_parent = []

    temp = a
    while True:
        tp = temp.parent
        if not tp:
            break
        a_parent.append(tp)
        temp = tp

    temp = b
    while True:
        tp = temp.parent
        if not tp:
            break
        b_parent.append(tp)
        temp = tp
    for i in a_parent:
        for j in b_parent:
            if i == j:
                return i


def find_num_child(a):
    l = 0
    r = 0
    if a:
        l = find_num_child(a.left)
        r = find_num_child(a.right)
        return 1 + l + r
    return 0


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None


T = int(input())

for tc in range(1, T+1):
    v, e, a, b = map(int, input().split())
    nodes = [Node(i) for i in range(1, v+2)]
    edges = list(map(int, input().split()))

    for i in range(0, 2*e, 2):
        p = nodes[edges[i]]
        c = nodes[edges[i+1]]

        c.parent = p
        if p.left:
            p.right = c
        else:
            p.left = c

    rootab = find_root(nodes[a], nodes[b])
    fnc = find_num_child(rootab)

    print("#{} {} {}".format(tc, rootab.data-1, fnc))
