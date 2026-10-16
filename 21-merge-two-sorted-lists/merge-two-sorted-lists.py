# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        if not l1:
            return l2
        if not l2:
            return l1
        if not l1 and not l2:
            return None
        i, j = l1, l2
        temp = ListNode()
        h = temp
        while i != None and j != None:
            if i.val <= j.val:
                temp.next = i
                i = i.next
            else:
                temp.next = j
                j = j.next
            temp = temp.next
        if i != None:
            temp.next = i
        if j != None:
            temp.next = j
        return h.next