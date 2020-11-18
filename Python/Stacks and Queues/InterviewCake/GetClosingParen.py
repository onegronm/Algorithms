import unittest
# https://www.interviewcake.com/question/python3/matching-parens?course=fc1&section=queues-stacks

#"Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

#Write a function that, given a sentence like the one above, along with the position of an opening parenthesis, finds the corresponding closing parenthesis.

#Example: if the example string above is input with the number 10 (position of the first parenthesis), the output should be 79 (position of the last parenthesis).
def get_closing_paren(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    openStack = []

    for i in range(0, len(sentence)):
        if sentence[i] == '(':
            openStack.append(i)
        elif sentence[i] == ')':
            index = openStack.pop()
            if index == opening_paren_index:
                return i

    raise Exception("No matching closing parenthesis")

def get_closing_paren_O_1_Space(sentence, opening_paren_index):

    # Find the position of the matching closing parenthesis
    open_nested_parents = 0

    for i in range(opening_paren_index + 1, len(sentence)):
        if sentence[i] == '(':
            open_nested_parents += 1
        elif sentence[i] == ')':            
            if open_nested_parents == 0:
                return i
            else: 
                open_nested_parents -= 1

    raise Exception("No matching closing parenthesis")

# Tests
class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)


    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)

unittest.main(verbosity=2)
