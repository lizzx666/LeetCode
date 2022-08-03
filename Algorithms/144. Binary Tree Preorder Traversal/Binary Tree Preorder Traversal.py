'''

Given the root of a binary tree, return the preorder traversal of its nodes' values.

 

Example 1:
Input: root = [1,null,2,3]
Output: [1,2,3]

Example 2:
Input: root = []
Output: []


Example 3:
Input: root = [1]
Output: [1]


'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        
        def traversal(root):
            if not root:
                return
            result.append(root.val)
            traversal(root.left)
            traversal(root.right)
            
        traversal(root)
        return result



class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        if not root:
            return []
        stack, output = [root,], []
        
        while stack:
            root = stack.pop()
            if root:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
  
        
        return output