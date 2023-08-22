class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i -1][j - 1] + pascal[i - 1][j]
        return pascal


def main():
    # Test cases: numRows = 5, output = [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    #             numRows = 1, output = [[1]]
    numRows = 5
    solution = Solution()
    print(solution.generate(numRows))


if __name__ == "__main__":
    main()