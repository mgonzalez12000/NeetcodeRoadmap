"""
Given a string array words, return the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. If no such two words exist, return i


Example 1:
Input: words = ["abcw","baz","foo","bar","xtfn","abcdef"]
Output: 16
Explanation: The two words can be "abcw", "xtfn".

Example 2:
Input: words = ["a","ab","abc","d","cd","bcd","abcd"]
Output: 4
Explanation: The two words can be "ab", "cd".

Example 3:
Input: words = ["a","aa","aaa","aaaa"]
Output: 0
Explanation: No such pair of words.
"""


def maxProduct(words):
    for i in range(0, len(words)):
        hs = set()
        tracker = 0
        result = 0
        for j in range(1, len(words)):
            if len(words[i]) == len(words[j]):
                for x in range(len(words[i])):
                    hs.add(words[i][x])
                for y in range(len(words[j])):
                    if words[j][y] in hs:
                        continue
                    else:
                        tracker = len(words[i]) * len(words[j])
                        result = max(result, tracker)
    return result


t1 = ["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
t2 = ["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
t3 = ["a", "aa", "aaa", "aaaa"]


print(maxProduct(t1))
