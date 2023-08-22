class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def buildBinaryTree(nums, index):
    if index >= len(nums) or nums[index] is None:
        return None

    root = TreeNode(nums[index])
    root.left = buildBinaryTree(nums, 2 * index + 1)  # Recursive call for left child
    root.right = buildBinaryTree(nums, 2 * index + 2)  # Recursive call for right child
    return root


class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if root is None:
            return False

        if root.left is None and root.right is None and root.val == targetSum:
            return True

        targetSum -= root.val
        
        return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)


def main():
    # Test cases: nums = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22, output = True
    #             nums = [1,2,3], targetSum = 5, output = False
    nums = [1,2,3]
    targetSum = 5
    root = buildBinaryTree(nums, 0)
    solution = Solution()
    print(solution.hasPathSum(root, targetSum))


if __name__ == "__main__":
    main()