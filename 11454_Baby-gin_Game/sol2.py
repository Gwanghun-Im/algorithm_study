import sys
sys.stdin = open("input.txt")

T = int(input())


for tc in range(1, T+1):
    x = input()
    # 0 ~ 9 까지의 개수를 센다.
    num = [0]*10
    # result에 run, triplet의 개수를 센다
    result = 0

    # 인풋값 x를 숫자로 바꾼후 인덱스마다 값을 추가
    for i in x:
        num[int(i)] += 1

    for i in range(10):

        # run 에 추가
        if num[i] >= 3:
            result += num[i]//3
            num[i] = num[i]%3

        if 1 < i :
            if num[i-2] and num[i-1] and num[i]:
                tmp = (num[i-2]+num[i-1]+num[i])//3
                result += tmp
                for j in range(i-2, i+1):
                    num[j] -= tmp

    result = 1 if result > 1 else 0
    print("#{} {}".format(tc, result))