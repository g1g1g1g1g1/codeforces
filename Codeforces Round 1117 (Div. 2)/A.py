import sys
from collections import defaultdict

input = sys.stdin.readline


def solve():
    # n = int(input())
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()
    n, m = map(int, input().split())
    words = []
    abbs = []

    for _ in range(n):
        words.append(input().strip())

    for _ in range(m):
        abbs.append(input().strip())

    first_letters = set()

    for word in words:
        first_letters.add(word[0])

    for abb in abbs:
        for c in abb:
            if c.lower() not in first_letters:
                print("NO")
                return

    print("YES")
    pass


t = int(input())

for _ in range(t):
    solve()