import sys
sys.stdin = open("input.txt")

T = int(input())


def cost():
    global day, month_1, month_3
    c = 0
    i = 0
    while i < 12:
        if plan[i] == 1:
            c += day*month[i]
        elif plan[i] == 2:
            c += month_1
        elif plan[i] == 3:
            c += month_3
            i += 2
        i += 1
    return c


def dfs(n):
    if n == 12:
        result.append(cost())
    else:
        if month[n] == 0:
            plan[n] = 0
            dfs(n+1)
        else:
            for i in range(3):
                plan[n] = i+1
                dfs(n+1)
                plan[n] = 0


for tc in range(1, T+1):
    day, month_1, month_3, year = map(int, input().split())
    month = list(map(int, input().split()))
    plan = [0] * 12
    result = [year]
    dfs(0)
    print("#{} {}".format(tc, min(result)))

