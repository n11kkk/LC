class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        n = 0
        # cost.append(0)
        for i in range(2,len(cost)):
            n=cost[i]+min(first,second)
            first = second
            second = n
        # print(first,second)
        return min(first,second)
            
        
                
        
                
        