'''

Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

 

Example 1:
Input: root = [1,2,2,3,4,4,3]
Output: true


Example 2:
Input: root = [1,2,2,null,3,null,3]
Output: false


'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.compare(root.left,root.right)
    
    def compare(self,left,right):
        if left == None and right!=None:
            return False
        elif left!=None and right==None:
            return False
        elif left==None and right==None:
            return True
        elif left.val!=right.val:
            return False
        
        return self.compare(left.left,right.right) and self.compare(left.right,right.left)
