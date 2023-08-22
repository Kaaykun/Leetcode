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


def isMirror(node1, node2):
        # Base case: if both nodes are None, they are considered symmetric
        if node1 is None and node2 is None:
            return True
        # Check if one of the nodes is None or their values are different
        if node1 is None or node2 is None or node1.val != node2.val:
            return False
        # print("Node 1 left:", node1.val)
        # print("Node 1 right:", node1.val)
        # print("Node 2 left:", node2.val)
        # print("Node 2 right:", node2.val)
        # Recursively check the subtrees
        return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return isMirror(root, root)


def main():
    # Test cases: nums = [1,2,2,3,4,4,3], output = true
    #             nums = root = [1,2,2,null,3,null,3], output = false
    nums = [1,2,2,3,4,4,3]
    root = buildBinaryTree(nums, 0)
    solution = Solution()
    print(solution.isSymmetric(root))


if __name__ == "__main__":
    main()