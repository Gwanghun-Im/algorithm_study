import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N, M, K = map(int,input().split())
    Ns = list(map(int, input().split()))
    Ns.sort()

    fishbread = 0
    t = 0
    ans = 'Possible'
    next_t = M
    # print(Ns)
    while Ns:
        if t == next_t:
            fishbread += K
            # print(t, fishbread,'붕어')
            next_t += M
        while Ns and t == Ns[0]:
            Ns.pop(0)
            fishbread -= 1
            # print(fishbread, t)
        if fishbread < 0:
            # print(Ns)
            # print(t, next_t, fishbread)
            ans = 'Impossible'
            break
        t += 1

    print("#{} {}".format(tc, ans))

