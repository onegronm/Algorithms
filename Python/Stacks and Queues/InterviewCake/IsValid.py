import unittest

# Write an efficient function that tells us whether or not an input string's openers and closers are properly nested.
def is_valid(code):

    # Determine if the input code is valid
    # valid operations:
    # opening a bracket, curly brace, or parenthesis

    # invalid operations:
    # the closing symbol is different than the top symbol on the stack
    openStack = []
    for i in range(0, len(code)):
        char = code[i]
        if char == '(' or char == '[' or char == '{':
            openStack.append(char)
        else:
            if not openStack:
                return False

            lastOpen = openStack.pop()           
            if (char == ')' and lastOpen != '(') or (char == ']' and lastOpen != '[') or (char == '}' and lastOpen != '{'):
                return False

    if openStack:
        return False

    return True

class Test(unittest.TestCase):

    def test_valid_short_code(self):
        result = is_valid('()')
        self.assertTrue(result)

    def test_valid_longer_code(self):
        result = is_valid('([]{[]})[]{{}()}')
        self.assertTrue(result)

    def test_interleaved_openers_and_closers(self):
        result = is_valid('([)]')
        self.assertFalse(result)

    def test_mismatched_opener_and_closer(self):
        result = is_valid('([][]}')
        self.assertFalse(result)

    def test_missing_closer(self):
        result = is_valid('[[]()')
        self.assertFalse(result)

    def test_extra_closer(self):
        result = is_valid('[[]]())')
        self.assertFalse(result)

    def test_empty_string(self):
        result = is_valid('')
        self.assertTrue(result)

unittest.main(verbosity=2)
