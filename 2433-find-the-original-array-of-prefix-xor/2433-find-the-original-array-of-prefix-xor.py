class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        l=list()
        l.append(pref[0])
        for idx in range(1,len(pref)):
            l.append(pref[idx-1]^pref[idx])
        return l