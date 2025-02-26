'''
===#647 Palindromic Substrings===

-Input
    str s: a string of lowercase English letters
    len(s) is between 1 and 1000
-Output
    int result: the number of substrings in s that are palindromes

-Complexity
    O(n^2) time
    O(1) space

-Observations
    * If s = "ss", the problem states that "s" and "s" are distinct palindromes within s
    * Proposal:
        for each letter in s:
            add to result list
            for each letter after the first letter:
                add to substr
                check if it's a palindrome/add or not to result

        This is n^3: nested for-loop is n^2 and palindrome check is n
    * Check each letter as the center of a palindrome
    * Proposal
        For each letter in s:
            result += 1
            while the letter has neighbors:
                if neighbors are equal, result += 1
                else: continue
            Also add right neighbor and run again

-Solution
    result = len(s)
    for i in range(len(s)):
        j = 1
        while i-j > -1 and i+j < len(s):
            if s[i+j] == s[i-j]:
                result += 1
            j += 1
        if i+1 < len(s) and s[i] == s[i+1]:
            j = 1
            k = 2
            while i-j > -1 and i+k < len(s):
                if s[i-j] == s[i+k]:
                    result += 1
                j += 1
                k += 1
    return result

'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        result = len(s)
        for i in range(len(s)):
            j = 1
            while i-j > -1 and i+j < len(s) and s[i+j] == s[i-j]:
                result += 1
                j += 1
            if i+1 < len(s) and s[i] == s[i+1]:
                result += 1
                j = 1
                k = 2
                while i-j > -1 and i+k < len(s) and s[i-j] == s[i+k]:
                    result += 1
                    j += 1
                    k += 1
        return result
        