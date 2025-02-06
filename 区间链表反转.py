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
        #循环找到区间左起点
        i : int = 1
        while i < m:
            pre = cur
            cur = cur.next
            i = 1 + i
        #算法实现
        j : int = m
        while j < n:
            temp = cur.next
            cur.next = temp.next
            temp.next = pre.next
            pre.next = temp
            j = j+1
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
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)

    # 打印原始链表
    print("原始链表：")
    printList(head)

    # 调用方法反转区间 [2, 4]
    solution = solution()
    new_head = solution.reverseBetween(head, 2, 4)

    # 打印反转后的链表
    print("反转区间 [2, 4] 后的链表：")
    printList(new_head)
     