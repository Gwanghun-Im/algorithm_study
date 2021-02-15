# 21.02.15 주기찾기

> 슈도랜덤 생성기를 돌리고 주기를 찾는문제

```python
T = int(input())


for tc in range(1, T+1):
    s, p, q, m = map(int, input().split())
	
    # 새로운 숫자가 들어올때마다 dict형태로 인덱스와 함께 추가한다.
    new_num = {s:0}
	
    # 슈도랜덤생성기를 담는 list
    arr = [s]
    # 현재 인덱스
    i = 0
    
    # 계속반복
    while True:
        #슈도랜덤생성
        arr += [(p*arr[i] + q) % m]
        # 인덱스업데이트
        i += 1

        # 만약 만들어진 숫자가 dict에 있으면 숫자가 반복된 것이고 
        if arr[i] in new_num.keys():
            # 현재 인덱스에서 dict에 담았던 인덱스 값을 빼준다
            result = i - new_num[arr[i]]
            # 반복문은 종료
            break
        # 없다면 딕셔너리에 추가
        new_num[arr[i]] = i



    print("#{} {}".format(tc, result))
```

>  **하지만 시간초과가 떠버렸다.....**
>
> 73개 맞았다.
>
> 어디서 시간을 줄일 수 있을까...?



> %m 부분을 이용하면 풀 수 있을거 같은데.???
>
> 결국 숫자는 최대 m개만 만들어지고, arr[슈도넘버]에 값이 존재하면 되는거자나,
>
> i 에서 arr[슈도넘버] 를 빼면 그만큼 차이가 존재하는거지

```python
T = int(input())


for tc in range(1, T+1):

    s, p, q, m = map(int, input().split())
    arr = [-1 for _ in range(m)]
    arr[s] = 0
    i = 1
    temp = s

    while True:
        temp = (temp * p + q) % m
        if arr[temp] >= 0:
            result = i - arr[temp]
            break

        arr[temp] = i
        i += 1

    print("#{} {}".format(tc, result))
```

> 또 시간초과가 떳다....
>
> 그래도 이번엔 81개 맞췄다.
>
> 왜지 진짜???

```python
T = int(input())


for tc in range(1, T+1):

    s, p, q, m = map(int, input().split())
    
    # m으로 나눈 나머지이기 때문에 숫자는 최대 m개가 생성된다.
    arr = [-1] * m
    # s숫자의 인덱스는 0이다. -> 슈도랜덤생성기의 인덱스를 담아서 사용
    arr[s] = 0
    # 다음 인덱스
    i = 1
    # 첫번째 숫자부터 계산시켜 나갈것
    temp = s

    while True:
        # 슈도랜덤 생성
        temp = (temp * p + q) % m
        # 만약 슈도랜덤에 인덱스 번호가 있는경우(인덱스 번호는 0부터 1이상의 정수)
        if arr[temp] >= 0:
            # 현재 인덱스에서 저장되어있는 전 인덱스를 뺀 값을 출력
            # 이게 cycle이 된다.
            result = i - arr[temp]
            break
		# 만약 슈도랜덤이 없으면 현재 인덱스 번호를 리스트에 저장
        arr[temp] = i
        # 인덱스 업데이트
        i += 1

    print("#{} {}".format(tc, result))
```

> 정답이다
>
> `arr = [-1 for _ in range(m)]`  `->` `arr = [-1] * m`
>
> 여기만 해결해주니까 정답이 나왔다. 
>
> for문이 생각보다 시간을 오래 잡아먹는다는 결론을 얻었다.



