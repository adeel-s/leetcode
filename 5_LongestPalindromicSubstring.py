'''
===#5 Longest Palindromic Substring===

-Input
    str s: a string to search for palindromes within
        len(s) is between 1 and 1000
        s contains only digits and English letters

-Output
    str result: the longest palindromic substring in s
    There can be more than one valid answer

-Complixity
    O(n^2) time
    O(1) space (not including result)

-Observations
    * Brute force: every substring: O(n^2)*checking if palindrome: O(n) = O(n^3)
    * If I find a palindrome in s, adding the next letter could not be another palindrome
        Unless the palindrome was all the same letter
    * Two pointers doesn't work because I don't know if all of s will be a palindrome until
        I check every letter with every other letter
    * Palindromes can be "unpeeled" - if I take a letter off either end, it must still
        be a palindrome
        This is where the dp comes in
    * Proposal:
        For every letter in s:
            best = that letter
            while if i+/- 1 are valid indices and characters are equal:
                best = initial letter + 2 letters
            update result

    * This only works for odd-length palindromes...
        I could do this three times for each letter:
        Once with just the letter
        Once with its left neighbor
        Once with its right neighbor
        Or each loop iteration checks both and adds only the one that works?
        Actually, just doing it with the right neighbor works.
            The left neighbor is covered in the previous iteration
    

    
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        result = ""
        for i in range(len(s)):
            lp, rp = i, i
            # Check odd-length palindromes
            while lp > -1 and rp < len(s) and s[lp] == s[rp]:
                pal = s[lp:rp+1]
                result = pal if len(pal) > len(result) else result
                lp -= 1
                rp += 1
            # Check even=length palindromes
            lp, rp = i, i + 1
            while lp > -1 and rp < len(s) and s[lp] == s[rp]:
                pal = s[lp:rp+1]
                result = pal if len(pal) > len(result) else result
                lp -= 1
                rp += 1

        return result

        