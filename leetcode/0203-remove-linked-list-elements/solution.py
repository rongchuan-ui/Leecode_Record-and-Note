# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        while head:
            if head.val==val:
                head=head.next
            else:
                break
        cur=head
        while cur:
            while cur.next and cur.next.val == val:
                cur.next=cur.next.next
            cur=cur.next
        return head
