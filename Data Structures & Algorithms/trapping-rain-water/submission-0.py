class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)

        left, right = 0, n-1
        left_lvl, right_lvl = height[left], height[right]

        area = 0
        while left<right:
            if left_lvl<right_lvl:
                left+=1
                left_lvl = max(left_lvl, height[left])
                area+=left_lvl-height[left]
            else:
                right-=1
                right_lvl = max(right_lvl, height[right])
                area+=right_lvl-height[right]
        return area        
    