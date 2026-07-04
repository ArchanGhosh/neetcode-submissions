class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement = {}

        for i, num in enumerate(nums):
            diff = target - num
            if diff in complement.keys():
                return [complement[diff], i]
            else:
                complement[num] = i
        return [] 