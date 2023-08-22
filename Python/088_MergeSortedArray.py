class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()
        return nums1


def main():
    # Test cases: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 --> [1,2,2,3,5,6]
    #             nums1 = [1], m = 1, nums2 = [], n = 0                --> [1]
    #             nums1 = [0], m = 0, nums2 = [1], n = 1               --> [1]
    nums1 = [0,0,0,0,0]
    m = 0
    nums2 = [1,2,3,4,5]
    n = 5
    solution = Solution()

    print(solution.merge(nums1, m, nums2, n))


if __name__ == "__main__":
    main()