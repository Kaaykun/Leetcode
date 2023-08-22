class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.strip().split(" ")[-1])


def main():
    solution = Solution()
    # Test cases: "Hello World" = 5, "   fly me   to   the moon  " = 4, "luffy is still joyboy" = 6
    s = "   fly me   to   the moon  "
    print(solution.lengthOfLastWord(s))


if __name__ == "__main__":
    main()