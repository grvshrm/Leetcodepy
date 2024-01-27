# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        vertMap = defaultdict(list)
        levelQ = []
        levelQ.append([root, 0, 0])
        while levelQ:
            temp = levelQ.pop(0)
            cur, vlevel, hlevel = temp[0], temp[1], temp[2]
            vertMap[(vlevel, hlevel)].append(cur.val)
            if cur.left:
                levelQ.append([cur.left, vlevel - 1, hlevel + 1])
            if cur.right:
                levelQ.append([cur.right, vlevel + 1, hlevel + 1])
        vertMap = dict(sorted(vertMap.items()))
        ans = defaultdict(list)
        for key, item in vertMap.items():
            ans[key[0]].extend(sorted(item))
        return ans.values() 