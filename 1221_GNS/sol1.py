import sys
sys.stdin = open("input.txt")

T = int(input())


for _ in range(1, T+1):
    tc, n = input().split()
    alien = list(input().split())
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
    alien_dict = {v:i for i,v in num_dict.items()}

    alien2earth = [num_dict.get(i) for i in alien]
    alien2earth.sort()

    result = [alien_dict.get(i) for i in alien2earth]

    print("{} {}".format(tc, ' '.join(result)))

