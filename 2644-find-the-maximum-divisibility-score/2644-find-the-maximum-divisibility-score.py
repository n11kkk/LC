class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        maxDiv = 0
        maxDivEle = float('inf')
        for i in range(len(divisors)):
            curDiv = 0
            for j in range(len(nums)):
                if(nums[j]%divisors[i]==0):
                    curDiv+=1
            if(curDiv>maxDiv):
                maxDiv = curDiv
                maxDivEle = divisors[i]
            if(curDiv==maxDiv):
                if(maxDivEle>divisors[i]):
                    maxDivEle = divisors[i]
        return maxDivEle
        