from typing import Optional

# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# 反转链表
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # curr1 = head
        # while curr1 == None:
        #     return curr1
        # res = ListNode(val=curr1.val)
        # while curr1.next:
        #     curr1 = curr1.next
        #     curr2 = ListNode(val=curr1.val, next=res)
        #     res = curr2

        # return res

        """空间复杂度为 O(n) """
        # curr = head
        # res = None
        # while curr:
        #     res = ListNode(val=curr.val, next=res)
        #     curr = curr.next
        # return res

        """通过在原链表上直接修改指针的方式，将空间复杂度优化为 O(1)"""
        # 初始化前一个节点为 None
        prev = None
        # 当前节点指向头节点
        curr = head
        while curr:
            # 保存当前节点的下一个节点
            next_node = curr.next
            # 将当前节点的 next 指针指向前一个节点
            curr.next = prev
            # 更新前一个节点为当前节点
            prev = curr
            # 更新当前节点为下一个节点
            curr = next_node
        # 最终 prev 指向反转后的链表头节点
        return prev








