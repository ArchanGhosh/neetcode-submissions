class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        _cleaned = "".join(char for char in s if char.isalnum())
        n = len(_cleaned)
        for i in range(n//2):
            front = i
            rear = n-1-i
            if _cleaned[front].lower() != _cleaned[rear].lower():
                return False
        
        return True