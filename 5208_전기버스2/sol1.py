import sys
sys.stdin = open("sample_input.txt")

T = int(input())


def solve(idx, now):
    global cnt
    if now >= cnt:
        return

    if idx >= n-1:
        if now<cnt:
            cnt = now
        return

    for i in range(charger[idx]):
        solve(idx + i+1, now+1)



for tc in range(1, T+1):
    inp = list(map(int, input().split()))
    n = inp[0]
    charger = inp[1:]
    cnt = n
    solve(0, -1)

    print("#{} {}".format(tc, cnt))
