class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def has_cycle(self,head:ListNode)->bool:
        visited = set()
        cur = head
        while cur:
            if cur in visited:
                print(cur.val)
                return True
            visited.add(cur)
            cur = cur.next
        return False
    
# ---------- 测试用例 ----------
# 构造有环链表 1->2->3->1（环）
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node1.next = node2
node2.next = node3
node3.next = node1  # 形成环
#创建实例
solution = Solution()
print(solution.has_cycle(node1))  # 输出 True

# 构造无环链表 4->5->6
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node4.next = node5
node5.next = node6
print(solution.has_cycle(node4))  # 输出 False