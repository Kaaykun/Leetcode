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
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        return(max(self.maxDepth(root.left), self.maxDepth(root.right))+1)

        # depth_left = self.maxDepth(root.left)
        # depth_right = self.maxDepth(root.right)

        # return max(depth_left, depth_right)+1


def main():
    # Test cases: nums = [3,9,20,null,null,15,7], output = 3
    #             nums = root = [1,null,2], output = 2
    nums = [3,9,20,None,None,15,7]
    root = buildBinaryTree(nums, 0)
    solution = Solution()
    print(solution.maxDepth(root))


if __name__ == "__main__":
    main()