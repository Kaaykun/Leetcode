class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = sorted(nums1 + nums2)
        n = len(nums)
        if n % 2 == 0:
            mid1 = nums[n // 2 - 1]
            mid2 = nums[n // 2]
            median = float((mid1 + mid2) / 2)
        else:
            median = float(nums[n // 2])
        return median


def main():
    # Test cases: [1,3] & [2], [1,2] & [3,4]
    nums1 = [1,2]
    nums2 = [3,4]
    solution = Solution()

    print(solution.findMedianSortedArrays(nums1, nums2))


if __name__ == "__main__":
    main()