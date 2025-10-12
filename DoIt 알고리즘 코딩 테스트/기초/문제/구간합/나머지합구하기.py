import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
count = [0] * M
sumlist = [0] * N
sumlist[0] = arr[0]
answer = 0

# 합배열 만들기
for i in range(1, N):
    sumlist[i] = sumlist[i-1] + arr[i] 
    
# 나머지 계산
for i in range(N):
    remainder = sumlist[i] % M
    if remainder == 0:
        answer += 1  # 처음부터 i까지가 M의 배수
    count[remainder] += 1

# 같은 나머지끼리 조합
for i in range(M):
    if count[i] > 1:
        answer += (count[i] * (count[i] - 1) // 2)

print(answer)