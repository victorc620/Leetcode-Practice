# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        
        for i in range(len(x)):
                    
            # Odd number digit
            if len(x)%2 != 0:
                if i == int((len(x)/2)-0.5):
                    # x(i) is the middle digit
                    break
                elif x[i] != x[(-i)-1]:
                    return False
                
            # Even number digit
            elif len(x)%2 == 0:
                if i == int(len(x)/2):
                    # x(i) pass the middle digit
                    break
                elif x[i] != x[(-i)-1]:
                    return False
            
        return True