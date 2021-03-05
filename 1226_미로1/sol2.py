import sys
sys.stdin = open("input.txt")

from collections import deque

T = 10


for tc in range(1, T+1):
    n = input()
    queue = deque()
    queue.append(1)
    if queue:
        print(queue)
        print('say young')
    print("#{} ".format(tc, ))

