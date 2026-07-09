# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = l1
        num2 = l2
        result_head = ListNode()
        result = result_head
        c = 0
        while num1 or num2:
            if not num1:
                num1_val = 0
            else:
                num1_val = num1.val
            
            if not num2:
                num2_val = 0
            else:
                num2_val = num2.val

            s = num1_val + num2_val + c
            d = s%10
            c = s//10
            result.next = ListNode(d)
            result = result.next
            if num1:
                num1 = num1.next
            if num2:
                num2 = num2.next
            
        if c:
            result.next = ListNode(c)
        
        return result_head.next
