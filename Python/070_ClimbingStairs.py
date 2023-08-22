class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        memory = {0: 1, 1: 1}

        def climb(n):
            if n in memory:
                return memory[n]
            else:
                memory[n] = climb(n-1) + climb(n-2)
                return memory[n]

        return climb(n)


def main():
    solution = Solution()
    # Test cases: n = 2 Expected = 2, n = 3 Expected 3
    n = 5
    print(solution.climbStairs(n))


if __name__ == "__main__":
    main()