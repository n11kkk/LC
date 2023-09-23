# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        d={}
        while(headA!=None):
            d[headA]=True
            headA=headA.next
        while(headB!=None):
            if(headB in d):
                return headB
            else:
                headB=headB.next
        return headB