class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def ReverseList(self,head:ListNode) ->ListNode:
        prev = None
        current = head
        while current != None:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    

