from typing import Optional

## 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
## 删除链表的倒数第N个节点

## bugfree，但时间复杂度为O(m*n)，m是链表的长度，n是向后移动的节点数
# class Solution:
#     def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
#         dummyhead = ListNode(next=head)
#         curr = dummyhead

#         while curr:
#             curr1 = curr
  
#             for i in range(1, n+1):
#                 curr1 = curr1.next

#             if curr1.next == None:
#                 curr.next = curr.next.next
#                 return dummyhead.next
#             else:
#                 curr = curr.next

## 双指针法时间复杂度为O(m)       
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # 创建虚拟头节点
        dummy = ListNode(0, head)
        # 初始化两个指针
        fast = dummy
        slow = dummy

        # 先将 first 指针向前移动 n + 1 步
        for _ in range(n + 1):
            fast = fast.next

        # 同时移动 first 和 second 指针，直到 first 到达链表末尾
        while fast:
            fast = fast.next
            slow = slow.next

        # 删除倒数第 n 个节点
        slow.next = slow.next.next

        return dummy.next


# 创建链表 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
n = 2
new_head = solution.removeNthFromEnd(head, n)

# 打印删除节点后的链表
curr = new_head
while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next


