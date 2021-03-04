import sys
sys.stdin = open("input.txt")

T = 10

for _ in range(1, T+1):
    tc = int(input())
    password = list(map(int, input().split()))

    i = 0
    while password[-1] > 0:
        # 5 안넘게
        i = (i % 5) + 1
        # 빼고 바로 뒤에 붙여줌
        password.append(password.pop(0) - i)

    password[-1] = 0
    print('#{} {} {} {} {} {} {} {} {}'.format(tc, *password))
