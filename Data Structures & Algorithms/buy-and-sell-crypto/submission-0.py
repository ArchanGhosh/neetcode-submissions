class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prof = 0
        _curr, _next = 0, 1
        n = len(prices)


        while _next<n:
            if prices[_next]>prices[_curr]:
                prof = max(prof, prices[_next]-prices[_curr])
                
            else:
                _curr = _next
            _next+=1
        return prof