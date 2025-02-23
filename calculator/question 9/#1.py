
import re
from typing import List, Union

class Calculator:
    """
    A class that implements a basic arithmetic calculator with support for parentheses.

    Attributes:
        None

    Methods:
        calculate(expression: str) -> float: Evaluates the given arithmetic expression.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.

        Args:
            expression (str): A string containing the arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the input expression is invalid or contains illegal characters.
        """
        # Remove all whitespace from the expression
        expression = expression.replace(" ", "")

        # Validate the expression
        if not self._is_valid_expression(expression):
            raise ValueError("Invalid expression")

        # Convert the expression to Reverse Polish Notation (RPN)
        rpn = self._to_rpn(expression)

        # Evaluate the RPN expression
        result = self._evaluate_rpn(rpn)

        return result

    def _is_valid_expression(self, expression: str) -> bool:
        """
        Validates the given expression for correctness.

        Args:
            expression (str): The arithmetic expression to validate.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        # Check for illegal characters
        if not re.match(r'^[\d\+\-\*\/\(\)\.]+$', expression):
            return False

        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            return False

        # Check for consecutive operators
        if re.search(r'[\+\-\*\/\(\)]+[\+\-\*\/\(\)]+', expression):
            return False

        # Check for numbers at the start and end of the expression
        if not re.match(r'^\-?\d', expression) or not re.search(r'\d$', expression):
            return False

        # Check for division by zero
        if '/0' in expression:
            return False

        return True

    def _to_rpn(self, expression: str) -> List[str]:
        """
        Converts the infix notation expression to Reverse Polish Notation (RPN).

        Args:
            expression (str): The infix notation expression.

        Returns:
            List[str]: The expression in RPN.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []

        for token in re.findall(r'(\d*\.?\d+|[+\-*/()])', expression):
            if token.isdigit() or (token.count('.') == 1 and token.replace('.', '').isdigit()):
                output.append(token)
            elif token in precedence:
                while stack and stack[-1] != '(' and precedence[stack[-1]] >= precedence[token]:
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()

        while stack:
            output.append(stack.pop())

        return output

    def _evaluate_rpn(self, rpn: List[str]) -> float:
        """
        Evaluates an expression in Reverse Polish Notation (RPN).

        Args:
            rpn (List[str]): The expression in RPN.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If division by zero is attempted.
        """
        stack = []

        for token in rpn:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            else:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)

        return stack[0]

# Example usage
if __name__ == "__main__":
    calculator = Calculator()
    while True:
        try:
            expression = input("Enter an arithmetic expression (or 'q' to quit): ")
            if expression.lower() == 'q':
                break
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
