import sys
from collections import defaultdict

input = sys.stdin.readline


def solve():
    # n = int(input())
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()
    n, m = map(int, input().split())
    first_giant = list(map(int, input().split()))
    second_giant = list(map(int, input().split()))

    diff1 = 0

    for i in range(len(first_giant)):
        if i == len(first_giant) - 1:
            diff1 += first_giant[i]
            continue

        diff1 += first_giant[i] - first_giant[i + 1] + 1

    diff2 = 0

    for i in range(len(second_giant)):
        if i == len(second_giant) - 1:
            diff2 += second_giant[i]
            continue

        diff2 += second_giant[i] - second_giant[i + 1] + 1

    if diff1 >= diff2:
        print(1)
    else:
        print(2)

    pass


t = int(input())

for _ in range(t):
    solve()