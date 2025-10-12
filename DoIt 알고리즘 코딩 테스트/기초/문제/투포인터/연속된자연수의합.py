"""
sum < N -> end + 1
sum > N -> start + 1, sum - start (왼쪽값 지우기)
sum = N -> count += 1
"""

N = int(input())

start = 1
end = 1
count = 0
s = 1

while start < N//2+1:
    if s == N:
        count += 1
        end += 1
        s += end 
    elif s < N:
        end += 1
        s += end
    elif s > N:
        s -= start
        start += 1

print(count+1)