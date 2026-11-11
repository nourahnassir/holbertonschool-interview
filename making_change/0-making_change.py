#!/usr/bin/python3
"""
Module for solving the Coin Change problem using Dynamic Programming.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.
    """
    if total <= 0:
        return 0

    # dp[i] will store the minimum coins needed for amount i
    # Initialize table with infinity for all amounts up to total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
