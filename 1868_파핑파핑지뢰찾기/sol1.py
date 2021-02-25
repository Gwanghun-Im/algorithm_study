import sys
sys.stdin = open("input.txt")

T = int(input())


def minecheck(i, j):
    dx = [0, -1, -1, -1, 0, 1, 1, 1]
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    temp = []
    for k in range(8):
        new_i = i+dy[k]
        new_j = j+dx[k]
        if mine[new_i][new_j] == '.' and (not visited[new_i][new_j]):
            temp += [new_i, new_j]
    return temp



for tc in range(1, T+1):
    n = int(input())


    mine = [list('/' * (n+2))]
    for i in range(n):
        mine.append(list('/'+input()+'/'))
    mine.append(list('/'*(n+2)))

    visited = [[0]*302 for _ in range(302)]
    stack = []
    while True:
        pass

    print("#{} ".format(tc, ))

