
from typing import Optional

# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # dummyhead: Optional[ListNode]
        # dummyhead.next = head
        # 上面虚拟头节点初始化错误

        # 创建虚拟头部节点以简化删除过程
        dummyhead = ListNode(next = head)

        curr = dummyhead
        while curr.next != None:
            if curr.next.val == val:
                curr.next = curr.next.next
               
            else:
                curr = curr.next
        
        return dummyhead.next
