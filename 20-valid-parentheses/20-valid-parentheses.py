class Solution:
    def isValid(self, s: str) -> bool:
        stack = list()
        for i in range(len(s)):
            c = s[i]
            match c:
                case '(':
                    stack.append(')')
                case '{':
                    stack.append('}')
                case '[':
                    stack.append(']')
                case _ if((len(stack) == 0) or (stack.pop() != c)):
                    return False
        return False if stack else True