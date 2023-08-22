class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        prefix = ""
        if len(strs) == 0:
            return prefix

        for i in range(min(map(lambda x: len(x), strs))):
            char = strs[0][i]
            if all(words[i] == char for words in strs):
                prefix += char
            else:
                break
        return prefix


def main():
    solution = Solution()
    # Test cases: ["flower","flow","flight"], ["dog","racecar","car"]
    strs = ["reflower","flow","flight"]
    print(solution.longestCommonPrefix(strs))


if __name__ == "__main__":
    main()