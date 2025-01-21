#time: O(n)
#Space: O(height of recursive stack)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.hasPath = False
        self.dfs(root,0,targetSum)
        return self.hasPath

    def dfs(self, root, cs ,targetSum):
        if root is None:
            return True
        cs= cs + int(root.val)
        self.dfs(root.left, cs, targetSum)
        self.dfs(root.right, cs, targetSum)
        if (root.left is None and root.right is None and cs == targetSum):
            self.hasPath= True
            return
                
        
        
