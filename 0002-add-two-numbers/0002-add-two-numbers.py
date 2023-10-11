# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = l1
        head2 = l2
        carry = 0
        head3 = ListNode()
        head4 = head3
        while(head1 and head2):
            summ = head1.val+head2.val+carry
            toAdd = summ%10
            summ//=10
            carry = summ
            head3.next = ListNode(val=toAdd)
            head3 = head3.next
            head1 = head1.next
            head2 = head2.next
        # print(head1,head2)
        while(head1 is not None):
            summ = head1.val+carry
            toAdd = summ%10
            summ//=10
            carry = summ
            head3.next = ListNode(val = toAdd)
            head1 = head1.next
            head3 = head3.next
        while(head2 is not None):
            summ = head2.val+carry
            toAdd = summ%10
            summ//=10
            carry = summ
            head3.next = ListNode(val = toAdd)
            head2 = head2.next
            head3 = head3.next
        if(carry!=0):
            head3.next = ListNode(val = carry)
        return head4.next
            
            
        