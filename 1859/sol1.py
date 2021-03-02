import sys
sys.stdin = open("input.txt")

#T = int(input())


for tc in range(int(input())):
    N = int(input())
    price = list(map(int, input().split()))
    # 현재 이득
    profit = 0
    # 가장 고점을 맨 뒤에있는 값으로 설정, 가장 최근 값은 사거나 팔 수 없기에
    # 그냥 버린다.
    max_Sell = price.pop()

    # 뒤에서 고점을 비교하여
    while price:
        # 고점보다 값이 더 크면
        if price[-1] >= max_Sell:
            # 고점을 바꾼다.
            max_Sell = price.pop()
            continue
        # 아니면 고점과 비교하여 값의 차이를 profit에 더해준다,
        profit += (max_Sell - price.pop())
    print("#{} {}".format(tc+1, profit))

