class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def LastNode(self,head:ListNode,k:int) ->ListNode:
        fast = head
        slow = head
        if head == None:
            return head
        for i in range(0,k):
            fast = fast.next
        while fast:
            fast = fast.next
            slow = slow.next
        return slow
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

    solution = Solution()
    Test = solution.LastNode(pHead1,2)
    printList(Test)


        
