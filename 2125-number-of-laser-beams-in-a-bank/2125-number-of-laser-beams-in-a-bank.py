class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev_count = bank[0].count("1")
        for i in range(1,len(bank)):
            c = bank[i].count("1")
            ans+=c*prev_count
            if(c!=0):
                prev_count = c
        return ans
            