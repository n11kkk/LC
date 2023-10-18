class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        nums1d = {}
        nums2d = {}
        for i,num in enumerate(nums1):
            nums1d[num] = nums1d.get(num,0)+1
        for i,num in enumerate(nums2):
            nums2d[num] = nums2d.get(num,0)+1
        for i in nums1:
            if(nums2d.get(i) is not None and nums2d.get(i)>0):
                ans.append(i)
                nums2d[i]-=1
        return ans