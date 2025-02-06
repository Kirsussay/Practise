class ListNode:
    def __init__(self,x):
       self.val = x
       self.next = None
class solution:
    def reverseBetween(self , head: ListNode, m: int, n: int) -> ListNode:
        res = ListNode(-1)
        res.next = head
        pre = res
        cur = head
        i : int = 1
        while i < m:
            pre = cur
            cur = cur.next
            i = 1 + i
        j : int = m
        while j < n:
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
            j = j+1
        return res.next

        

        