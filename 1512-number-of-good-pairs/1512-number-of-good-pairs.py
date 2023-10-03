import math
class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        # ans = 0
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if(nums[i]==nums[j]):
        #             ans+=1
        # return ans
        counts  = {}
        for i in nums:
            if(counts.get(i) is not None):
                counts[i]+=1
            else:
                counts[i] = 1
        ans = 0
        for i in counts.values():
            if(i>=2):
                ans+=math.comb(i,2)
        return ans