visited = set()
count = 0
n = int(input())
for _ in range(n):
    s = input()
    if s == "ENTER":
        visited = set()
    else:
        if s not in visited:
            count += 1
            visited.add(s)  # 이 줄이 빠져있었음
print(count)