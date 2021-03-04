import sys
sys.stdin = open("input.txt")

T = 10


for tc in range(1, T+1):
    n, start = map(int, input().split())
    li = list(map(int, input().split()))
    max_n = max(li) + 1
    contact = [[] for _ in range(max_n)]
    visited = [False for _ in range(max_n)]
    for i in range(0, n, 2):
        contact[li[i]].append(li[i+1])
    stack = [[] for _ in range(n)]
    stack[0].append(start)
    visited[start] = True
    nums = []
    for i in range(n):
        now = []
        while stack[i]:
            temp = stack[i].pop()
            visited[temp] = True
            if contact[temp]:
                for j in contact[temp]:
                    if not visited[j]:
                        stack[i+1].append(j)
                        now.append(j)
        if now:
            nums.append(now)
    print("#{} {}".format(tc, max(nums[-1])))

