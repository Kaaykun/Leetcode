class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        if n % 2 != 0:
            return False

        stack = []
        mappings = {")": "(", "]": "[", "}": "{"}

        for char in s:
            if char in mappings:
                # If the character is a closing bracket
                if not stack or stack[-1] != mappings[char]:
                    # If the stack is empty or the top of the stack is not the corresponding opening bracket
                    return False
                # Remove the corresponding opening bracket from the stack
                stack.pop()
            else:
                # If the character is an opening bracket, push it onto the stack
                stack.append(char)
        # The string is valid if the stack is empty at the end
        return not stack


def main():
    solution = Solution()
    # Test cases: "(())" == True, "()[]{}" == True, "([]{})" == True, "(]" == False
    s = "([]{}[)"
    print(solution.isValid(s))


if __name__ == "__main__":
    main()