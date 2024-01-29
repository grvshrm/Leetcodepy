# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseUtil(cur, prev):
            if cur is None:
                return prev
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            return reverseUtil(cur, prev)
        head = reverseUtil(head, None)
        return head