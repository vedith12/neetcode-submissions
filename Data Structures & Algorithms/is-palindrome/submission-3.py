class Solution:
    def isPalindrome(self, s: str) -> bool:
        arr = []

        for character in s:
            if character.isalnum():
                arr.append(character.lower())
        l = 0
        r = len(arr)-1
        while l<r:

            if arr[l] != arr[r]:
                return False
                break
            l+=1 
            r-=1
        else: 
            return True