import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    stick = input().split('()')
    laser = '0'.join(stick)

    stick_split = []
    i = 0
    while len(laser) != laser.count('0'):
        if laser[i] == '(':
            cnt = 0
            tf = False
            for j in range(i+1, len(laser)):
                if laser[j] == '0':
                    cnt += 1
                if laser[j] == '(':
                    break
                if laser[j] == ')':
                    stick_split += [cnt]
                    tf = True
                    break
            if tf:
                laser = laser[:i] + '0'*cnt + laser[j+1:]
                i = 0
        if i < len(laser)-1:
            i += 1
            continue
        i -= i

    result = 0
    for i in stick_split:
        result = result + 1 + i

    print("#{} {}".format(tc, result))

