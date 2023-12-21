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


def solution(words):
    # get unique items from input lst
    lst_sort_words = []
    for i in range(len(words)):
        lst_sort_words.append(sorted(words[i]))
    return lst_sort_words
    # lst_lengths = []
    # # add the lenths of each element in the input list to an array
    # for i in range(len(words)):
    #     lst_lengths.append(len(words[i]))
    # hm = {}
    # # keep track of how many times each length occurs for each word
    # for i in range(len(lst_lengths)):
    #     if lst_lengths[i] not in hm:
    #         hm[lst_lengths[i]] = 1
    #     else:
    #         hm[lst_lengths[i]] += 1


def maxProductTest(words):
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


print("This is the solution in test:", solution(t1))
print(maxProductTest(t1))
