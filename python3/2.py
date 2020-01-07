# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        temp = head

        add = 0
        
        while l1 or l2:
            n1 = 0
            n2 = 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next

            n3 = n1 + n2 + add

            if n3 >= 10:
                n3 = n3 % 10
                add = 1
            else:
                add = 0

            temp.next = ListNode(n3)
            temp = temp.next

        if add == 1:
            temp.next = ListNode(1)

        return head.next
