class ListNode(object):
    """
    This class represents one node in a doubly linked list.
    """
    def __init__(self, val, nxt, prev):
        self.value=val
        self.next=nxt
        self.prev=prev

class MyLinkedList(object):
    """
    This class represents the whole linked list object.
    """
    def __init__(self):
        self.size=0
        self.head=ListNode(0,None,None)
        self.tail=ListNode(0,None,None)
        self.tail.prev=self.head
        self.head.next=self.tail
        
    def get(self, index):
        """
        :type index: int
        :rtype: int
        """
        i=0
        cur=self.head.next
        while cur != self.tail:
            if i==index:
                return cur.value
            else:
                cur=cur.next
                i+=1
        return -1

    def addAtHead(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur= ListNode(val,nxt=self.head.next, prev=self.head)
        self.head.next=cur
        cur.next.prev=cur
        self.size+=1
        return

    def addAtTail(self, val):
        """
        :type val: int
        :rtype: None
        """
        cur= ListNode(val,nxt=self.tail, prev=self.tail.prev)
        cur.prev.next=cur
        self.tail.prev=cur
        self.size+=1
        return

    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        cur=self.head.next
        i=0
        if index == 0:
            self.addAtHead(val)
            return
        if index == self.size:
            self.addAtTail(val)
            return
        if index >0 and index <self.size:
            while i <=index:
                if i==index:
                    cur = ListNode(val,nxt=cur, prev=cur.prev)
                    cur.next.prev=cur
                    cur.prev.next=cur
                    self.size+=1
                    break
                else:
                    cur=cur.next
                    i+=1
            return
        if index > self.size:
            return

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        cur=self.head.next
        i=0
        if index > self.size-1 or index<0:
            return
        if index<=self.size-1:
            while i <= index:
                if i == index:
                    cur.prev.next=cur.next
                    cur.next.prev=cur.prev
                    self.size-=1
                    break
                else:
                    cur=cur.next
                    i+=1
        return cur  
        
        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
