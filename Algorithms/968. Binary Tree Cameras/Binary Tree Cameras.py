'''


You are given the root of a binary tree. We install cameras on the tree nodes where each camera at a node can monitor its parent, itself, and its immediate children.
Return the minimum number of cameras needed to monitor all nodes of the tree.

 

Example 1:
Input: root = [0,0,null,0,0]
Output: 1
Explanation: One camera is enough to monitor all nodes if placed as shown.

Example 2:
Input: root = [0,0,null,0,null,0,null,null,0]
Output: 2
Explanation: At least two cameras are needed to monitor all nodes of the tree. The above image shows one of the valid configurations of camera placement.


'''





class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        #status:
        #0: not covered
        #1: equip camera
        #2: been covered

        result = 0
        def traversal(curr):
            nonlocal result

            if not curr:
                return 2
            left = traversal(curr.left)
            right = traversal(curr.right)

            if left == 2 and right == 2:
                return 0
            elif left == 0 or right == 0:
                result+=1
                return 1
            elif left == 1 or right == 1:
                return 2

        if traversal(root)==0:
            result += 1

        return result
