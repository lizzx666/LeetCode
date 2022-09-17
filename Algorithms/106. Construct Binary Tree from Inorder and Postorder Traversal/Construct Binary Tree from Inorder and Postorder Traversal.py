'''

Given two integer arrays inorder and postorder where inorder is the inorder traversal of a binary tree and postorder is the postorder traversal of the same tree, 
construct and return the binary tree.

 

Example 1:
Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]


Example 2:
Input: inorder = [-1], postorder = [-1]
Output: [-1]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not postorder:
            return None
        #last item of postorder is current root
        root_val = postorder[-1]
        root = TreeNode(root_val)
        
        #find cutting point
        separator_idx = inorder.index(root_val)
        
        #cut inorder array
        inorder_left = inorder[:separator_idx]
        inorder_right = inorder[separator_idx+1:]
        
        #cut postorder array, after-cut postorder array length should be same with after-cut inorder array
        postorder_left = postorder[:len(inorder_left)]
        postorder_right = postorder[len(inorder_left):len(postorder)-1]
        
        #recursion
        root.left = self.buildTree(inorder_left,postorder_left)
        root.right = self.buildTree(inorder_right,postorder_right)
        
        return root
