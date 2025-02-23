
class Calculator:
    def __init__(self):
        self.operators = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y,
                          '*': lambda x, y: x * y,
                          '/': lambda x, y: x / y}

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        :param expression: A mathematical expression as a string.
        :return: The normalized expression without spaces.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/().eE ")
        if not all(char in allowed_chars for char in expression):
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

    def parse_expression(self, expression: str) -> list:
        """
        Parses a mathematical expression into a list of tokens.

        :param expression: A string containing the mathematical expression.
        :return: A list of tokens representing the expression.
        """
        tokens = []
        number = ""
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            elif char in self.operators or char in '()':
                if number:
                    tokens.append(float(number))
                    number = ""
                tokens.append(char)
        if number:
            tokens.append(float(number))
        return tokens

    def evaluate(self, tokens: list) -> float:
        """
        Evaluates a list of tokens representing a mathematical expression.

        :param tokens: A list of tokens representing the expression.
        :return: The result of the evaluated expression.
        :raises ZeroDivisionError: If division by zero is encountered.
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                sub_expr = []
                while stack[-1] != '(':
                    sub_expr.append(stack.pop())
                stack.pop()  # Remove '('
                stack.append(self.evaluate(sub_expr[::-1]))
            else:  # Operator
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero.")
                stack.append(self.operators[token](a, b))
        return stack.pop()

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression.

        :param expression: A string containing the mathematical expression.
        :return: The result of the evaluated expression.
        :raises ValueError: If the expression is invalid or contains unbalanced parentheses.
        :raises ZeroDivisionError: If division by zero is encountered.
        """
        normalized_expr = self.normalize_expression(expression)
        if not self.is_balanced(normalized_expr):
            raise ValueError("Unbalanced parentheses.")
        tokens = self.parse_expression(normalized_expr)
        return self.evaluate(tokens)
