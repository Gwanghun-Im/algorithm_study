import sys
sys.stdin = open("input_.txt")

T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    cancer = [list(map(int, input().split())) for _ in range(n)]
    row = 0
    for i in cancer:
        if max(i) > row:
            row = max(i)
    body = [[0]*row for _ in range(row)]

    n_k = 1
    for li in cancer:
        for i in range(min(li[0], li[2]),max(li[0], li[2])):
            for j in range(min(li[1], li[3]),max(li[1], li[3])):
                body[j][i] = n_k
        n_k += 1

    k = 0
    flag = False
    while not flag:
        k += 1
        for i in range(row+1-k):
            for j in range(row+1-k):
                t_body = body[:]
                for y in range(i, i+k):
                    for x in range(j, j+k):
                        t_body[y][x] = 0
                temp = []
                for y in t_body:
                    for x in y:
                        if x and x not in temp:
                            temp.append(x)
                if len(temp) <= m:
                    print(k)
                    for u in t_body:
                        print(u)
                    flag = True



    print("#{} {}".format(tc, k))

