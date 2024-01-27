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
            curMin = levelQ[0][1]
            for i in range(size):
                cur, indx = levelQ.pop(0)
                cur_id = indx - curMin
                if i == 0:
                    left_indx = cur_id
                if i == size - 1:
                    right_indx = cur_id
                if cur.left:
                    levelQ.append([cur.left, 2 * cur_id + 1])
                if cur.right:
                    levelQ.append([cur.right, 2 * cur_id + 2])
            ans = max(ans, right_indx - left_indx + 1)
        return ans