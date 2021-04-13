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

HEX = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


for tc in range(1, T+1):
    n, m = map(int, input().split())
    code = [input()[:m] for _ in range(n)]
    r_dict = dict()

    for i in range(n):
        Bin = ''
        for t in code[i]:
            Bin += HEX[t]
        code[i] = Bin

    for Bin in code:
        if '1' not in Bin:
            continue
        j = len(Bin) - 1
        while j > 7:
            if Bin[j] == '0':
                j -= 1
            else:
                w = 1
                temp = []

                while len(temp) != 8:
                    temp = []
                    for tco in range((j+1)-56*w, j+1, 7*w):
                        try:
                            temp.append(my_dict[Bin[tco:tco + 7 * w:w]])
                        except:
                            w += 1
                            break
                j = (j+1)-56*w - 1
                if str(temp) in r_dict.keys():
                    r_dict[str(temp)] += 1
                else:
                    r_dict[str(temp)] = 1

    result = 0
    for rd in r_dict.keys():
        if r_dict[rd] > 4:
            i = []
            for j in rd:
                if j in '0123456789':
                    i.append(int(j))
            if not ((i[0] + i[2] + i[4] + i[6])*3 + i[1] + i[3] + i[5] + i[7]) % 10:
                result += sum(i)

    print("#{} {}".format(tc, result))