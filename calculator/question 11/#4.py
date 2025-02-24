import re
from typing import List, Union

class Calculator:
    def __init__(self):
        self.allowed_chars = set("0123456789+-*/(). ")

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
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

    def tokenize(self, expression: str) -> List[Union[float, str]]:
        """
        Tokenizes the mathematical expression into numbers, operators, and parentheses.

        Args:
            expression (str): A normalized mathematical expression.

        Returns:
            List[Union[float, str]]: A list of tokens.
        """
        tokens = re.findall(r'\d+\.\d+|\d+|[+*/()-]', expression)
        return [float(token) if re.match(r'\d+\.\d+|\d+', token) else token for token in tokens]

    def evaluate_expression(self, tokens: List[Union[float, str]]) -> float:
        """
        Evaluates a tokenized mathematical expression.

        Args:
            tokens (List[Union[float, str]]): A list of tokens.

        Returns:
            float: The result of the expression.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        def apply_operator(operators, values):
            operator = operators.pop()
            right = values.pop()
            left = values.pop()
            if operator == '+':
                values.append(left + right)
            elif operator == '-':
                values.append(left - right)
            elif operator == '*':
                values.append(left * right)
            elif operator == '/':
                if right == 0:
                    raise ZeroDivisionError("Division by zero")
                values.append(left / right)

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        values = []
        operators = []
        i = 0

        while i < len(tokens):
            if isinstance(tokens[i], float):
                values.append(tokens[i])
            elif tokens[i] == '(':
                operators.append(tokens[i])
            elif tokens[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
            else:
                while (operators and operators[-1] in precedence and
                       precedence[operators[-1]] >= precedence[tokens[i]]):
                    apply_operator(operators, values)
                operators.append(tokens[i])
            i += 1

        while operators:
            apply_operator(operators, values)

        return values[0]

    def calculate(self, expression: str) -> float:
        """
        Evaluates the mathematical expression.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            float: The result of the expression.

        Raises:
            ValueError: If the expression is invalid.
            ZeroDivisionError: If division by zero is attempted.
        """
        expression = self.normalize_expression(expression)
        if not self.is_balanced(expression):
            raise ValueError("Unbalanced parentheses")

        tokens = self.tokenize(expression)
        return self.evaluate_expression(tokens)

# Example usage:
if __name__ == "__main__":
    calculator = Calculator()
    try:
        result = calculator.calculate("3 + 5 * (2 - 8)")
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
