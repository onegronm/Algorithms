# Salesforce software engineer coding test round 1
import unittest

class Solution:
    
    def isPalindrome(self, sentence) -> bool:
        """
        """
       
        if sentence is None:
            raise ValueError("Invalid argument. Input string must have a value.")

        if len(sentence) == 0: return True

        isPalindrome = True
        
        lo = 0
        hi = len(sentence) - 1
        
        while lo <= hi:
            loChar = sentence[lo]
            hiChar = sentence[hi]
            
            if loChar != hiChar:
                isPalindrome = False
                break # <= you forgot to break here
            else:
                lo += 1
                hi -= 1
                
        return isPalindrome
        
        
class Test(unittest.TestCase):
    def test1(self):
        s = Solution()
        self.assertTrue(s.isPalindrome("eve"))
        
    def test2(self):
        s = Solution()
        self.assertTrue(s.isPalindrome("otto"))
        
    def test3(self):
        s = Solution()
        self.assertTrue(s.isPalindrome("rotator"))
        
    def test4(self):
        s = Solution()
        self.assertTrue(s.isPalindrome("adcda"))
        
    def test5(self):
        s = Solution()
        self.assertTrue(s.isPalindrome(""))
        
    def test6(self):
        s = Solution()
        self.assertFalse(s.isPalindrome("venezuela"))

    def test7(self):
        s = Solution()
        try:
            s.isPalindrome(None)
        except ValueError: 
            self.assertTrue(True)

unittest.main(verbosity=2)

