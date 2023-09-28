class Solution:
    # def decodeAtIndex(self, s: str, k: int) -> str:
    #     ans = ""
    #     for i in range(len(s)):
    #         if(len(ans)>=k):
    #             return ans[k-1]
    #         if(s[i].isdigit()):
    #             ans+=ans*(int(s[i])-1)
    #         else:
    #             ans+=s[i]
    #     return ans[k-1]
    def decodeAtIndex(self, S, K):
        N = 0
        for i, c in enumerate(S):
            N = N * int(c) if c.isdigit() else N + 1
            if K <= N: break
        for j in range(i, -1, -1):
            c = S[j]
            if c.isdigit():
                N /= int(c)
                K %= N
            else:
                if K == N or K == 0: return c
                N -= 1