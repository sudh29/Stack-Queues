class Solution:
    # Function to evaluate a postfix expression.
    def evaluate_postfix(self, S):
        n = len(S)
        stack = []

        for i in range(n):
            if S[i] in ['+', '-', '*', '/']:
                a = stack.pop()
                b = stack.pop()
                
                if S[i] == '+':
                    res = b + a
                elif S[i] == '-':
                    res = b - a
                elif S[i] == '*':
                    res = b * a
                elif S[i] == '/':
                    res = int(b / a)  # Use int() to ensure integer division
                stack.append(res)
            else:
                stack.append(int(S[i]))

        return stack[-1]  # Return the top element of the stack


# Example usage:
solution = Solution()
postfix_expression = "231*+9-"  # Example postfix expression
result = solution.evaluate_postfix(postfix_expression)
print(result)  # Output will depend on the expression
