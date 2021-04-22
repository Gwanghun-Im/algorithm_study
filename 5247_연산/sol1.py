import sys
sys.stdin = open("sample_input.txt")

from collections import deque


T = int(input())

for tc in range(1, T+1):
    n, m = map(int, input().split())
    cnt = m-n
    calc = [0] * 10000001
    queue = deque()
    queue.append((n, 0))
    while queue:
        now, count = queue.popleft()
        if count > cnt:
            continue
        if now == m:
            cnt = count
            break
        if calc[now]:
            continue

        calc[now] = 1
        queue.append((now+1, count+1))
        if 0 <= now-1:
            queue.append((now-1, count+1))
        if now*2 < 1000001:
            queue.append((now*2, count+1))
        if 0<= now-10:
            queue.append((now-10, count+1))

    print("#{} {}".format(tc, cnt))

