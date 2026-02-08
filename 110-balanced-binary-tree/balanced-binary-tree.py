# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        is_bal = True
        def height(node: TreeNode) -> int:
            nonlocal is_bal
            if node is None:
                return 0
            left_ht = height(node.left)
            right_ht = height(node.right)
            if abs(left_ht - right_ht) > 1:
                is_bal = False
            return 1 + max(left_ht, right_ht)
        tree_height = height(root)
        return is_bal
