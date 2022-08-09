'''


Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:

a binary tree in which the left and right subtrees of every node differ in height by no more than 1.

 

Example 1:
Input: root = [3,9,20,null,null,15,7]
Output: true

Example 2:
Input: root = [1,2,2,3,3,null,null,4,4]
Output: false

Example 3:
Input: root = []
Output: true


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.getheight(root)!=-1:
            return True
        else:
            return False
        
    def getheight(self,node):
        if not node:
            return 0
        left_height = self.getheight(node.left)
        if left_height == -1:
            return -1
        right_height = self.getheight(node.right)
        if right_height == -1:
            return -1

        if abs(left_height-right_height)>1:
            return -1
        else:
            return 1 + max(left_height,right_height)
