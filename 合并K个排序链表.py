from typing import List
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
    
    def divideList(self, lists: List[ListNode], left:int, right:int) -> ListNode:
        if left > right:
            return None
        elif left == right:
            return lists[left]
        mid = (int)((left + right)/2)
        #递归实现分割合并
        return self.Merge(self.divideList(lists, left, mid), self.divideList(lists, mid + 1, right))
    
    def mergeKLists(self , lists: List[ListNode]) -> ListNode:
        
        return self.divideList(lists, 0, len(lists) - 1)
    
    # 链表构建辅助函数
def build_linkedlist(arr):
    dummy = ListNode(-1)
    cur = dummy
    for num in arr:
        cur.next = ListNode(num)
        cur = cur.next
    return dummy.next

# 链表打印函数
def print_list(node):
    res = []
    while node:
        res.append(str(node.val))
        node = node.next
    print(" → ".join(res))

if __name__ == "__main__":
    # 创建测试链表
    list1 = build_linkedlist([1, 4, 5])
    list2 = build_linkedlist([2, 6])
    list3 = build_linkedlist([3, 7])
    
    # 显示输入链表
    print("输入链表:")
    print("List1:", end=" "); print_list(list1)
    print("List2:", end=" "); print_list(list2)
    print("List3:", end=" "); print_list(list3)
    
    # 执行合并操作
    sol = Solution()
    merged = sol.mergeKLists([list1, list2, list3])
    
    # 显示输出结果
    print("\n合并结果:")
    print_list(merged)