import sys
sys.stdin = open("input.txt")

T = int(input())

dict16 = {
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

for tc in range(1, T+1):
    n, inp = input().split()
    temp = ''
    for i in range(int(n)):
        if inp[i] in dict16.keys():
            temp += dict16[inp[i]]
        else:
            m = int(inp[i])
            new_m = ''
            while m:
                new_m = str(m % 2) + new_m
                m //= 2
            if len(new_m) < 4:
                new_m = '0'*(4-len(new_m))+new_m
            temp += new_m

    print("#{} {}".format(tc, temp))

