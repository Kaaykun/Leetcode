class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1
        # Default answer when target is greater than all elements
        answer = len(nums)
        # Binary search, start in middle - if target not in middle, search if greater or smaller
        while start <= end:
            mid = (start + end) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                start = mid + 1
            else:
                answer = mid
                end = mid - 1
        return answer


def main():
    solution = Solution()
    # Test cases: nums = [1,3,5,6] and target = 5, nums = [1,3,5,6] and target = 2, nums = [1,3,5,6] and target = 7
    nums = [1,3,5,6]
    target = 7
    print(solution.searchInsert(nums, target))


if __name__ == "__main__":
    main()