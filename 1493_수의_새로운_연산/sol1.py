import sys
sys.stdin = open("input.txt")

T = int(input())

arr = [[0]*301 for _ in range(300)]
i = 1
for y in range(300):
    temp_y = y
    temp_x = 0
    arr[temp_y][temp_x] = i
    i+= 1

    while temp_y > 0:
        temp_x += 1
        temp_y -= 1
        arr[temp_y][temp_x] = i
        i += 1

for tc in range(1, T+1):
    p, q = map(int, input().split())
    p_loc = []
    q_loc = []

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == p:
                p_loc = [i,j]
            if arr[i][j] == q:
                q_loc = [i, j]
        if p_loc and q_loc: break

    result = arr[q_loc[0]+p_loc[0]+1][q_loc[1]+p_loc[1]+1]

    print("#{} {}".format(tc, result))

