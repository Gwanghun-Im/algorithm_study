# 4408 SWEA

자기방으로 들어가기 

생각해보면 복도를 만들어서

이동하는것을 체크하고

복도에서 가장 많이 겹친부분을 return 하면 된다.

```python
import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n = int(input())
	
    # 복도인데, 변수명 잘못생각함
    room = [0]*201
	
    # 각자 시작과 목표방
    goal = []
    for i in range(n):
        goal += [list(map(int, input().split()))]
	
    for temp in goal:
        temp.sort()
        # 방 번호를 하나로 묶었다.
        for i in range(2):
            if temp[i] % 2:
                temp[i] += 1
            temp[i] //= 2
        # 복도에 색칠하기
        for i in range(temp[0], temp[1]+1):
            room[i] += 1

    print("#{} {}".format(tc, max(room)))
```

