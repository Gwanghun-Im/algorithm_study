import sys
sys.stdin = open("input.txt")


def pre_order(node):
    if node:
        print('{}'.format(node),end=' ')
        pre_order(tree[node][0])
        pre_order(tree[node][1])


v = int(input())
line = list(map(int, input().split()))

tree = [[0, 0, 0] for _ in range(v+1)]
visited = [[] for _ in range(v+1)]

for i in range(0, len(line),2):
    parent, child = line[i], line[i+1]

    if tree[parent][0]:
        tree[parent][1] = child
    else:
        tree[parent][0] = child

    tree[child][2] = parent

print(pre_order(1))