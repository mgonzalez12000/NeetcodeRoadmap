"""
Given an array of strings strs, group the anagrams together. You can
return the answer in any order

An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letter exactly once

Example 1: Input: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
           Output: [["bat"], ["nat", "tan"]. ["ate, "eat", "tea"]]
Example 2: Input: strs = [""]
           Output: [[""]]
"""
# https://leetcode.com/problems/group-anagrams/

def groupAnagrams(strs):
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    hm = {}
    groupIndex = 0
    result = []
    for i in range(len(strs)):
        sorting = sorted(strs[i])
        sortedStr = str(sorted(sorting))
        if sortedStr not in hm:
            hm[sortedStr] = groupIndex
            groupIndex += 1
            result.append([strs[i]])
        else:
            index = hm[sortedStr]
            result[index].append(strs[i]) 
    return result

test = ["eat", "tea", "tan", "ate", "nat", "bat"]
test2 = [""]
print(groupAnagrams(test))
print(groupAnagrams(test2))

practice = ['test']
result_practice = str(practice)
print(result_practice)

"""
Code explanation: The main goal for this question is to put all common anagram into a "group" or a list.
The finnal result will be 2d list. From problem 242 we know that an anagram is word that is made from it's
rearranged chars. Knowing this, we can sorted each word in the input list. Since a hashmap, does not take
into consideration duplicates, we can use a hashmap/dictionary data structure to keep track of our "groups".

We will initiate a hm to keep track of our "groups", a groupIndex var to keep track of our index, and a result list
to be returned. Iterate through the list. On every iteration we will sort the element. If that sorted element is
not in the hashmap yet, we will add it to the hashmap, along with our groupIndex which will represent which group
the sorted word belongs to. We will increment the groupIndex var, and append our original word to our result list.
However, if the sorted word already exists in the hashmap, then we simply grab the index aka value of the hashmap,
and append it to the list within our result list. Finally, return result list.

This pattern can be applied to validAnagram242
"""