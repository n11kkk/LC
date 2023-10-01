class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                tot = 0
                if(grid[i][j]==1):
                    if(i+1<=len(grid)-1):
                        tot+=grid[i+1][j]
                    if(j+1<=len(grid[i])-1):
                        tot+=grid[i][j+1]
                    if(j-1>=0):
                        tot+=grid[i][j-1]
                    if(i-1>=0):
                        tot+=grid[i-1][j]
                    ans+=4-tot
        return ans  
                       
                        
        