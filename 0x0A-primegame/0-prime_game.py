#!/usr/bin/python3
"""Prime Game"""


def is_prime(num):
    """
    Check if a number is prime
    """
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def isWinner(x, nums):
    """
    Determines the winner of a game played x rounds
    Args:
    x: The number of rounds to play.
    nums: List of integers representing the starting set for each round.

    Returns:
    Name of player with the most wins or None if number of wins is equal
    """
    winners = []
    for n in nums:
        maria_moves = True
        while n > 1:
            found_prime = False
            for i in range(2, n + 1):
                if is_prime(i) and n % i == 0:
                    found_prime = True
                    n -= i
                    break
            if not found_prime:
                break
            maria_moves = not maria_moves

    if maria_moves:
        winners.append("Maria")
    else:
        winners.append("Ben")

    # Count the number of wins for each player
    maria_wins = winners.count("Maria")
    ben_wins = winners.count("Ben")

    # Determine the overall winner
    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None
