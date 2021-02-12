import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    N_list = list(map(int, input().split()))
    for i in range(N-1):
        for j in range(N-i-1):
            if N_list[j] > N_list[j+1]:
                N_list[j], N_list[j+1] = N_list[j+1], N_list[j]

    print("#{} {}".format(tc, ' '.join([str(i) for i in N_list])))

