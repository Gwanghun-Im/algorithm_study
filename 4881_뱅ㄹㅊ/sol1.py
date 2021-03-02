import sys
sys.stdin = open("input.txt")


def solve(n):
    result = 10 * n
    while x_stack:
        now = x_stack.pop()
        if len(now) == n:
            temp = 0
            for i in range(n):
                temp += matrix[i][now[i]]
            if result > temp:
                result = temp
        else:
            for i in range(n):
                temp = 0
                for j in range(len(now)):
                    temp += matrix[j][now[j]]
                if temp >= result:
                    break
                if i not in now:
                    x_stack.append(now + [i])
    return result


T = int(input())

for tc in range(1, T+1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    x_stack = [[i] for i in range(n)]

    print("#{} {}".format(tc, solve(n)))

