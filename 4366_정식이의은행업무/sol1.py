import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    bi_num = input()
    tri_num = input()
    bi_li = []
    tri_li = []
    flag = False
    for i in range(len(bi_num)):
        temp = list(bi_num)
        for j in range(2):
            if str(j)==bi_num[i]:
                continue
            temp[i] = str(j)
            bi_li.append(int(''.join(temp),2))

    for i in range(len(tri_num)):
        temp = list(tri_num)
        for j in range(3):
            if str(j)==tri_num[i]:
                continue
            temp[i] = str(j)
            tri_li.append(int(''.join(temp),3))
    for i in bi_li:
        for j in tri_li:
            if i==j:
                flag = True
                print("#{} {}".format(tc, i))
                break
        if flag:
            break

