from typing import Optional

# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 只要有环，指针就出不去，总不能让指针一直在环里循环？
## 把环类比为操场，让一快一慢指针
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        # 阶段一：判断链表是否有环
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # 如果快指针追上慢指针，说明有环
            if slow == fast:
                break
        # 如果没有环，返回 None
        if not fast or not fast.next:
            return None
        # 阶段二：找出环的入口节点
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

## 时间 O(n)  空间 O(1)
            
# 创建有环的链表
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1  # 形成环

solution = Solution()
entry_node = solution.detectCycle(head)
if entry_node:
    print(f"环的入口节点的值为: {entry_node.val}")
else:
    print("链表中没有环")