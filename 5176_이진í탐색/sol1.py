import sys
sys.stdin = open("input.txt")

T = int(input())

def tree_insert(n):
    global num, N
    if n <= N:
        tree_insert(n * 2)
        nodes[n] = num
        num += 1
        tree_insert(n * 2 + 1)

for tc in range(1, T+1):
    N = int(input())
    nodes = [0]*(N+1)
    num = 1
    tree_insert(num)

    print("#{} {} {}".format(tc, nodes[1], nodes[N//2]))
