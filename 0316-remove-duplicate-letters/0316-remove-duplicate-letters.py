class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        d = {}
        for i in range(len(s)):
            d[s[i]] = i
        stack = []
        v = set()
        for i in range(len(s)):
            if(s[i] not in v ):
                while(stack and s[i]<stack[-1] and i<d[stack[-1]]):
                    v.remove(stack.pop())
                v.add(s[i])
                stack.append(s[i])
        ans = ""
        for i in stack:
            ans+=i
        return ans
            