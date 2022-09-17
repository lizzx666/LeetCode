'''
Given two integer arrays preorder and inorder where preorder is the preorder traversal of a binary tree and inorder is the inorder traversal of the same tree, 
construct and return the binary tree.

 

Example 1:
Input: preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
Output: [3,9,20,null,null,15,7]


Example 2:
Input: preorder = [-1], inorder = [-1]
Output: [-1]


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder:
            return None
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        separator_idx = inorder.index(root_val)
        
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1:]
        
        preorder_left = preorder[1:1+len(inorder_left)]
        #both are ok
        preorder_right = preorder[1+len(inorder_left):]
        #preorder_right = preorder[len(preorder)-len(inorder_right):]
        
        root.left = self.buildTree(preorder_left,inorder_left)
        root.right = self.buildTree(preorder_right,inorder_right)
