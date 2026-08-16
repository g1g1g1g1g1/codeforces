import sys

input = sys.stdin.readline


def solve():
    # n = int(input())
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()
    n, w = map(int, input().split())
    print(n - n // w)
    pass


t = int(input())

for _ in range(t):
    solve()