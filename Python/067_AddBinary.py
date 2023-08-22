class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return bin(int(a, 2) + int(b, 2))[2:]


def main():
    solution = Solution()
    # Test cases: a = "11", b = "1" = "100", a = "1010", b = "1011" = "10101"
    a = "1010"
    b = "1011"
    print(solution.addBinary(a, b))


if __name__ == "__main__":
    main()