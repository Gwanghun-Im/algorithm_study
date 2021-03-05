import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    n, m = map(int, input().split())
    li = list(map(int, input().split()))
    # 인덱스번호와 치즈양만큼 리스트로 묶음
    pizza = [[i+1, v] for i, v in enumerate(li)]
    # 오븐에는 n개의 피자만 들어간다
    oven = pizza[:n]
    # 오븐에 들어가지 못한 피자
    pizza = pizza[n:]
    # 오븐에 마지막으로 피자가 1개만 남았을때까지
    while len(oven) != 1:
        # 꺼내는 피자
        check_pizza = oven.pop(0)
        # 치즈의 양은 전보다 줄었다.
        check_pizza[1] //= 2
        # 만약 치즈가 다 녹았다?
        if check_pizza[1]==0:
            # 그리고 오븐에 들어가지 못한피자가 있다?
            if pizza:
                # 그럼 오븐에 넣는다.
                oven.append(pizza.pop(0))
        # 치즈가 안녹았다?
        else:
            # 다시 오븐에 집어 넣어
            oven.append(check_pizza)

    print("#{} {}".format(tc, oven[0][0]))

