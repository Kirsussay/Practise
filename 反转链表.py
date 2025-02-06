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


# 辅助函数：打印链表
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")
        # 测试用例
if __name__ == "__main__":
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # 打印原始链表
    print("原始链表：")
    printList(head)

    # 调用方法反转区间 [2, 4]
    solution = Solution()
    new_head = solution.ReverseList(head)

    # 打印反转后的链表
    print("反转区间 [2, 4] 后的链表：")
    printList(new_head)
