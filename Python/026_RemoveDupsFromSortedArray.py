class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        replace = 1

        for i in range(1, len(nums)):
            if nums[i-1] != nums[i]:
                nums[replace] = nums[i]
                replace += 1
        return replace


def main():
    solution = Solution()
    # Test cases: [1,1,2] == 2, [0,0,1,1,1,2,2,3,3,4] == 5
    nums = [0,0,1,1,1,2,2,3,3,4]
    print(solution.removeDuplicates(nums))


if __name__ == "__main__":
    main()