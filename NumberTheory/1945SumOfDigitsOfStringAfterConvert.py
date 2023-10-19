"""
You are given the a string s consisting of lowercase English letters, and an integer k.

First, convert s into an integer by replacing each letter with its position in the alphabet.
eg: a = 1, b = 2, c = 3 ... z = 26

Then, transform the integer by replacing it with the sum of its digits. Repeat the transform operation k
times in total.

For example, if s = "zbax" and k = 2, then the resulting integer would be 8 by the following operations:
- Convert: "zbax" ➝ "(26)(2)(1)(24)" ➝ "262124" ➝ 262124
- Transform #1: 262124 ➝ 2 + 6 + 2 + 1 + 2 + 4 ➝ 17
- Transform #2: 17 ➝ 1 + 7 ➝ 8

Return the resulting integer after performing the operations described above.


Example 1:
Input: s = "iiii", k = 1
Output: 36
Explanation: The operations are as follows:
- Convert: "iiii" ➝ "(9)(9)(9)(9)" ➝ "9999" ➝ 9999
- Transform #1: 9999 ➝ 9 + 9 + 9 + 9 ➝ 36
Thus the resulting integer is 36.


Example 2:
Input: s = "leetcode", k = 2
Output: 6
Explanation: The operations are as follows:
- Convert: "leetcode" ➝ "(12)(5)(5)(20)(3)(15)(4)(5)" ➝ "12552031545" ➝ 12552031545
- Transform #1: 12552031545 ➝ 1 + 2 + 5 + 5 + 2 + 0 + 3 + 1 + 5 + 4 + 5 ➝ 33
- Transform #2: 33 ➝ 3 + 3 ➝ 6
Thus the resulting integer is 6.


Example 3:
Input: s = "zbax", k = 2
Output: 8
"""


def getLucky(s, k):
    dic = {
        "a": "1",
        "b": "2",
        "c": "3",
        "d": "4",
        "e": "5",
        "f": "6",
        "g": "7",
        "h": "8",
        "i": "9",
        "j": "10",
        "k": "11",
        "l": "12",
        "m": "13",
        "n": "14",
        "o": "15",
        "p": "16",
        "q": "17",
        "r": "18",
        "s": "19",
        "t": "20",
        "u": "21",
        "v": "22",
        "w": "23",
        "x": "24",
        "y": "25",
        "z": "26",
    }

    string = ""
    count = 0
    # keep in mind that a string is an iterable, so we will need to use the hm above to match each element of the string
    for i in range(len(s)):
        string += dic[s[i]]
    for i in range(len(string)):
        count += int(string[i])
    k = k - 1
    while k > 0:
        count_str = str(count)
        count = 0
        for i in range(len(count_str)):
            count += int(count_str[i])
        k = k - 1
    return count


print(getLucky("zbax", 2))
