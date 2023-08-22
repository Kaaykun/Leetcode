class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        


def main():
    # Test cases: nums = [1,0,-1,0,-2,2], target = 0, Output = [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
    #             nums = [2,2,2,2,2], target = 8, Output = [[2,2,2,2]]
    nums = [1,0,-1,0,-2,2]
    target = 0

    solution = Solution()
    print(solution.fourSum(nums, target))


if __name__ == "__main__":
    main()