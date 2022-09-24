'''
You are given the root of a binary search tree (BST) and an integer val.

Find the node in the BST that the node's value equals val and return the subtree rooted with that node. 
If such a node does not exist, return null.

Example 1:
Input: root = [4,2,7,1,3], val = 2
Output: [2,1,3]


Example 2:
Input: root = [4,2,7,1,3], val = 5
Output: []

'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#recursion
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root or root.val==val:
            return root
        result = TreeNode(None)
        if root.val>val:
            result = self.searchBST(root.left,val)
        if root.val<val:
            result = self.searchBST(root.right,val)
            
        return result
    

#iteration
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return root
        while root:
            if root.val<val:
                root = root.right
            elif root.val>val:
                root = root.left
            else:
                return root
        return None



