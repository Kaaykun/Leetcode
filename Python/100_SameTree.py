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
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

        return p is q


def main():
    # Test cases: p = [1,2,3], q = [1,2,3], output = true
    #             p = [1,2], q = [1,null,2], output = false
    #             p = [1,2,1], q = [1,1,2], output = false
    p_nums = [1,2]
    q_nums = [1,2]
    p = buildBinaryTree(p_nums, 0)
    q = buildBinaryTree(q_nums, 0)

    solution = Solution()
    print(solution.isSameTree(p, q))


if __name__ == "__main__":
    main()