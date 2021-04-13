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

hex_to_bin = {
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
T = 13
for tc in range(1, T+1):
    n, m = map(int, input().split())
    code = [input() for _ in range(n)]
    if tc < T:
        continue
    result_dict = {}
    r = []
    i = 0
    while i < n:
        tempcode = ''
        for t in code[i]:
            tempcode += hex_to_bin[t]
        if '1' not in tempcode:
            i += 1
            continue

        for j in range(len(tempcode) - 1, 0, -1):
            if tempcode[j] == '1':
                break
        master_1 = j+1

        width = 1
        while width < len(tempcode):
            k = master_1
            temp = []
            while k >= 7:
                try:
                    temp.insert(0, my_dict[tempcode[k - (7*width):k:width]])
                    k -= (7*width)
                except:
                    k -= 1
            if temp and (not len(temp) % 8):
                break
            else:
                width += 1

        cnt = 1
        while i + 1 < n and code[i] == code[i + 1]:
            i += 1
            cnt += 1

        for tmp in range(0, len(temp),8):
            if str(temp[tmp:tmp+8]) in result_dict.keys():
                result_dict[str(temp[tmp:tmp+8])] += cnt
            else:
                result_dict[str(temp[tmp:tmp+8])] = cnt
        print(temp, width,cnt)
        i += 1

    result = 0
    for rd in result_dict.keys():
        if result_dict[rd] > 4:
            i = []
            for j in rd:
                if j in '0123456789':
                    i.append(int(j))
            if not ((i[0] + i[2] + i[4] + i[6])*3 + i[1] + i[3] + i[5] + i[7]) % 10:
                result += sum(i)

    print("#{} {}".format(tc, result))

