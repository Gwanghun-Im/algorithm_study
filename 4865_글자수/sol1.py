import sys
sys.stdin = open("input.txt")

T = int(input())
def str_dict(string):
    dict = {}
    for i in string:
        if i in dict.keys():
            dict[i] += 1
            continue
        dict[i] = 1
    return dict

for tc in range(1, T+1):
    str1 = list(set(input()))
    str2 = str_dict(input())

    num_of_max = 0
    for i in str1:
        if num_of_max < str2.get(i):
            num_of_max = str2.get(i)


    print("#{} {}".format(tc, num_of_max))

