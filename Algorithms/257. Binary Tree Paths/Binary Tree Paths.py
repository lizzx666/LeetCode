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
