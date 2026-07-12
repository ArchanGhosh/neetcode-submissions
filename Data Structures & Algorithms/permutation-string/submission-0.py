class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False

        s1_count = [0] * 26
        window_count = [0] * 26

        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            window_count[ord(s2[i]) - ord('a')] += 1
        
        total_perm = 0

        for i in range(26):
            if s1_count[i] == window_count[i]:
                total_perm += 1
        
        left = 0
        for right in range(len(s1), len(s2)):
            if total_perm == 26:
                return True

            idx = ord(s2[right]) - ord('a')
            window_count[idx] += 1
            if window_count[idx] == s1_count[idx]:
                total_perm += 1
            elif window_count[idx] == s1_count[idx] + 1:
                total_perm -= 1

            idx = ord(s2[left]) - ord('a')
            window_count[idx] -= 1
            if window_count[idx] == s1_count[idx]:
                total_perm += 1
            elif window_count[idx] == s1_count[idx] - 1:
                total_perm -= 1

            left += 1

        return total_perm == 26
