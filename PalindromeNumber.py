class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers are NOT palindrome
        if x < 0:
            return False
        
        rev = self.reverseDigit(x)
        return x == rev
    
    def reverseDigit(self, x: int) -> int:
        rev = 0
        
        while x != 0:
            digit = x % 10
            rev = (rev * 10) + digit
            x = x // 10
        
        return rev


# 🔥 Test cases (for IDE run)
if __name__ == "__main__":
    sol = Solution()
    
    test_cases = [121, -121, 10, 12321, 0]

    for num in test_cases:
        print(f"{num} -> {sol.isPalindrome(num)}")