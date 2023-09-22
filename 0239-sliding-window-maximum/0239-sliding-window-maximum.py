from collections import deque
# from queue import PriorityQueue  
class Solution:
    def maxSlidingWindow(self, nums: List[int], slw: int) -> List[int]:
        # def getLast(prq,slw):
        #     count = 0
        #     prq1 = PriorityQueue()
        #     while(count<slw-1):
        #         toAdd = prq.get()[1]
        #         prq1.put((-toAdd,toAdd))
        #         count+=1
        #     return prq1
        # prq = PriorityQueue()
        # ans = []
        # for i in range(len(nums)):
        #     prq.put((-nums[i],nums[i]))
        #     if(prq.qsize()>=slw):
        #         anss = prq.get()[1]
        #         # print(prq)
        #         ans.append(anss)
        #         prq.put((-anss,anss))
        #         prq = getLast(prq,slw)
        # return ans
                
                
            
        
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

        
    
