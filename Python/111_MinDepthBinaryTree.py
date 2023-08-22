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
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        left = self.minDepth(root.left)
        right = self.minDepth(root.right)
        print("left:", left)
        print("right:", right)

        if root.left is None and root.right is None:
            return 1
        if root.left is None:
            return right + 1
        if root.right is None:
            return left + 1

        return(min(left, right)+1)


def main():
    # Test cases: nums = [3,9,20,None,None,15,7], output = 2
    #             nums = [2,None,3,None,4,None,5,None,6], output = 5
    nums = [2,None,3,None,4,None,5,None,6]
    root = buildBinaryTree(nums, 0)
    solution = Solution()
    print(solution.minDepth(root))


if __name__ == "__main__":
    main()