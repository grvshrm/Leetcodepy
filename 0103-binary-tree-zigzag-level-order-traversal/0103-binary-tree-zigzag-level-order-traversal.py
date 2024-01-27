# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        levelOrder = []
        levelQ = [root]
        lToR = True
        while levelQ:
            levelList = []
            for i in range(len(levelQ)):
                cur = levelQ.pop(0)
                if cur.left:
                    levelQ.append(cur.left)
                if cur.right:
                    levelQ.append(cur.right)
                levelList.append(cur.val)
            levelList = levelList if lToR else levelList[::-1]
            levelOrder.append(levelList)
            lToR = not lToR
        return levelOrder
                    
            