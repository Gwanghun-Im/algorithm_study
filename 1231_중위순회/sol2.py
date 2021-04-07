import sys
sys.stdin = open("input.txt")

T = 10

def in_order(tree, idx):
    global res
    if idx*2 < len(tree):
        in_order(tree,idx*2)
    res += tree[idx]
    if idx*2 +1 < len(tree):
        in_order(tree, idx*2+1)

for tc in range(1, T+1):
    n = int(input())
    tree = [0] * (n+1)
    for i in range(n):
        temp = list(input().split())
        tree[int(temp[0])] = temp[1]
    res = ''
    in_order(tree, 1)
    print("#{} {}".format(tc, res))

