import sys

input = sys.stdin.readline


def solve():
    # n = int(input())
    # n, k = map(int, input().split())
    # a = list(map(int, input().split()))
    # s = input().strip()
    n = int(input())
    s = input().strip()

    def count_chain(start):
        ways = 0

        for first in ['0', '1']:
            expected = first
            valid = True

            for i in range(start, n, 2):
                if s[i] != '?' and s[i] != expected:
                    valid = False
                    break

                if expected == '0':
                    expected = '1'
                else:
                    expected = '0'

            if valid:
                ways += 1

        return ways

    even = count_chain(0)
    odd = count_chain(1)

    print(even * odd)


t = int(input())

for i in range(t):
    solve()