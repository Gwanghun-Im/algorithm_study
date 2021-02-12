import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    N = int(input())
    a = input()

    # 숫자를 dict 형태로 저.장
    how_many = {}
    for i in a:
        if int(i) in how_many :
            how_many[int(i)] += 1
            continue
        how_many[int(i)] = 1

    how = 0 # 얼마?
    many = 0 # 얼마나 많이?
    for i, v in how_many.items():
        if v > many: #
            how = i
            many = v
        if v == many : # 갯수가 같은 경우
            if how < i: # 값이 큰 값으로 해준다
                how = i
    #^^ 별말씀을


    print("#{} {} {}".format(tc,how, many))

