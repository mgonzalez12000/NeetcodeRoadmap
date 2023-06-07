"""
Given two strings s and t return true if t is an
anagram of s, and false otherwise.

An ANAGRAM is a word or phrase formed by rearranging the
letters of a different word or phrase, typically using
all the original letters exactly one.

Example 1: input: s = 'anagram', t = 'nagaram'
           output: true

Example 2: input: s = "rat", t = "car"
           output: false
"""
# https://leetcode.com/problems/valid-anagram/

# Naive approach
def isAnagram(s, t):
    """
    :type s: str
    :type t: str
    :rtype: bool
    """
    dict_s = {}
    dict_t = {}
    for i in range(len(s)):
        if s[i] not in dict_s:
            dict_s[s[i]] = 1
        else:
            dict_s[s[i]] += 1
    for i in range(len(t)):
        if t[i] not in dict_t:
            dict_t[t[i]] = 1
        else:
            dict_t[t[i]] += 1
    if dict_s == dict_t:
        return True
    else:
        return False

s1, t1 = 'anagram', 'nagaram'
s2, t2 = 'rat', 'car'
print('Naive approach')
print(isAnagram(s1, t1))
print(isAnagram(s2, t2))

# Second approach uising only one hashmap
def isAnagram2(s, t):
    tracker = {}
    iterableList = []
    iterableList.append(s)
    iterableList.append(t)
    for i in range(len(iterableList)):
        sorting = sorted(iterableList[i])
        sorted_str = str(sorting)
        if sorted_str not in tracker:
            tracker[sorted_str] = 1
        else:
            tracker[sorted_str] += 1
    if len(tracker) == 1:
        return True
    else:
        return False
    
print('Second approack')
print(isAnagram2(s1, t1))
print(isAnagram2(s2, t2))

# Third approach. Most optimal approach using a hashset
def isAnagram3(s, t):
    hashSet = set()
    iterable_list = []
    iterable_list.append(s)
    iterable_list.append(t)
    for i in range(len(iterable_list)):
        sorting = sorted(iterable_list[i])
        sorted_str = str(sorting)
        if sorted_str not in hashSet:
            hashSet.add(sorted_str)
    if len(hashSet) == 1:
        return True
    else:
        return False

print("Third approach")
print(isAnagram3(s1, t1))
print(isAnagram3(s2, t2))

"""
Code explanation: 

First approach: 
An ANAGRAM, as described, a word(s) or phrase(s) that
contain the same number of letters/char. Knowing this, we can use a
dictionary/hashmap data structure that will allow us to keep track of our
characters. The key will represent that char, while the value will represent
the count. We are creating two dictionaries to keep track of both input
strings. Once both of our dictionaries are populated, we will compare both
dictionaries. If both dictioanries are equal, then both input strings
are indeed anagram. Therefore, we will return TRUE. Otherwise, if both
dictionaries are not equal, we will return FALSE.

Second approach:
We can use one single hashmap to decrease memory usage, instead of using two
hashmpas. In order to do so, we will need to add append both inputs into a list,
and then iterate through the list. When iterating through the list, we will sort
the elements. Once done, if the element does not exist in the hashmap, we add 
to it and make the value 1. Else increment the value by 1. Keep in mind hashmaps
do not take in duplicates, therefore, we can check if the length is 1, if so, it
means it will return TRUE because an anagram exists. Otherwise,m if the length is
not two, it will return FALSE, it is not an anagram.

Third approach:
Using a hashset data structure, we can implement a similar approach by sorting our
elements. But instead, simply adding the sorted elements to the hashset. Since a hashset
does not take duplicates, we can once again check for the length like previosuly.
Using a dictionary/hashmap data structure is not necessary since there really isn't
anything to track
"""