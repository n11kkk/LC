class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        # def calculate(n):
        #     if(n==1):
        #         return "0"
        #     else:
        #         ans = ""
        #         sol = calculate(n-1)
        #         for i in range(len(sol)):
        #             if(int(sol[i])==0):
        #                 ans+="01"
        #             if(int(sol[i])==1):
        #                 ans+="10"
        #         return ans 
        # sol = calculate(n)
        # return int(sol[k-1])
        ans = [0,1]
        row = n
        val = k
        toFind = k
        while(row>=2):
            maxEle = 2**(row-2)
            if(val>maxEle):
                if((val%maxEle)>maxEle//2):
                    toFind = (val%maxEle) - (maxEle//2)
                else:
                    toFind = maxEle//2 + (val%maxEle)
            else:
                toFind = val
            val = toFind
            row-=1
        return ans[toFind-1]
                    