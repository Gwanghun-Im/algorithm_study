inp = list(map(int, input().split()))
n = max(inp)
link = [[] for _ in range(n+1)]
visited =  [0]*(n+1)
for i in range(0,len(inp),2):
    link[inp[i]].append(inp[i+1])
    
queue = [1]
visited[1] = 1
s = [str(1)]
while queue:
    now = queue.pop(0)
    for i in link[now]:
        if not visited[i]:
            visited[i] = 1
            queue.append(i)
            s.append(str(i))

print('-'.join(s))