"""
4 3
1 2 3 4
2 3 4 5
3 4 5 6
4 5 6 7
2 2 3 4
3 4 3 4
1 1 4 4
"""
import sys
input = sys.stdin.readline

N, Q = map(int, input().split())

board = [[0]*(N+1)] + [[0] + [i for i in map(int, input().split())] for _ in range(N)]

prefix_sum = [[0 for _ in range(N+1)] for _ in range(N+1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        prefix_sum[i][j] = prefix_sum[i][j-1] + prefix_sum[i-1][j] - prefix_sum[i-1][j-1] + board[i][j]

for _ in range(Q):
    x1, y1, x2, y2 = map(int, input().split())
    result = prefix_sum[x2][y2] - prefix_sum[x1-1][y2] - prefix_sum[x2][y1-1] + prefix_sum[x1-1][y1-1]
    print(result)
    