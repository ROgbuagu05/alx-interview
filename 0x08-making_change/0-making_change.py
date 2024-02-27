#!/usr/bin/python3
""" Determine the fewest number of coins needed to meet a given amount """


def makeChange(coins, total):
    """
    This function determines the fewest number of coins

    Args:
    coins: A list of the values of the coins in your possession.
    total: The target amount to reach using the coins.

    Returns:
    The fewest number of coins needed to make the total amount or -1 if it cannot be achieved.
    """

    if total == 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1
