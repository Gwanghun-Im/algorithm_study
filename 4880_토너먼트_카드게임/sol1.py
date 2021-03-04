import sys
sys.stdin = open("input.txt")

T = int(input())

# 가위바위보 후 승자를 나타내줌
def conquer(a, b):
    i = a
    if n_list[a] == 1 and n_list[b] == 2:
        i = b
    if n_list[a] == 2 and n_list[b] == 3:
        i = b
    if n_list[a] == 3 and n_list[b] == 1:
        i = b
    return i

# 분할한다, 시작 끝을 기준으로,(인덱스 값이 들어옴)
def divide(start, end):
    # 인자가 하나만 들어올땐 바로 반환
    if start == end:
        return start
    # 시작인덱스와, 끝 인덱스를 나눈다.
    new_s = divide(start, (start+end)//2)
    new_e = divide((start+end)//2 + 1, end)
    # 승자를 반환함
    return conquer(new_s, new_e)


for tc in range(1, T+1):
    n = int(input())
    n_list = list(map(int, input().split()))
    print("#{} {}".format(tc, divide(0, n-1)+1))

