from typing import Optional

# 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 两两交换链表中的节点
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummyhead = ListNode(next=head)
        curr = dummyhead

        while curr.next and curr.next.next:
            next1 = curr.next
            next2 = next1.next
            next3 = next2.next
    
            curr.next = next2
            next2.next = next1
            next1.next = next3

            # curr = next3 
            # 这一句不对，因为经过上面的步骤之后next123的位置都改变了
            curr = curr.next.next

        return dummyhead.next


# 创建链表 1 -> 2 -> 3 -> 4
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)

solution = Solution()
new_head = solution.swapPairs(head)

# 打印交换后的链表
current = new_head
while current:
    print(current.val, end=" -> " if current.next else "\n")
    current = current.next







