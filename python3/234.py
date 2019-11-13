# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        length = 0
        temp = head

        while temp is not None:
            length += 1
            temp = temp.next

        if length == 0 or length == 1:
            return True

        right_start = int(length / 2)
        if length % 2 == 1:
            right_start += 1

        l = []
        index = 0
        temp = head
        while temp is not None:
            if index >= right_start:
                l.append(temp.val)
            temp = temp.next
            index += 1

        temp = head
        for i in range(len(l)):
            if temp.val != l.pop():
                return False
            temp = temp.next

        return True

# 1 先求长度, 截取后半段组链表入栈，再跟前半一个循环比较，如果中途不一样就是 false
# 2 求长度，一个指针先前进 一半，还有一个指针从头开始，比较两个指针值 (想错了，回文)
# 3 取出所有值转成 str , 比较 str == str.reverse (错误，有负数)

