import sys
sys.stdin = open("input.txt")

#T = int(input())


for tc in range(int(input())):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    max_Sell = price.pop()

    while price:
        if price[-1] >= max_Sell:
            max_Sell = price.pop()
            continue
        profit += (max_Sell - price.pop())
    print("#{} {}".format(tc+1, profit))

