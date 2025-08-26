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
            visited.add(s)
print(count)