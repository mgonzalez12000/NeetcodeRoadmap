def reverseString(s):
    """
    Do not return anything, modify s in-place instead.
    """
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


s1 = ["h","e","l","l","o"]
s2 = ["H","a","n","n","a","h"]
