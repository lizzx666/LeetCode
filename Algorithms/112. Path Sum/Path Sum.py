'''
Given the root of a binary tree and an integer targetSum, 
return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.

 

Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true

Example 2:
Input: root = [1,2,3], targetSum = 5
Output: false

Example 3:
Input: root = [1,2], targetSum = 0
Output: false



'''





class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def traversal(node,target):
            if node.left==None and node.right==None and target==0:
                return True
            if node.left==None and node.right==None and target!=0:
                return False
            if node.left:
                if traversal(node.left,target-node.left.val):
                    return True
            if node.right:
                if traversal(node.right,target-node.right.val):
                    return True
            return False
        if not root:
            return False
        else:
            return traversal(root,targetSum-root.val)
         
         


class Solution:
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        if not root:
            return False
        if root.val == targetSum and not(root.left or root.right):
            return True
        
        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
