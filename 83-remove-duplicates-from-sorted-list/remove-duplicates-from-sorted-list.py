# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        if not head or not head.next:
            return head
        temp = head
        last = head
        head = head.next
        while head is not None:
            print("Head", head.val)
            print("Last", last.val)
            if head.val != last.val:
                last.next = head
                last = last.next
            head = head.next
        last.next = None
        return temp
