import sys
from collections import defaultdict

def solve(a,cards):
    print("cards: ",cards)
    dp = defaultdict(int)
    for i in range(a):
        dp[i] = max(cards[i],dp[i])
    
    for j in range(2,a):
        dp[j] = max(dp[j],dp[j-1]+dp[1])
    
    return dp[j]





if __name__ == "__main__":
    a=int(input())
    cards = list(map(int,input().split()))
    print(solve(a,cards))


