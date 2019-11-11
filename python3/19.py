# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        length = 0
        temp_head = head
        while temp_head is not None:
            length += 1
            temp_head = temp_head.next

        temp_head = head
        remove_index = length - n
        current_index = 0

        if length == 0:
            return None

        if length == 0 and remove_index == 0:
            return None

        if remove_index == 0:
            head = head.next
            temp_head.next = None

        provious = temp_head
        temp_head = temp_head.next
        current_index += 1

        while temp_head is not None:
            if current_index == remove_index:
                provious.next = temp_head.next
                temp_head.next = None
                break
            provious = temp_head
            temp_head = temp_head.next
            current_index += 1

        return head


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


l = makeListNode([1, 2, 3, 4, 5])
s = Solution()
t = s.removeNthFromEnd(l, 2)
printListNode(t)
