class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 0:
            return 0
        start = 0
        end = x
        answer = 0

        while start <= end:
            mid = (start + end) // 2

            if mid * mid <= x and (mid+1) * (mid+1) > x:
                return mid
            elif mid * mid > x:
                end = mid -1
            else:
                start = mid +1
        return answer

def main():
    solution = Solution()
    # Test cases: x = 4 Expected = 2, x = 8 Expected 2
    x = 36
    print(solution.mySqrt(x))


if __name__ == "__main__":
    main()