"""
Koko loves to eat bananas. There are n piles of bananas, the ith
pile has piles[i] bananas. The guards have gone and will come
back in h hours.

Koko can decide her bananas per-hour eating speed of k. Each hour,
she chooses some pile of bananas and eats k bananas from that pile.
If the pile has less than k bananas, she eats all of them instead
and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the
bananas before the guards return.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30
"""
# https://leetcode.com/problems/koko-eating-bananas/

import math


def minEatingSeed(piles, h):
    left = 1
    right = max(piles)
    res = right
    while left <= right:
        middle = (left + right) // 2
        hours = 0
        for i in range(len(piles)):
            hours += math.ceil(piles[i] / middle)
        if hours <= h:
            res = min(res, middle)
            right = middle - 1
        else:
            left = middle + 1
    return res


p1, h1 = [3, 6, 7, 11], 8
p2, h2 = [30, 11, 23, 4, 20], 5
print(minEatingSeed(p1, h1))
print(minEatingSeed(p2, h2))


"""
Code explanation: 
"""
