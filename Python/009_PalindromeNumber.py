class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x_str = str(x)
        rev = x_str[::-1]
        return x_str == rev


def main():
    x = 122
    solution = Solution()
    print(solution.isPalindrome(x))


if __name__ == "__main__":
    main()