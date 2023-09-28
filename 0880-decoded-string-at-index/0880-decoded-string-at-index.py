class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        currCount = 0
        for i in range(len(s)):
            if(s[i].isdigit()):
                currCount+=currCount*((int(s[i])-1))
            else:
                currCount+=1
        for i in range(len(s)-1,-1,-1):
            if(s[i].isdigit()):
                # print(currCount,k)
                currCount=currCount/int(s[i])
                k=k%currCount
                # print(currCount,k)
            else:
                if(currCount==k or k==0):
                    return s[i]
                currCount-=1