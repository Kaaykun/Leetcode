class Solution(object):
    def __init__(self):
        self._nums = [int(num) for num in input("Nums: ").split(",")]
        self._target = int(input("Target: "))

    @property
    def nums(self):
        return self._nums

    @property
    def target(self):
        return self._target

    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i, value in enumerate(nums):
            remaining = target - nums[i]
            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[value] = i


def main():
    solution = Solution()
    print(solution.twoSum(solution.nums, solution.target))


if __name__ == "__main__":
    main()