import re
from typing import List, Union

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions.

    This class supports addition (+), subtraction (-), multiplication (*),
    division (/), and parentheses (), while ensuring the correct order of operations.

    Attributes:
        expression (str): The mathematical expression to be evaluated.
    """

    def __init__(self, expression: str):
        """
        Initializes the Calculator with the given expression.

        Args:
            expression (str): The mathematical expression to be evaluated.

        Raises:
            ValueError: If the input expression is invalid.
        """
        self.expression = self._normalize_expression(expression)

    def calculate(self) -> float:
        """
        Evaluates the mathematical expression.

        Returns:
            float: The result of the calculation.

        Raises:
            ValueError: If the expression is invalid or division by zero occurs.
        """
        if not self._is_valid_expression():
            raise ValueError("Invalid expression")

        tokens = self._tokenize(self.expression)
        result = self._evaluate(tokens)
        return result

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the mathematical expression by removing spaces and validating characters.

        Args:
            expression (str): The input expression.

        Returns:
            str: The normalized expression.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def _is_valid_expression(self) -> bool:
        """
        Checks whether the expression is valid.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        if not self._is_balanced():
            return False

        # Check for consecutive operators or other invalid patterns
        if re.search(r'[\+\-\*/]{2,}', self.expression):
            return False

        if re.search(r'[\+\-\*/]\)$', self.expression):
            return False

        if re.search(r'^\([\+\-\*/]', self.expression):
            return False

        return True

    def _is_balanced(self) -> bool:
        """
        Checks whether the expression has properly paired parentheses.

        Returns:
            bool: True if parentheses are correctly paired, False otherwise.
        """
        stack = []
        for char in self.expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def _tokenize(self, expression: str) -> List[Union[str, float]]:
        """
        Tokenizes the expression into numbers and operators.

        Args:
            expression (str): The normalized expression.

        Returns:
            List[Union[str, float]]: A list of tokens (numbers and operators).
        """
        tokens = []
        current_number = ""
        for char in expression:
            if char in "0123456789.":
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ""
                if char != "(" and char != ")":
                    tokens.append(char)
                else:
                    tokens.append(char)
        if current_number:
            tokens.append(float(current_number))
        return tokens

    def _evaluate(self, tokens: List[Union[str, float]]) -> float:
        """
        Evaluates the tokenized expression using the Shunting Yard algorithm and RPN.

        Args:
            tokens (List[Union[str, float]]): The tokenized expression.

        Returns:
            float: The result of the calculation.

        Raises:
            ValueError: If division by zero occurs.
        """
        def precedence(op: str) -> int:
            if op in "+-": return 1
            if op in "*/": return 2
            return 0

        output_queue = []
        operator_stack = []

        for token in tokens:
            if isinstance(token, float):
                output_queue.append(token)
            elif token == "(":
                operator_stack.append(token)
            elif token == ")":
                while operator_stack and operator_stack[-1] != "(":
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == "(":
                    operator_stack.pop()
                else:
                    raise ValueError("Unbalanced parentheses")
            else:  # operator
                while (operator_stack and operator_stack[-1] != "(" and
                       precedence(operator_stack[-1]) >= precedence(token)):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output_queue.append(operator_stack.pop())

        # Evaluate RPN
        stack = []
        for token in output_queue:
            if isinstance(token, float):
                stack.append(token)
            else:
                b, a = stack.pop(), stack.pop()
                if token == "+":
                    stack.append(a + b)
                elif token == "-":
                    stack.append(a - b)
                elif token == "*":
                    stack.append(a * b)
                elif token == "/":
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)

        return stack[0]


# Example usage
if __name__ == "__main__":
    try:
        calc = Calculator("(2 + 3) * 4 - 6 / 2")
        result = calc.calculate()
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
