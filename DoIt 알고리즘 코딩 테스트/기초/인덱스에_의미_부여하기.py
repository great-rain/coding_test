import sys

N = int(sys.stdin.readline())
count = [0]*1001
numbers = list(map(int, sys.stdin.readline().split()))

for number in numbers:
    count[number] += 1 # 인덱스에 숫자값으로 의미를 부여하여 데이터 저장 
    """ex) 10 9 8 7 6 5 4 3 2 1 -> count = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0.... ] """
    
for i in range(1001):
    if count[i] != 0:
        for _ in range(count[i]):
            sys.stdout.write(str(i) + ' ')      
