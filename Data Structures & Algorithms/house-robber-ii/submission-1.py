class Solution:
    def rob(self, nums: List[int]) -> int:

        def find_max(nums):
            if not nums:
                return 0
            if len(nums) == 1:
                return nums[0]
            dp = [0] * len(nums)
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])

            for i in range(2, len(nums)):
                dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])

            return dp[-1]

        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        return max(find_max(nums[1:]),find_max(nums[:-1]))