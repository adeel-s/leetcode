'''
===#567 Permutation in String===
-Input:
    str s1: a string I need to look for a permutation of in s2
    str s2: a string
        len(s1) and len(s2) are between 1 and 1000
-Output
    bool result: whether a permuation of s1 occurs in s2

-Observations:
    * If s1 was ever longer than s2, we could return false immediately
    * I can slide a window of len(s1) across s2 and check if the letter frequency is the same.
        * If it ever is, return True
            Otherwise return false
    * Proposal:
        lp = 0
        rp = len(s1) - 1
        frequency array for s1 and s2
        for the length of s2, - len(s1) + 1:
            generate frequency array for s2
            if same as for s1
                return true
        return false

'''

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lp = 0
        rp = len(s1)
        s1Letters, s2Letters = [0] * 26, [0] * 26

        for c in s1:
            s1Letters[ord(c) - 97] += 1
            
        for i in range(len(s2) - len(s1) + 1):
            for c in s2[lp+i:rp+i]:
                s2Letters[ord(c) - 97] += 1
            if s1Letters == s2Letters:
                return True
            s2Letters = [0] * 26
        return False
