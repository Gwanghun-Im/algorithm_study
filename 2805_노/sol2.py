import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
    values = []
    for i in range(n):
        values.append(list(map(int, list(input()))))

    x = n//2
    y = 0

    # 진행순서
    # s : start
    # e : end
    # 0 0 s 0 0
    # 0 ↙ ↙ ↖ 0
    # ↘ ↘ e ↖ ↖
    # 0 ↘ ↗ ↗  0
    # 0 0 ↗ 0 0

    result = 0
    # delta
    dy = [1, 1, -1, -1]
    dx = [-1, 1, 1, -1]
    while x != y != n//2:
        i = 0
        tx = x
        ty = y
        while True:
            result += values[y][x]
            y += dy[i]
            x += dx[i]
            if x == n//2 or y == n//2:
                i += 1
            if tx == x and ty == y:
                break
        # 싸이클이 끝나면 아래로 한칸 내려줌
        y += 1
    # 가운데는 따로 더해줌
    result += values[y][x]

    print("#{} {}".format(tc, result))

