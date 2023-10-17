class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if(rowIndex==0):
            return [1]
        ans = [1]*(rowIndex+1)
        for i in range(1,rowIndex+1):
            temp=ans[0:i+1]
            for j in range(1,i):
                ans[j]=temp[j]+temp[j-1]
        return ans
        # ans = [0]*(rowIndex+1)
        # ans[0]=1
        # for i in range(1,rowIndex+1):
        #     for j in range(i,0,-1):
        #         ans[j]=ans[j]+ans[j-1]
        # return ans
        
            
        