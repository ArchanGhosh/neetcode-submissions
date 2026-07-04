class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        char_count = {}
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            if s[i] in char_count:
                char_count[s[i]]+=1
            else:
                char_count[s[i]]=1
            if t[i] in char_count:
                char_count[t[i]]-=1
            else:
                char_count[t[i]]=-1
        
        for j in char_count:
            if char_count[j] !=0:
                return False
        
        return True
