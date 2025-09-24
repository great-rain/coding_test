n,m = map(int, (input().split()))
output = [[]]

def backtracking(start:int, end:int):
    if end == n and start == n:
        output[-1].append([start, end])
        return
    elif end == n:
        output.append([])
        return backtracking(start+1, 1)
    elif start == end:
        return backtracking(start, end + 1)
    
    output[-1].append([start, end])
    return backtracking(start, end + 1)

backtracking(1, 1)

for line in output:
    for item in line:
        print(' '.join(map(str, item)))