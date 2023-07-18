'''
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called root.

Besides the root, each house has one and only one parent house. 
After a tour, the smart thief realized that all houses in this place form a binary tree. 
It will automatically contact the police if two directly-linked houses were broken into on the same night.

Given the root of the binary tree, return the maximum amount of money the thief can rob without alerting the police.

Example 1:
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.


Example 2:
Input: root = [3,4,5,1,3,null,1]
Output: 9
Explanation: Maximum amount of money the thief can rob = 4 + 5 = 9.

'''



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        rs = self.rob_tree(root)
        return max(rs[0],rs[1])
        
    def rob_tree(self,cur):
        #store each node's decision in a list ls
        #ls[0] means the biggest value if skip cur node
        #ls[1] means the biggest value if steal cur node
        if not cur:
            return [0,0]
        left_dp = self.rob_tree(cur.left)
        right_dp = self.rob_tree(cur.right)

        #if steal cur node
        val_1 = cur.val+left_dp[0]+right_dp[0]
        #if skip cur node
        val_2 = max(left_dp[0],left_dp[1])+max(right_dp[0],right_dp[1])

        return [val_2,val_1]
        

class Solution:
    def rob(self, root: TreeNode) -> int:
        def helper(node):
            #return [rob this node, not rob this node]
            if not node:
                return (0,0)
            left = helper(node.left)
            right = helper(node.right)
            rob = node.val + left[1] + right[1]
            not_rob = max(left) + max(right)
            return [rob, not_rob]
        return max(helper(root))
