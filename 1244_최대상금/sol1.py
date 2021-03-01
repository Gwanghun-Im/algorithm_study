def reward(M, count, k):
    global maxi, size, ch_cnt
    if count == N:
        M = int(''.join(map(str, M)))
        if maxi < M:
            maxi = M
        return
    else:
        for i in range(k, size):
            for j in range(i + 1, size):
                if M[j] >= M[i]:
                    ch_cnt += 1
                    temp = M[:]
                    temp[i], temp[j] = temp[j], temp[i]
                    reward(temp, count + 1, i)


T = int(input())
for t in range(T):
    M, N = input().split()
    N = int(N)
    M = list(map(int, list(M)))
    size = len(M)
    maxi = 0
    ch_cnt = 0
    reward(M, 0, 0)
    if ch_cnt == 0:
        maxi = ''.join(map(str, M))
        if N % 2:
            maxi = int(maxi[:-2] + maxi[-1] + maxi[-2])

    print('#{} {}'.format(t + 1, maxi))