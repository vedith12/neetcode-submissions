class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        #trying to do in O(1)
        l = 0
        i = len(s)-1
        while s[i] == ' ':
            i-=1
        while i>=0 and s[i] != ' ':
            i-=1
            l+=1
        return l

    