class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#
# 
# @param pHead1 ListNode类 
# @param pHead2 ListNode类 
# @return ListNode类
#
class Solution:
    def FindFirstCommonNode(self , pHead1 , pHead2 ):
        # write code here
        a = pHead1
        b = pHead2
        # 当两者相同则是第一个公共节点
        while a!=b:
            # a从pHead1遍历完再遍历pHead2
            a = a.next #if a else pHead2
            if a == None:
                a = pHead2
            # b从pHead2遍历完再遍历pHead1
            b = b.next #if b else pHead1
            if b == None:
                b = pHead1
            print(a,b)
            
        return a

            
# 辅助函数：打印链表
def printList(head):
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

        # 测试用例
if __name__ == "__main__":
    # 创建链表 1 -> 2 -> 3 -> 4 -> 5
    # 创建公共尾部节点
    common_tail = ListNode(7)
    common_tail.next = ListNode(9)

# 构造链表1：1->3->5->公共尾部
    pHead1 = ListNode(1)
    pHead1.next = ListNode(3)
    pHead1.next.next = ListNode(5)
    pHead1.next.next.next = common_tail  # 指向公共节点

# 构造链表2：2->4->公共尾部
    pHead2 = ListNode(2)
    pHead2.next = ListNode(4)
    pHead2.next.next = common_tail  # 指向同一个公共节点


    # 打印原始链表
    print("原始链表：")
    printList(pHead1)
    printList(pHead2)

    # 调用方法
    solution = Solution()
    new_head = solution.FindFirstCommonNode(pHead1,pHead2)

    # 打印链表
    print("合并后的链表：")
    printList(new_head)