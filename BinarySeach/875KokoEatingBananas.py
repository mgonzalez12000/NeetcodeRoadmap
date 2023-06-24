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
p3, h3 = [30,11,23,4,20], 6
print(minEatingSeed(p1, h1))
print(minEatingSeed(p2, h2))
print(minEatingSeed(p3, h3))


"""
Code explanation: implement your typical binary search algorithm with three pointers, left, right, and middle, where our nmiddle represents
our speed of eating bananas/hour. However, if koko is able to eat bananas in time before the h amount of hours given, we will shift our 
right pointer -1 from the middle, to check if we can get a smaller middle value (speed). We will keep tracking our minimum possible 
result by using the min() trcik in python = min(arg1, arg2)
"""
