class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dp = [[0.0 for i in range(query_row+2)] for j in range(query_row+2)]
        dp[0][0] = float(poured)
        for i in range(query_row+1):
            for j in range(i+1):
                if(dp[i][j]>1):
                    dp[i+1][j] += (dp[i][j]-1)/2.0
                    dp[i+1][j+1] += (dp[i][j]-1)/2.0
        # print(dp[1],dp[query_row],dp[query_row-1])
        return min(dp[query_row][query_glass],1)
                    
                
            