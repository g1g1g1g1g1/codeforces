import sys
from collections import defaultdict

input = sys.stdin.readline


def solve():
    # n = int(input())
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()
    n, m = map(int, input().split())
    
    grid = []

    for _ in range(n):
        row = input().strip()
        grid.append(row)

    prefix_rows = defaultdict(list)
    prefix_cols = defaultdict(list)

    for i in range(n):
        prefix_row = [0] * m

        for j in range(m):
            if grid[i][j] == '1':
                if j == 0:
                    prefix_row[j] = 1
                else:
                    prefix_row[j] = prefix_row[j - 1] + 1
            else:
                if j > 0:
                    prefix_row[j] = prefix_row[j - 1]

        prefix_rows[i] = prefix_row

    for j in range(m):
        prefix_col = [0] * n

        for i in range(n):
            if grid[i][j] == '1':
                if i == 0:
                    prefix_col[i] = 1
                else:
                    prefix_col[i] = prefix_col[i - 1] + 1
            else:
                if i > 0:
                    prefix_col[i] = prefix_col[i - 1]

        prefix_cols[j] = prefix_col

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                left = prefix_rows[i][j] == j + 1
                top = prefix_cols[j][i] == i + 1

                if not left and not top:
                    print("NO")
                    return

    print("YES")


t = int(input())

for _ in range(t):
    solve()    