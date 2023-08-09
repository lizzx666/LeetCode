'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 2

Example 2:
Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5


'''









# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.get_height(root)

    def get_height(self,node):
        if not node:
            return 0
        
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)

        if not node.left and node.right:
            return 1+right_height
        if node.left and not node.right:
            return 1+left_height
        
        return 1+min(left_height,right_height)






class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        
        min_depth = float('inf')
        
        if root.left:
            min_depth = min(self.minDepth(root.left),min_depth)
        if root.right:
            min_depth = min(self.minDepth(root.right),min_depth)
        
        return min_depth+1
