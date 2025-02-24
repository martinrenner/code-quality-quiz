
from typing import List, Union
import re
from decimal import Decimal, InvalidOperation

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions following operator precedence.
    Supports operations: +, -, *, / and parentheses ().
    """

    def __init__(self):
        """Initialize operator precedence and patterns for token parsing."""
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        self.number_pattern = re.compile(r'-?\d*\.?\d+')

    def calculate(self, expression: str) -> float:
        """
        Evaluate the given arithmetic expression and return the result.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the expression evaluation.

        Raises:
            ValueError: If the expression is invalid or contains syntax errors.
            ZeroDivisionError: If division by zero is attempted.
        """
        try:
            # Remove whitespace and validate characters
            expression = self._sanitize_expression(expression)
            # Convert infix expression to postfix notation
            postfix = self._infix_to_postfix(expression)
            # Evaluate the postfix expression
            result = self._evaluate_postfix(postfix)
            return float(result)
        except (ValueError, ZeroDivisionError) as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _sanitize_expression(self, expression: str) -> str:
        """
        Sanitize and validate the input expression.

        Args:
            expression (str): The input expression.

        Returns:
            str: Sanitized expression.

        Raises:
            ValueError: If the expression contains invalid characters or is malformed.
        """
        # Remove whitespace
        expression = ''.join(expression.split())
        
        # Validate characters
        valid_chars = set('0123456789.+-*/() ')
        if not all(c in valid_chars for c in expression):
            raise ValueError("Expression contains invalid characters")

        # Check for balanced parentheses
        if not self._check_parentheses(expression):
            raise ValueError("Unbalanced parentheses")

        return expression

    def _check_parentheses(self, expression: str) -> bool:
        """
        Check if parentheses in the expression are balanced.

        Args:
            expression (str): The expression to check.

        Returns:
            bool: True if parentheses are balanced, False otherwise.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def _tokenize(self, expression: str) -> List[str]:
        """
        Convert expression string into a list of tokens.

        Args:
            expression (str): The expression to tokenize.

        Returns:
            List[str]: List of tokens.
        """
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            
            # Handle numbers (including decimals and negatives)
            if char.isdigit() or (char == '-' and (i == 0 or expression[i-1] in '(+')):
                match = self.number_pattern.match(expression[i:])
                if match:
                    tokens.append(match.group())
                    i += len(match.group())
                    continue

            # Handle operators and parentheses
            if char in '+-*/()':
                tokens.append(char)
            i += 1
            
        return tokens

    def _infix_to_postfix(self, expression: str) -> List[str]:
        """
        Convert infix expression to postfix notation using Shunting Yard algorithm.

        Args:
            expression (str): The infix expression.

        Returns:
            List[str]: Expression in postfix notation.
        """
        tokens = self._tokenize(expression)
        output = []
        operators = []

        for token in tokens:
            if self.number_pattern.match(token):
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                operators.pop()  # Remove '('
            else:  # Operator
                while (operators and operators[-1] != '(' and
                       self.precedence.get(operators[-1], 0) >= self.precedence.get(token, 0)):
                    output.append(operators.pop())
                operators.append(token)

        while operators:
            output.append(operators.pop())

        return output

    def _evaluate_postfix(self, tokens: List[str]) -> float:
        """
        Evaluate a postfix expression.

        Args:
            tokens (List[str]): The postfix expression tokens.

        Returns:
            float: Result of the evaluation.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
            ValueError: If the expression is invalid.
        """
        stack = []

        for token in tokens:
            if self.number_pattern.match(token):
                stack.append(Decimal(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                
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
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)

        if len(stack) != 1:
            raise ValueError("Invalid expression")
            
        return float(stack[0])


# Example usage
def main():
    calculator = Calculator()
    
    # Test expressions
    test_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2.5 * (3 + 4.2)",
        "-2 * 3.5",
        "10 / 2",
    ]

    for expression in test_expressions:
        try:
            result = calculator.calculate(expression)
            print(f"{expression} = {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error evaluating '{expression}': {str(e)}")

if __name__ == "__main__":
    main()
