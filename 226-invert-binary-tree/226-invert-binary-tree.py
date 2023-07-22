# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if(not root): 
            return None
        queue = list()
        queue.append(root)
        while(queue):
            curr = queue.pop(0)
            temp = curr.left
            curr.left = curr.right
            curr.right = temp
            
            if(curr.left is not None):
                queue.append(curr.left)
            if(curr.right is not None):
                queue.append(curr.right)
            
        return root
            