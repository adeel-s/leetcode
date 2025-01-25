
'''
===Encode and Decode Strings===
Design one method to encode and another method to decode strings
Encode method
-Input
    List[str]: a list of strings to encode into one string
-Output 
    str: an encoded string
Decode method
-Input
    str: an encoded string
-Output 
    List[str]: a list of strings to encode into one string
Solution: Use a compound delimiter
    A blind delimiter could be confused with the same delimiting string appearing in
    .strs
    With an accompanying length, the decode method knows the end of the next string,
    "handshaking" its way down the encoded string
    Thus, the delimiter is a combination of the length of the next string 
        and a delimiting character, in this case, '#'
    *Encode:
    for every string in .strs, append its length and the '#' character to .str
    *Decode:
    while s isn't an empty string
    partition s on #
    [0] is the length of the next list item
    [1] is the '#'
    [2] is the remaining string
    s = [2]
    strs.append(s[:[0]])
    remove the next [0] from s
'''
class Solution:
    def encode(self, strs: List[str]) -> str: 
        result = ""
        for s in strs:
            result += (str(len(s)) + "#" + s)
        return result
        
    def decode(self, s: str) -> List[str]:
        strs = []
        while not s == "":
            part = s.partition("#")
            s = part[2]
            strs.append(s[:int(part[0])])
            s = s[int(part[0]):]
        return strs
        
