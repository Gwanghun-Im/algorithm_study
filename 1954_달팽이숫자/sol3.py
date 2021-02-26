import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):

    n = int(input())

    snail = [[1] + [0] * n + [1] for _ in range(n)]
    snail += [[1] * (n+2)]


    #     우 하 좌 상
    dr = [0, 1, 0, -1] # y에 더해줄 값
    dc = [1, 0, -1, 0]# x에 더해줄값
    x, y = 1, 0
    idx = 0
    for i in range(1, n**2 + 1):
        snail[y][x] = i
        # print(x, y , dc[idx], dr[idx], idx)
        if snail[y+dr[idx]][x+dc[idx]] > 0:
            idx += 1
            idx %= 4
        x += dc[idx]
        y += dr[idx]








    
    print("#{} ".format(tc, ))
    for i in range(n):
        print(*snail[i][1:n+1])

