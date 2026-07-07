class Solution:
    def minOperations(self, s: str) -> int:
        left=0
        right=0
        temp=list(s)
        l=len(temp)
        for i in range(l-1):
            if temp[i]==temp[i+1]:
                temp[i+1]="0" if temp[i]=="1" else "1"
                right+=1
        return min(l-right,right)
        

            

        