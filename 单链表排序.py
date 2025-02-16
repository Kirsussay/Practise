class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

class Solution:
    def sort(self,left:ListNode,right:ListNode)->ListNode:
        head = ListNode(-1)
        res = head
        while left != None and right != None:
            if left.val < right.val:
                head.next = left
                left = left.next
            else:
                head.next = right
                right = right.next
            head = head.next
        head.next = left if left else right
        return res.next

    def sortInList(self,head:ListNode)->ListNode:
        if not head or not head.next:
            return head
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
        mid = slow.next
        slow.next = None
        left = self.sortInList(head)
        right = self.sortInList(mid)

        
        return self.sort(left,right)
# 构建测试链表
def build_list(arr):
    dummy = ListNode(-1)
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# 打印链表
def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print("->".join(res))

# 测试用例
test = [4, 2, 1, 3, 7, 6 ,9 ,0 ,5]
head = build_list(test)
print("原链表：", end="")
print_list(head)  # 4->2->1->3

sorted_head = Solution().sortInList(head)
print("排序后：", end="")
print_list(sorted_head)  # 1->2->3->4

        