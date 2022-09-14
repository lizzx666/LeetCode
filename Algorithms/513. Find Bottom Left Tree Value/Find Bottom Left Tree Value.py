'''

Given the root of a binary tree, return the leftmost value in the last row of the tree.

 

Example 1:
Input: root = [2,1,3]
Output: 1


Example 2:
Input: root = [1,2,3,4,null,5,6,null,null,7]
Output: 7

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_depth = float('-inf')
        leftmost_val = 0
        
        def traversal(node,depth):
            nonlocal max_depth, leftmost_val
            if node.left==None and node.right==None:
                if depth>max_depth:
                    max_depth=depth
                    leftmost_val = node.val
            if node.left:
                depth+=1
                traversal(node.left,depth)
                depth-=1
            if node.right:
                depth+=1
                traversal(node.right,depth)
                depth-=1
                
        traversal(root,0) 
        return leftmost_val
