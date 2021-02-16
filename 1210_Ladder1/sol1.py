import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    n = int(input())

    arr = [[-1]*102]
    for i in range(100):
        arr.append([-1, *list(map(int, input().split())), -1])

    for i in range(101):
        if arr[100][i] == 2:
            row = i

    depth = 100
    while depth > 0:

        if arr[depth][row+1] == 1 :
            while arr[depth][row+1] == 1:
                row += 1
            depth -= 1
            continue
        if arr[depth][row-1] == 1 :
            while arr[depth][row-1] == 1:
                row -= 1
            depth -= 1
            continue

        depth -= 1


    print("#{} {}".format(n, row-1))

