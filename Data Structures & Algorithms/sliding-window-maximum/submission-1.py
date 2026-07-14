from collections import deque

class Solution:
    def maxSlidingWindow(self, nums, k):
        dq = deque()
        final = []
        i = 0
        while i < len(nums):

            while dq and dq[0] <= i - k:
                dq.popleft()

            while dq and nums[dq[-1]] < nums[i]:
                dq.pop()

            dq.append(i)

            if i >= k - 1:
                final.append(nums[dq[0]])
            
            i+=1

        return final