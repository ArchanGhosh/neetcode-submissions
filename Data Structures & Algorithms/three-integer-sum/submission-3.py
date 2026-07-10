class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final = []
        n = len(nums)
        for i in range(n):
            left, right = i+1, n-1
            if i>0 and nums[i] == nums[i-1]:
                continue

            while left<right:
                target = nums[i] + nums[left] + nums[right]
                if target == 0:
                    final.append([nums[i], nums[left], nums[right]])
                    left+=1
                    right-=1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
                    while left < right and nums[right] == nums[right+1]:
                        right -= 1
                elif target > 0:
                    right-=1
                else:
                    left+=1
        return final