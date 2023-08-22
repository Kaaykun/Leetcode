class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        try:
            index = haystack.index(needle)
            return index
        except ValueError:
            return -1


def main():
    solution = Solution()
    # Test cases: haystack = "sadbutsad" and needle = "sad", haystack = "leetcode" and needle = "leeto"
    haystack = "sadbutsad"
    needle = "sad"
    print(solution.strStr(haystack, needle))


if __name__ == "__main__":
    main()