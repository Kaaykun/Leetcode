class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # map: each digit in digits into str, then concatenate in empty str ""
        digits_int = int("".join(map(str, digits)))
        digits_int += 1
        # digits_int into str, then iterate over each digit in str to convert back to single digit ints
        return [int(x) for x in str(digits_int)]


def main():
    solution = Solution()
    # Test cases: digits = [1,2,3] = [1,2,4], digits = [4,3,2,1] = [4,3,2,2], digits = [9] = [1,0], digits = [9,9] = [1,0,0]
    digits = [9,9]
    print(solution.plusOne(digits))


if __name__ == "__main__":
    main()