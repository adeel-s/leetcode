'''
===139. Word Break===

-Input
    str s: a target string to make out of words in wordDict
        len(s) is between 1 and 200
    List[str] wordDict: a dictionary of strings
        len(wordDict) is between 1 and 100
        wordDict[i] is between 1 and 20
    all input characters are lowercase English letters

-Output
    bool result: whether s can be formed from words in wordDict

-Complexity
    O(n*m*t) time - n=len(s) m=len(wordDict), t=len(wordDict[i])
    O(n) space

-Observations
    * A brute force approach would try recursively match words in wordDict with
        letters in s. On a match, pass the remaining portion of s and wordDict to
        the next recursive call. This is something like O(n^m)
    * How does having n space reduce the problem?
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        result = [False] * (len(s) + 1)

        result[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and s[i:i+len(w)] == w:
                    result[i] = result[i+len(w)]
                if result[i]:
                    break

        return result[0]
        