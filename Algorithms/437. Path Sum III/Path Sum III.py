'''
Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

 

Example 1:
Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
Output: 3
Explanation: The paths that sum to 8 are shown.


Example 2:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
Output: 3

'''


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def preorder(node:TreeNode,curr_sum):
            nonlocal count
            if not node:
                return 
            
            curr_sum += node.val
            
            if curr_sum==k:
                count+=1
            
            if curr_sum - k in h:
                count += h[curr_sum - k]
            
            h[curr_sum]+=1

            #process for left subtree
            preorder(node.left,curr_sum)

            #process for right subtree
            preorder(node.right,curr_sum)
            
            #remove the current sum from the hashmap
            #in order not to use it during the parallel subtree processing
            h[curr_sum]-=1
        
        count, k = 0,sum
        h = defaultdict(int)
        preorder(root,0)
        return count
