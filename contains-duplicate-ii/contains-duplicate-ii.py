class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = dict()
        for i in range(len(nums)):
            if(d.get(nums[i]) is not None):
                # print(d,nums[i],d[nums[i]],i,k,d[nums[i]]-i)
                if(i-d[nums[i]]<=k):
                    return True
                else:
                    d[nums[i]] = i
            else:
                d[nums[i]] = i
                # print(d)
                
        return False
                
            
            