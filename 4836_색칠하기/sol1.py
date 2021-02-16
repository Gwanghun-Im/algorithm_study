import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    # 비어있는 팔레트를 만든다.
    palette = [[0 for _ in range(10)] for _ in range(10)]
    N = int(input())
    # 보라색의 개수를 파악
    cnt = 0
    
    # N개의 색칠과정
    for _ in range(N):
        r1, c1, r2, c2, color = map(int, input().split())
        # row, col만큼 색칠
        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                palette[i][j] += color
    
    # 팔레트에서 찾는다, 개수를
    for i in range(len(palette)):
        for j in range(len(palette[0])):
            # 3이면 1, 2가 색칠된것이기 때문에 보라색, ... 
            # 근데 이렇게 하면 빨간색으로 3번칠해도 보라색이 된다. 
            # 약간 애매함, pass뜨긴 했는데 찝찝
            if palette[i][j] == 3:
                cnt += 1


    print("#{} {}".format(tc, cnt))

