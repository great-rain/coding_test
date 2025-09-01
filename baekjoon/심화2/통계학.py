import sys

def ArithmeticMean(numbers: list) -> int:
    return round(sum(numbers) / len(numbers))

def MediaValue(numbers: list) -> int:
    return sorted(numbers)[len(numbers) // 2]

def ModeValue(numbers: list) -> int:
    count = {}
    for i in numbers:
        count[i] = count.get(i, 0) + 1
    
    # 최대 빈도 찾기
    max_count = max(count.values())
    
    # 최빈값들을 오름차순으로 정렬
    modes = sorted([num for num, cnt in count.items() if cnt == max_count])
    
    # 최빈값이 하나면 그것을, 여러 개면 두 번째로 작은 값을 반환
    if len(modes) == 1:
        return modes[0]
    else:
        return modes[1]

def Range(numbers: list) -> int:
    return max(numbers) - min(numbers)

numbers = []
for _ in range(int(input())):
    numbers.append(int(sys.stdin.readline().rstrip()))

print(ArithmeticMean(numbers))
print(MediaValue(numbers))
print(ModeValue(numbers))
print(Range(numbers))