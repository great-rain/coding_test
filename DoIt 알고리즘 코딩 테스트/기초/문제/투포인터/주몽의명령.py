"""
start = 0, end = last
S == N -> count += 1 end -1
S < N -> start +
S > N -> end -

6
9
2 6 4 1 5 3
"""

N = int(input())
M = int(input())
armor = sorted(i for i in map(int, input().split()))
start = 0
end = N-1
count = 0

while start < end:
    s = armor[start] + armor[end]
    if s == N:
        count += 1
        start += 1
        end -= 1
    elif s < N:
        start += 1
    elif s > N:
        end -= 1

print(count)