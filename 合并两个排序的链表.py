class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None


class Solution:
    def Merge(self, pHead1:ListNode, pHead2:ListNode)->ListNode:
        res =ListNode(-1)
        pre = res
        cur1 = pHead1
        cur2 = pHead2
        
        while cur1 and cur2:
            if cur1.val <= cur2.val:
                pre.next = cur1
                cur1 = cur1.next
            else:
                pre.next = cur2
                cur2 = cur2.next
            pre = pre.next
        if cur1:
            pre.next = cur1
        elif cur2:
            pre.next = cur2
        return res.next


# 辅助函数：打印链表
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
        # 测试用例
if __name__ == "__main__":
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    pHead1 = ListNode(1)
    pHead1.next = ListNode(3)
    pHead1.next.next = ListNode(5)
    pHead1.next.next.next = ListNode(7)
    pHead1.next.next.next.next = ListNode(9)


    pHead2 = ListNode(2)
    pHead2.next = ListNode(4)
    pHead2.next.next = ListNode(4.5)
    pHead2.next.next.next = ListNode(7)
    pHead2.next.next.next.next = ListNode(8)
    pHead2.next.next.next.next.next = ListNode(10)

    # 打印原始链表
    print("原始链表：")
    printList(pHead1)
    printList(pHead2)

    # 调用方法
    solution = Solution()
    new_head = solution.Merge(pHead1,pHead2)

    # 打印链表
    print("合并后的链表：")
    printList(new_head)


                
                

