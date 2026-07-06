class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        distinct = set(nums)
        ans = 0

        for num in distinct:
            if num - 1 not in distinct:
                curr = num
                length = 1

                while curr + 1 in distinct:
                    curr += 1
                    length += 1

                ans = max(ans, length)

        return ans