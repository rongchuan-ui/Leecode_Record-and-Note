# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
    # whole logic: reverse the second part of linked list and compare the second part with the first part, if they are same, then return True
        # 1. Find the middle node - to distinguish second half and first half
        slow=head
        fast=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        if fast:
            slow=slow.next
        # 2. reverse the second half
        prev=None
        cur=slow
        while cur:
            nxt=cur.next
            cur.next=prev
            prev=cur
            cur=nxt
        # 3. Compare
        while head and prev:
            if prev.val==head.val:
                prev=prev.next
                head=head.next
            else:
                return False
        return True


