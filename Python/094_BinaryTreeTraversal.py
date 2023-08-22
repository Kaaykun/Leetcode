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
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []

        result = []
        result.extend(self.inorderTraversal(root.left))
        result.append(root.val)
        result.extend(self.inorderTraversal(root.right))
        return result


def main():
    # Test cases: root = [1,null,2,3], output = [1,3,2]
    #             root = [], output = []
    #             root = [1], output = [1]
    nums = [3,1,2]
    root = buildBinaryTree(nums, 0)

    solution = Solution()
    print(solution.inorderTraversal(root))


if __name__ == "__main__":
    main()