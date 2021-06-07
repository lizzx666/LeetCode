"""Given the root of a Binary Search Tree and a target number k, 
return true if there exist two elements in the BST such that their sum is equal to the given target."""








# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return False
        return self.findTarget2(root,set(),k)
    
    
    def findTarget2(self,node,nodes,k):
        if not node:
            return False
        
        complement = k - node.val
        if complement in nodes:
            return True
        nodes.add(node.val)
        
        return self.findTarget2(node.left,nodes,k) or self.findTarget2(node.right,nodes,k)
