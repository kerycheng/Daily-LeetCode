class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dict = {'(': ')', 
                '[': ']',
                '{': '}'}
        stack = []

        for char in s:
            if char in '([{':
                stack.append(char)
            elif len(stack) == 0 or char != dict[stack.pop()]:
                return False
        return len(stack) == 0
                