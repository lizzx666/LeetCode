'''
Given the root of a binary tree, return the sum of all left leaves.

A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.


Example 2:
Input: root = [1]
Output: 0


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.traversal(root)
    
    def traversal(self,node):
        if node==None:
            return 0
        if node.left==None and node.right==None:
            return 0
        left_val = self.traversal(node.left)
        if node.left and node.left.left==None and node.left.right==None:
            left_val = node.left.val
            
        right_val = self.traversal(node.right)
        sum_val = left_val + right_val
        return sum_val
