class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if(len(s)<=0):
            return True
        if(len(t)<=0 or len(t)<len(s)):
            return False
        j=0
        lenS=len(s)
        for i in t:
            if(j>lenS-1):
                return True
            if(i==s[j]):
                j+=1
        if(j>lenS-1):
            return True
        return False