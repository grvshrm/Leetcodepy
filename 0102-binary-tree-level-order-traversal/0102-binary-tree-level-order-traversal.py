# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levelOrder = []
        levelQ = []
        levelQ.append(root)
        while levelQ:
            levelList = []
            for i in range(len(levelQ)):
                cur = levelQ.pop(0)
                levelList.append(cur.val)
                if cur.left:
                    levelQ.append(cur.left)
                if cur.right:
                    levelQ.append(cur.right) 
            levelOrder.append(levelList)
        return levelOrder