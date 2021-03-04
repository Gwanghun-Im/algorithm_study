import sys
sys.stdin = open("input.txt")

T = int(input())


dy = [-1, 0, 0, 1]
dx = [0, -1, 1, 0]

for tc in range(1, T+1):
    n = int(input())
    square = [list(map(int, input().split())) for _ in range(n)]
    num_o_visit = [1 for _ in range(n**2 + 1)]
    for y in range(n):
        for x in range(n):
            stack = [(y, x)]
            num = square[y][x]
            while stack:
                now = stack.pop()
                temp_num = square[now[0]][now[1]]
                for i in range(4):
                    temp_y = now[0]+dy[i]
                    temp_x = now[1]+dx[i]
                    if 0 <= temp_y < n and 0 <= temp_x < n:
                        if temp_num + 1 == square[temp_y][temp_x]:
                            stack.append((temp_y, temp_x))
                            num_o_visit[num] += 1
                            break
    max_num_o_visit = max(num_o_visit)
    max_num = num_o_visit.index(max_num_o_visit)
    print("#{} {} {}".format(tc, max_num, max_num_o_visit))

