# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:

        orders = []

        self.midOrder(orders, root)

        for i in range(1, len(orders)):
            if orders[i] <= orders[i - 1]:
                return False

        return True

    def midOrder(self, order_list: [int], root: TreeNode):
        if root is not None:
            self.midOrder(order_list, root.left)
            order_list.append(root.val)
            self.midOrder(order_list, root.right)

