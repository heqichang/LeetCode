# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        result = []
        temp = []

        def preOrder(node: TreeNode, num: int, stack: [int]):
            stack.append(node.val)
            if node.left is None and node.right is None:
                if num - node.val == 0:
                    result.append(stack.copy())
            else:
                if node.left:
                    preOrder(node.left, num - node.val, stack)
                if node.right:
                    preOrder(node.right, num - node.val, stack)

            stack.pop()

        if root:
            preOrder(root, sum, temp)
        return result

# 1 遍历树，升一个 level ，入一个栈，回一个 level，出一个栈
