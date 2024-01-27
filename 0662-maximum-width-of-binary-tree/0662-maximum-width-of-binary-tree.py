# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        levelQ = []
        ans = 0
        levelQ.append([root, 0])
        while levelQ:
            left_indx, right_indx = 0, 0
            size = len(levelQ)
            for i in range(size):
                cur, cur_indx = levelQ.pop(0)
                if i == 0:
                    left_indx = cur_indx
                if i == size - 1:
                    right_indx = cur_indx
                if cur.left:
                    levelQ.append([cur.left, 2 * cur_indx + 1])
                if cur.right:
                    levelQ.append([cur.right, 2 * cur_indx + 2])
            ans = max(ans, right_indx - left_indx + 1)
        return ans