'''
Given the root of a binary tree, return all root-to-leaf paths in any order.

A leaf is a node with no children.

 

Example 1:
Input: root = [1,2,3,null,5]
Output: ["1->2->5","1->3"]


Example 2:
Input: root = [1]
Output: ["1"]


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        path = ''
        result = []
        if not root:
            return result

        self.traversal(root,path,result)
        return result
         
    def traversal(self,node,path,result):
        path+=str(node.val)
        
        if node.left==None and node.right==None:
            result.append(path)
            
        if node.left:
            self.traversal(node.left,path + '->',result)
            
            
        if node.right:
            self.traversal(node.right,path + '->',result)



          
          
          


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def construct_paths(root,path):
            if root:
                path += str(root.val)
                if not root.left and not root.right:
                    paths.append(path)
                else:
                    path += "->"
                    construct_paths(root.left,path)
                    construct_paths(root.right,path)
        paths = []
        construct_paths(root, "")
        return paths
