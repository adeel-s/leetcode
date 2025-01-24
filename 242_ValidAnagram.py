'''
===#242 Valid Anagram===
-Input
    str s: a string
    str t: another string
    both strings consist of lowercase English letters
-Output
    bool result: whether s and t are anagrams of each other

-Complexity
    O(n+m) time
    O(1) space
    n is the length of s
    m is the length of t

-Observations
    * I CAN create a set because the possible values for characters
        is bounded by the number of english letters
    * Proposal
        For each letter in s:   
            store letter:frequency in a dictionary
        For each letter in t:
            store letter_frequency in a dictionary
        compare dictionaries


'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = [0] * 26
        tLetters = [0] * 26

        for c in s:
            print(ord(c))
            sLetters[ord(c) - 97] += 1

        for c in t:
            tLetters[ord(c) - 97] += 1
        
        return sLetters == tLetters

        