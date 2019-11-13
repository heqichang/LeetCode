# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        head = ListNode(0)
        temp = head

        while l1 is not None or l2 is not None:
            if l1 is not None and l2 is not None:
                if l1.val < l2.val:
                    temp.next = l1
                    l1 = l1.next
                    temp = temp.next
                else:
                    temp.next = l2
                    l2 = l2.next
                    temp = temp.next
            elif l1 is not None:
                temp.next = l1
                l1 = l1.next
                temp = temp.next
            else:
                temp.next = l2
                l2 = l2.next
                temp = temp.next

        return head.next


def makeListNode(list_nums: []) -> ListNode:
    temp_nums = list_nums
    temp_nums.reverse()

    head = None
    for i in range(len(temp_nums)):
        temp_node = ListNode(temp_nums[i])
        temp_node.next = head
        head = temp_node
    return head


def printListNode(head: ListNode):
    while head is not None:
        print(head.val)
        head = head.next


l11 = makeListNode([])
l22 = makeListNode([])
s = Solution()
t = s.mergeTwoLists(l11, l22)
printListNode(t)

# 1 同时遍历，比较两边大小，小的先入新的 listnode
