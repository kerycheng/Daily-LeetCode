# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        first = res = head
        while first and first.next!=None:
            first = first.next.next
            res = res.next
        else:
            return res