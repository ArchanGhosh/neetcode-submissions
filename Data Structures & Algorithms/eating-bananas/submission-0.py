import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        max_k = max(piles)

        curr_k = 1
        k = float("inf")
        while max_k>=curr_k:
            mid_k = (max_k + curr_k)//2
            total_h = 0
            for pile in piles:
                total_h= total_h + (math.ceil(pile/mid_k))

            if total_h>h:
                curr_k = mid_k+1
            elif total_h<=h:
                k = min(mid_k, k)
                max_k = mid_k-1
        return k




