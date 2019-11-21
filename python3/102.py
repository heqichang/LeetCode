# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        result = []

        if root:
            result.append([root.val])
            self.__level(root.left, 1, result)
            self.__level(root.right, 1, result)

        return result

    def __level(self, child: TreeNode, level: int, orders: List[List[int]]):

        if child:

            if level >= len(orders):
                orders.append([])

            self.__level(child.left, level + 1, orders)
            self.__level(child.right, level + 1, orders)

            orders[level].append(child.val)

