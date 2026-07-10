class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        complement = {}

        for i, num in enumerate(numbers):
            diff = target - num
            if diff in complement:
                return [complement[diff]+1, i+1]
            else:
                complement[num]=i
        