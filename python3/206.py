# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        if head is None:
            return None

        previous = head
        head = head.next
        previous.next = None

        while head is not None:
            next_temp = head.next
            head.next = previous
            previous = head
            head = next_temp

        return previous


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


l = makeListNode([1])
s = Solution()
t = s.reverseList(l)
printListNode(t)
