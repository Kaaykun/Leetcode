class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pascal = [[1] * (i + 1) for i in range(rowIndex + 1)]
        for i in range(rowIndex + 1):
            for j in range(1, i):
                pascal[i][j] = pascal[i -1][j - 1] + pascal[i - 1][j]
        return pascal[rowIndex]


def main():
    # Test cases: rowIndex = 3, output = [1,3,3,1]
    #             rowIndex = 1, output = [1,1]
    #             rowIndex = 0, output = [1]
    rowIndex = 3
    solution = Solution()
    print(solution.getRow(rowIndex))


if __name__ == "__main__":
    main()