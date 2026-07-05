from collections import defaultdict
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        final = []
        for num in nums:
            count[num]+=1
        print(count)
        
        freq = [[] for i  in range(len(nums)+1)]
        for item,value in count.items():
            freq[value].append(item)
        
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                final.append(num)
                if len(final)==k:
                    return final
