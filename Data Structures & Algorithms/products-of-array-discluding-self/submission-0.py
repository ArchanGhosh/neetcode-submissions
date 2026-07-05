class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * (len(nums) + 1)
        suffix = [1] * (len(nums) + 1)

        p_mul = 1
        for i, num in enumerate(nums):
            prefix[i] = p_mul
            p_mul *= num

        s_mul = 1
        for i in range(len(nums)-1, -1, -1):
            suffix[i] = s_mul
            s_mul *= nums[i]
        
        ans = [prefix[i] * suffix[i] for i in range(len(nums))]

        return ans