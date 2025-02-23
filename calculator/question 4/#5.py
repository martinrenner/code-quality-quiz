
class Calculator:
    def __init__(self):
        self.allowed_chars = set("0123456789+-*/(). ")

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        :param expression: A mathematical expression as a string.
        :return: The normalized expression without spaces.
        :raises ValueError: If the expression contains invalid characters.
        """
        if not all(char in self.allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def is_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

        :param expression: A string containing the mathematical expression.
        :return: True if parentheses are correctly paired, otherwise False.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def tokenize(self, expression: str) -> list:
        """
        Tokenizes the expression into numbers, operators, and parentheses.

        :param expression: A normalized mathematical expression.
        :return: A list of tokens.
        """
        tokens = []
        i = 0
        while i < len(expression):
            if expression[i] in "0123456789.":
                j = i
                while j < len(expression) and (expression[j] in "0123456789."):
                    j += 1
                tokens.append(expression[i:j])
                i = j
            else:
                tokens.append(expression[i])
                i += 1
        return tokens

    def infix_to_postfix(self, tokens: list) -> list:
        """
        Converts an infix expression to a postfix expression using the Shunting Yard algorithm.

        :param tokens: A list of tokens from the tokenized expression.
        :return: A list of tokens in postfix notation.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        stack = []
        output = []

        for token in tokens:
            if token.isnumeric() or self.is_float(token):
                output.append(token)
            elif token in precedence:
                while (stack and stack[-1] in precedence and
                       precedence[stack[-1]] >= precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove the '(' from the stack

        while stack:
            output.append(stack.pop())

        return output

    def is_float(self, token: str) -> bool:
        """
        Checks if a token is a float.

        :param token: A token from the tokenized expression.
        :return: True if the token is a float, otherwise False.
        """
        try:
            float(token)
            return True
        except ValueError:
            return False

    def evaluate_postfix(self, postfix: list) -> float:
        """
        Evaluates a postfix expression.

        :param postfix: A list of tokens in postfix notation.
        :return: The result of the evaluation.
        :raises ZeroDivisionError: If division by zero is attempted.
        """
        stack = []

        for token in postfix:
            if token.isnumeric() or self.is_float(token):
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero.")
                    stack.append(a / b)

        return stack[0]

    def calculate(self, expression: str) -> float:
        """
        Evaluates the mathematical expression.

        :param expression: A mathematical expression as a string.
        :return: The result of the evaluation.
        :raises ValueError: If the expression contains invalid characters or unbalanced parentheses.
        :raises ZeroDivisionError: If division by zero is attempted.
        """
        expression = self.normalize_expression(expression)
        if not self.is_balanced(expression):
            raise ValueError("Unbalanced parentheses.")

        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        result = self.evaluate_postfix(postfix)

        return result

# Example usage:
# calc = Calculator()
# result = calc.calculate("3 + 5 * (2 - 8)")
# print(result)
