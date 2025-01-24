'''
===#49 Group Anagrams===
-Input
    List[str] strs: a list of strings
        len(strs) is between 1 and 1000
        len(strs[i]) is between 0-100
        strs[i] is made up of lowercase english letters
-Output
    List[List[str]] result: strings from strs grouped by anagrams

-Complexity
    O(mn) time
    O(m) space
    m is the number of strings 
    n is the length of the longest string

-Observations
    * I can create a frequency array for each word in strs
        * Matching frequency arrays represent one class of anagram
        * Key:Values → frequency arrays:corresponding strings
        * return the values of the dictionary
'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        anagrams = defaultdict(list) #new dictionary for frequency:wordList pairs. defultdict because if a key doesn't exist, it returns an empty list, which we append to to create a new pair
        for s in strs: # for each string in .strs
            letters = [0] * 26 # new array for counting letter frequencies
            for c in s: # for each character in .s
                letters[ord(c) - ord("a")] += 1 # increment the letter count by 1

            anagrams[tuple(letters)].append(s) # add or append to the list for the given key

        return anagrams.values() # return the values of the dictionary
        