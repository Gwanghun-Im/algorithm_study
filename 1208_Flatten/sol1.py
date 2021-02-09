import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    dump = int(input())
    boxes = list(map(int, input().split()))
    boxes_2d = [[0 for _ in range(100)] for _ in range(100)]
    cnt = 0

    for i in range(99, -1, -1):
        for j in range(99, -1, -1):
            if boxes[j] > 0:
                boxes_2d[i][j] += 1
                boxes[j] -= 1
    while dump > 0:
        brk = False
        for i in range(100):
            if brk:
                break
            for j in range(100):
                if boxes_2d[i][j] == 1:
                    boxes_2d[i][j] = 0
                    brk = True
                    break

        brk = False
        for i in range(99,-1, -1):
            if brk:
                break
            for j in range(99, -1, -1):
                if boxes_2d[i][j] == 0:
                    boxes_2d[i][j] = 1
                    brk = True
                    break
        dump -= 1
    high = 0
    for i in range(100):
        if sum(boxes_2d[i]) > 0:
            high = i
            break
    low = 0
    for i in range(99, -1, -1):
        if sum(boxes_2d[i]) < 100:
            low = i
            break
    diff = low - high +1
    print("#{} {}".format(tc, diff))

