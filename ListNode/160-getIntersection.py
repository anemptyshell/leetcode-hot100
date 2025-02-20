from typing import Optional

## 定义链表
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

## 初始化两个指针 pA 和 pB 分别指向链表 A 和链表 B 的头节点。
## 然后同时遍历两个链表，当 pA 到达链表 A 的末尾时，将其指向链表 B 的头节点；
## 当 pB 到达链表 B 的末尾时，将其指向链表 A 的头节点。这样，两个指针走过的总路程是相等的。
## 如果两个链表相交，那么在某一时刻，pA 和 pB 会指向同一个节点，该节点就是相交的起始节点；
## 如果两个链表不相交，那么最终 pA 和 pB 都会同时指向 None。
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode :

        currA = headA
        currB = headB

        # 处理边缘情况
        if not headA or not headB:
            return None

        while currA != currB:

            # currA = currA.next
            # currB = currB.next
            # if currA.next == None:
            #     currA = headB
            # if currB.next == None:
            #     currB = headA
            ## 上面条件判断有误，会导致跳过最后一个节点，应该在指针到达链表末尾进行重置
            
            # 移动 currA 指针
            currA = currA.next if currA else headB
            # 移动 currB 指针
            currB = currB.next if currB else headA
        
        return currA
    ## 跳出while循环：AB两链表都遍历完后，指针都为None，循环终止
        
# 创建相交链表示例
# 公共部分
common = ListNode(8)
common.next = ListNode(4)
common.next.next = ListNode(5)

# 链表 A
headA = ListNode(4)
headA.next = ListNode(1)
headA.next.next = common

# 链表 B
headB = ListNode(5)
headB.next = ListNode(6)
headB.next.next = ListNode(1)
headB.next.next.next = common

solution = Solution()
intersection = solution.getIntersectionNode(headA, headB)
if intersection:
    print(f"相交节点的值为: {intersection.val}")
else:
    print("两个链表没有交点")