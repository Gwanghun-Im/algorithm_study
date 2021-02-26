import sys
sys.stdin = open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    price = list(map(int, input().split()))
    profit = 0
    my_max = max(price)
    max_i = price.index(my_max)

    for i in range(N - 1):
        if i < max_i:
            pred = my_max - price[i]
            if pred <= 0:
                continue
            profit += pred
        if i == max_i:
            my_max = max(price[i + 1:])
            max_i = price.index(max(price[i + 1:]), max_i+1)
    print("#{} {}".format(tc, profit))

