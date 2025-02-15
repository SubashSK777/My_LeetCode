# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = end = None
        carry = 0
        while l1 or l2 or carry != 0:
            sum_val = carry
            if l1:
                sum_val += l1.val
                l1 = l1.next
            if l2:
                sum_val += l2.val
                l2 = l2.next

            newNode = ListNode(sum_val % 10)
            carry = sum_val // 10

            if res:
                end.next = newNode
                end = newNode

            else:
                res = end = newNode

        return res

            
        