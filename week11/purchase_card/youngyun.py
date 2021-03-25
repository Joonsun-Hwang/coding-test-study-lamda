from collections import defaultdict


def solve():
    dp = defaultdict(int)
    for i in range(1, n+1):
        for j in range(1, i+1):
            dp[i] = max(dp[i], dp[i-j]+cards[j-1])

    return dp[n]


if __name__ == "__main__":
    n = int(input())
    cards = list(map(int, input().split()))
    print(solve())
