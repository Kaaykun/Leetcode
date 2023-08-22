class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        replace = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[replace] = nums[i]
                replace += 1
        return replace


def main():
    solution = Solution()
    # Test cases: val = 3 and nums = [3,2,2,3] == 2, val = 2 and nums = [0,1,2,2,3,0,4,2] == 5
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    print(solution.removeElement(nums, val))


if __name__ == "__main__":
    main()