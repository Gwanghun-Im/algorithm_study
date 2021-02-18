# 1493 SWEA

문제 자체의 어려움보다는

표를 그릴때 어려움이 존재한다.

표를 그릴때 크기가 중요한데

표 안에 들어가는 최대 숫자는 10000이다

10000을 만들어 주기 위해서 i, j 값은 100 이 되어야 하고

~~모서리는 100만큼 더 늘어나야 한다.~~

> 아 좀 더 늘어나야 하나보다... 100 더 늘렸다

y축을 기준으로 우상향으로 올라간다.

> 계속 올라가서 y == 0 이면 멈춤

```python
import sys
sys.stdin = open("input.txt")

T = int(input())

# 표를 먼저 만들어 준다.
arr = [[0]*301 for _ in range(300)]
i = 1
for y in range(300):
    temp_y = y
    temp_x = 0
    arr[temp_y][temp_x] = i
    i+= 1

    while temp_y > 0:
        temp_x += 1
        temp_y -= 1
        arr[temp_y][temp_x] = i
        i += 1

for tc in range(1, T+1):
    p, q = map(int, input().split())
    p_loc = []
    q_loc = []

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            #p와 q를 찾는다.
            if arr[i][j] == p:
                p_loc = [i,j]
            if arr[i][j] == q:
                q_loc = [i, j]
        # 둘다 찾으면 끝내버림
        if p_loc and q_loc: break

    result = arr[q_loc[0]+p_loc[0]+1][q_loc[1]+p_loc[1]+1]

    print("#{} {}".format(tc, result))


```

