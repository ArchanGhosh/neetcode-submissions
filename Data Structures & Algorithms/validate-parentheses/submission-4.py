class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {"{": "}",
                 "[": "]",
                 "(": ")" 
                }

        if len(s)%2!=0:
            return False
        
        if s[0] in pairs.values():
            return False
        
        track = []

        
        for obj in s:
            if obj in pairs:
                track.append(obj)
            else:
                if not track:
                    return False

                if obj == pairs[track[-1]]:
                    track.pop()
                else:
                    return False
        
        return len(track) == 0