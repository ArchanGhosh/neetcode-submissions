class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        diff = [0] * len(temperatures)

        for i in range(len(temperatures)):
            curr_temp = temperatures[i]

            while stk and curr_temp>temperatures[stk[-1]]:
                prev = stk.pop()
                diff[prev] = i - prev
            stk.append(i)
        
        return diff

