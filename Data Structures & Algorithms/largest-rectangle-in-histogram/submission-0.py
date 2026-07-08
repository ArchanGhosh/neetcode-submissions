class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        max_area = 0

        for i, height in enumerate(heights):
            start = i

            while stack and stack[-1][1] > height:
                idx, hgt = stack.pop()
                max_area = max(max_area, hgt * (i - idx))
                start = idx

            stack.append((start, height))

        n = len(heights)

        while stack:
            idx, hgt = stack.pop()
            max_area = max(max_area, hgt * (n - idx))

        return max_area