
import re
from typing import List, Union

class Calculator:
    """
    A calculator capable of evaluating arithmetic expressions.

    This calculator supports addition, subtraction, multiplication, 
    and division with correct operator precedence and parentheses.
    """

    def __init__(self):
        """Initialize the calculator with operator precedence."""
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression.

        Args:
            expression (str): The expression to evaluate.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If the expression is invalid or contains invalid operations.
        """
        # Normalize the expression
        expression = self._normalize_expression(expression)

        # Validate the expression
        self._validate_expression(expression)

        # Convert to postfix notation
        postfix = self._infix_to_postfix(expression)

        # Evaluate the postfix expression
        result = self._evaluate_postfix(postfix)

        return result

    def _normalize_expression(self, expression: str) -> str:
        """Normalize the expression by removing whitespace and handling unary operators."""
        # Remove all whitespace
        expression = re.sub(r'\s+', '', expression)

        # Handle unary minus
        expression = re.sub(r'(-(?!\d)|-(?=\())', '0-', expression)

        # Add '0+' at the beginning if expression starts with '('
        if expression.startswith('('):
            expression = '0+' + expression

        return expression

    def _validate_expression(self, expression: str) -> None:
        """Validate the expression for correctness."""
        # Check for invalid characters
        if not re.match(r'^[0-9+\-*/().]+$', expression):
            raise ValueError("Invalid characters in expression")

        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses")

        # Check for consecutive operators
        if re.search(r'[+\-*/]{2,}', expression):
            raise ValueError("Consecutive operators found")

    def _infix_to_postfix(self, expression: str) -> List[str]:
        """Convert infix expression to postfix notation."""
        output = []
        stack = []
        number = ''

        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    output.append(number)
                    number = ''

                if char == '(':
                    stack.append(char)
                elif char == ')':
                    while stack and stack[-1] != '(':
                        output.append(stack.pop())
                    if stack and stack[-1] == '(':
                        stack.pop()
                    else:
                        raise ValueError("Mismatched parentheses")
                elif char in self.precedence:
                    while stack and stack[-1] != '(' and self.precedence.get(stack[-1], 0) >= self.precedence[char]:
                        output.append(stack.pop())
                    stack.append(char)

        if number:
            output.append(number)

        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output.append(stack.pop())

        return output

    def _evaluate_postfix(self, postfix: List[str]) -> float:
        """Evaluate a postfix expression."""
        stack = []

        for token in postfix:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
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

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        return stack[0]


# Example usage
if __name__ == "__main__":
    calculator = Calculator()
    
    # Test cases
    expressions = [
        "3 + 4 * 2 / ( 1 - 5 )",
        "10 + 3 * 2 - 5 / 2",
        "(2 + 3) * (4 - 1)",
        "2 * (3 + 4) - 5",
        "-3 * (2 + 4) / 2",
        "0.1 + 0.2",
        "-1 - (-2)",
    ]

    for expr in expressions:
        try:
            result = calculator.calculate(expr)
            print(f"{expr} = {result}")
        except ValueError as e:
            print(f"Error in '{expr}': {str(e)}")
