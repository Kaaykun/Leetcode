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
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check_tree(root):
            # If the tree is non-existant, return any value != -1
            if root is None:
                return 1

            left = check_tree(root.left)
            # If left subtree of current node is -1, it is unbalanced
            if left == -1:
                return -1
            right = check_tree(root.right)
            # If right subtree of current node is -1, it is unbalanced
            if right == -1:
                return -1
            # If absolute value of left - right is bigger than one, it is unbalanced
            if abs(left - right) > 1:
                # Return -1 so it fails check in "isBalanced"
                return -1
            # If other checks are passed, return any value != -1
            return 1 + max(left, right)

        return check_tree(root) != -1


def main():
    # Test cases: nums = [3,9,20,null,null,15,7], output = True
    #             nums = [1,2,2,3,3,null,null,4,4], output = False
    nums = [-10,-3,0,5,9]
    root = buildBinaryTree(nums, 0)
    solution = Solution()
    print(solution.isBalanced(root))


if __name__ == "__main__":
    main()