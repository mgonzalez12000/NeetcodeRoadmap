"""
Given an array of string strs, group all anagram together into sublists. You may
return the output in any order

An anagram is a string that contrains the exact same chars as another string, but
the order of the chars can be different

Example 1:
Input: strs = ["act","pots","tops","cat","stop","hat"]
Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]

Example 2:
Input: strs = ["x"]
Output: [["x"]]

Example 3:
Input: strs = [""]
Output: [[""]]
"""

strs = ["act","pots","tops","cat","stop","hat"]
strs2 = ["x"]
strs3 = [""]

# Takes in an array of strings and returns a 2d array of strings
def groupAnagram(strs):
    if strs == [""]:
        return [[""]]
    hm = {}
    # Iterate through the array first and do something upon each iteration
    for element in strs:
        # Sorting because hm does not take duplicates and want to keep track of common anagramss
        sorted_element = ''.join(sorted(element))
        # If the sorted element does not exist in the hashmap, create a key-value pair
        # Where the key will be the sorted element, and the value will be an intitiated array of the current iterated element
        if sorted_element not in hm:
            hm[sorted_element] = [element]
        # Else if the sorted element already exists within the hm as key, append the iterated elemnt to the values array
        else:
            hm[sorted_element].append(element)
    # Create an empty array that will be appended to with the final answer
    final_answer = []
    # Iterate through the now-populated hm and append value arrays to the final_answer array
    for key, value in hm.items():
        final_answer.append(value)
    return final_answer

print(groupAnagram(strs))