import sys
sys.stdin = open("input.txt")

T = int(input())

my_dict = {
    '0001101': 0,
    '0011001': 1,
    '0010011': 2,
    '0111101': 3,
    '0100011': 4,
    '0110001': 5,
    '0101111': 6,
    '0111011': 7,
    '0110111': 8,
    '0001011': 9
}


for tc in range(1, T+1):
    n, m = map(int, input().split())
    code = [input() for _ in range(n)]
    r = []
    i = 0

    while i < n:
        if '1' not in code[i]:
            i += 1
            continue
        for j in range(m-1, 0, -1):
            if code[i][j] == '1':
                break
        j += 1
        temp = []
        for k in range(j, 0, -7):
            try:
                temp.insert(0, my_dict[code[i][k-7:k]])
            except:
                break
        cnt = 1
        while i+1 < n and code[i] == code[i+1]:
            i += 1
            cnt += 1
        if cnt >= 5:
            r.append(temp)
        i += 1
    result = 0
    for i in r:
        try:
            if not ((i[0] + i[2] + i[4] + i[6])*3 + i[1] + i[3] + i[5] + i[7]) % 10:
                result += sum(i)
        except:
            continue

    print("#{} {}".format(tc, result))

