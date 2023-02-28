#!/usr/bin/python3
"""
Playing with coins
"""

def makeChange(coins, total):
    """determine the fewest number of coins
    needed to meet a given amount total
    """
    if total <= 0:
        return 0
