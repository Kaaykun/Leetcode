class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        start = 0
        end = 0

        for i in range(n):
            # Works for palindrome of odd number of chars
            len1 = expand(s, i, i)
            # Works for palindrome of even number of chars
            len2 = expand(s, i, i + 1)
            # Figure out which of the two lengths is bigger
            length = max(len1, len2)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return(s[start:end+1])


def expand(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1

def main():
    s = "babad"
    solution = Solution()
    print(solution.longestPalindrome(s))


if __name__ == "__main__":
    main()