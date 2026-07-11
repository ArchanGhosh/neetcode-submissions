class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n-1
        max_area = 0
        while left<right:
            curr_area = (right - left)*(min(heights[left], heights[right]))
            max_area = max(curr_area, max_area)

            if heights[left]<heights[right]:
                left+=1
            elif heights[left]>heights[right]:
                right-=1
            else:
                left+=1
                right-=1

        return max_area
