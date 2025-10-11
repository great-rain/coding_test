"""
5 3
5 4 3 2 1
1 3
2 4
5 5
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [i for i in map(int, input().split())]
temp = 0
perpix = [0]

for i in arr:
    temp = temp + i
    perpix.append(temp)

for _ in range(M):
    start, end = map(int, input().split())
    print(perpix[end]-perpix[start-1])