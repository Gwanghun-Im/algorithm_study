'''
다음은 연결되어 있는 두개의 정점 사이의 간선을 순서대로 나열해 놓은 것이다. 
모든 정점을 깇이 우선 탐색하여 화면에 깊이우선탐색 경로를 출력하시오.
시작 정점을 1로 시작하시오
'''


def dfs(idx):
    global n, s
    for i in link[idx]:
        if not visited[i]:
            visited[i] = 1
            s+=str(i)
            dfs(i)


inp = list(map(int, input().split()))
n = max(inp)
link = [[] for _ in range(n+1)]
visited = [0]*(n+1)
for i in range(0,len(inp), 2):
    link[inp[i]].append(inp[i+1])
    link[inp[i+1]].append(inp[i])

visited[1] = 1
s = '1'
dfs(1)
print('-'.join(s))

# inp = list(map(int, input().split()))
# n = max(inp)
# link = [[] for _ in range(n+1)]
# visited = [0]*(n+1)
# for i in range(0,len(inp),2):
#     link[inp[i]].append(inp[i+1])
#     link[inp[i+1]].append(inp[i])
# stack = [1]
# visited[1] = 1
# s = []
# while stack:
#     now = stack.pop()
#     s.append(str(now))
#     for i in link[now]:
#         if not visited[i]:
#             visited[i] = 1
#             stack.append(i)
#
# print('-'.join(s))