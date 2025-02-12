class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:

    
    def addList(self, pHead1:ListNode,pHead2:ListNode)->ListNode:
        dummy = ListNode(-1)
        newHead1 = ReverseList(pHead1)
        newHead2 = ReverseList(pHead2)
        sum : int = 0
        tem : int = 0
        while(newHead1 != None or newHead2 != None):
            sum = tem
            if newHead1 != None:
                sum += newHead1.val
                newHead1 = newHead1.next
            if newHead2 != None:
                sum += newHead2.val
                newHead2 = newHead2.next

            #创建结点
            node = ListNode(sum%10)
            tem = int(sum / 10)
            node.next = dummy.next
            dummy.next = node

        if tem > 0:
            node = ListNode(tem)
            node.next = dummy.next
            dummy.next = node
        return dummy.next
    
# 辅助函数：打印链表
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")



def ReverseList(head:ListNode) ->ListNode:
    prev = None
    current = head
    while current != None:
        temp = current.next
        current.next = prev
        prev = current
        current = temp
    return prev

if __name__ == "__main__":
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    pHead1 = ListNode(1)
    pHead1.next = ListNode(3)
    pHead1.next.next = ListNode(5)
    pHead1.next.next.next = ListNode(7)
    pHead1.next.next.next.next = ListNode(9)


    pHead2 = ListNode(2)
    pHead2.next = ListNode(4)
    pHead2.next.next = ListNode(4)
    pHead2.next.next.next = ListNode(7)
    pHead2.next.next.next.next = ListNode(8)

    # 打印原始链表
    print("原始链表：")
    printList(pHead1)
    printList(pHead2)

    # 调用方法
    solution = Solution()
    new_head = solution.addList(pHead1,pHead2)

    # 打印链表
    print("合并后的链表：")
    printList(new_head)



