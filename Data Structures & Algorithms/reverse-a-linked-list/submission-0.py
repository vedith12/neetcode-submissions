# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        first, second = None, None
        curr = head
        while curr!= None:
            second = curr.next
            curr.next = first
            first = curr
            curr = second
        return first