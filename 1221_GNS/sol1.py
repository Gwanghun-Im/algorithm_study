import sys
sys.stdin = open("input.txt")

T = int(input())


for _ in range(1, T+1):
    tc, n = input().split()
    alien = list(input().split())
    # 외계문자를 숫자로 바꿔주는 dict
    num_dict = {"ZRO":0,
                "ONE":1,
                "TWO":2,
                "THR":3,
                "FOR":4,
                "FIV":5,
                "SIX":6,
                "SVN":7,
                "EGT":8,
                "NIN":9}
    # 숫자를 외계문자로 바꿔주는 dict
    alien_dict = {v:i for i,v in num_dict.items()}

    # 외계문자를 하나하나 숫자로 바꿔준다.
    alien2earth = [num_dict.get(i) for i in alien]
    # 정렬
    alien2earth.sort()

    # 정렬된 숫자를 하나하나 외계문자로 바꿔준다.
    result = [alien_dict.get(i) for i in alien2earth]

    # 한칸뛰고 join
    print("{} {}".format(tc, ' '.join(result)))

