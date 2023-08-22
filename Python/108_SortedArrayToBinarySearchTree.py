class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        # If the array is empty, return None
        if not nums:
            return None
        # Find the middle element of the array
        start = 0
        end = len(nums) - 1
        mid = (start + end) // 2
        # Create a new node with middle element as its value
        root = TreeNode(nums[mid])
        # Recursively construct the left subtree using the left half of the array
        root.left = self.sortedArrayToBST(nums[:mid])
        # Recursively construct the right subtree using the right half of the array
        root.right = self.sortedArrayToBST(nums[mid+1:])

        return root


def main():
    # Test cases: nums = [-10,-3,0,5,9], output = [0,-3,9,-10,null,5]
    #             nums = [1,3], output = [3,1]
    nums = [-10,-3,0,5,9]
    solution = Solution()
    print(solution.sortedArrayToBST(nums))


if __name__ == "__main__":
    main()