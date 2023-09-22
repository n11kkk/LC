class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        newArr = nums1+nums2
        newArr.sort()
        # print(newArr)
        if(len(newArr)%2==0):
            return (newArr[len(newArr)//2-1]+newArr[len(newArr)//2])/2
        else:
            return newArr[len(newArr)//2]