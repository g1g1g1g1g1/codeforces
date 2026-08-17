import sys
from collections import defaultdict, deque

input = sys.stdin.readline


def solve():
    # n = int(input())
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()
    n = int(input())
    parent = list(map(int, input().split()))
    m = int(input())
    dams = list(map(int, input().split()))

    if m == 1:
        print(0)
        return

    skip = min(dams)

    cameras = []

    for dam in dams:
        if dam != skip:
            cameras.append(dam)

    print(len(cameras), *list(cameras))
    pass


t = int(input())

for _ in range(t):
    solve()