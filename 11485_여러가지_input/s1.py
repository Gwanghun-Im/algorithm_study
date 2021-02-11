import sys
sys.stdin = open('input.txt')

N = int(input())
result = 1 if N%2 else 0
print(result)

numbers = list(map(int, input().split()))
result = sum(numbers)
print(result)

N = int(input())
matrix = []
for _ in range(N):
    matrix += [list(map(int, input().split()))]
print(matrix[1][1])