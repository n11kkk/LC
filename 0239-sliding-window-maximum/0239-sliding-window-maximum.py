from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], slw: int) -> List[int]:
        deq = deque()
        ans=[]
        for i in range(len(nums)):
            
            while(deq and nums[deq[-1]]<=nums[i]):
                deq.pop()
            
            deq+=[i]
            
            if(i-deq[0]>=slw):
                deq.popleft()
            
            if(i>=slw-1):
                ans.append(nums[deq[0]])
        return ans