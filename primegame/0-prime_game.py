#!/usr/bin/python3
"""Prime Game module."""


def isWinner(x, nums):
    """Determine who won the most rounds of Prime Game."""
    if not nums or x <= 0:
        return None

    rounds = min(x, len(nums))
    max_n = max(nums[:rounds])
    if max_n < 1:
        return None

    is_prime = [True] * (max_n + 1)
    if max_n >= 0:
        is_prime[0] = False
    if max_n >= 1:
        is_prime[1] = False

    i = 2
    while i * i <= max_n:
        if is_prime[i]:
            for multiple in range(i * i, max_n + 1, i):
                is_prime[multiple] = False
        i += 1

    prime_counts = [0] * (max_n + 1)
    count = 0
    for num in range(1, max_n + 1):
        if is_prime[num]:
            count += 1
        prime_counts[num] = count

    maria_wins = 0
    ben_wins = 0

    for n in nums[:rounds]:
        if n < 1:
            ben_wins += 1
            continue
        if prime_counts[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    if ben_wins > maria_wins:
        return "Ben"
    return None
