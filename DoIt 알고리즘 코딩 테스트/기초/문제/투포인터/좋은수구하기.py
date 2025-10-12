"""
10
1 2 3 4 5 6 7 8 9 10

10
1 2 7 9 11 20 23 31 42 50 
"""
import sys
input = sys.stdin.readline
N = int(input())
A = sorted(map(int, input().split()))
count = 0

for i in range(N):
    target = A[i]
    start = 0
    end = N - 1
    
    while start < end:
        if start == i:
            start += 1
            continue
        if end == i:
            end -= 1
            continue
            
        s = A[start] + A[end]
        if s == target:
            count += 1
            break
        elif s < target:
            start += 1
        else:
            end -= 1

print(count)