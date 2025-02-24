
from typing import List, Union
from decimal import Decimal, InvalidOperation
import re

class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations
    and handles parenthesized expressions.
    """

    OPERATORS = {
        '+': (1, lambda x, y: x + y),
        '-': (1, lambda x, y: x - y),
        '*': (2, lambda x, y: x * y),
        '/': (2, lambda x, y: x / y)
    }

    def __init__(self):
        """Initialize the calculator."""
        self.tokens: List = []

    def tokenize(self, expression: str) -> List[str]:
        """
        Convert an expression string into a list of tokens.

        Args:
            expression (str): The mathematical expression to tokenize.

        Returns:
            List[str]: A list of tokens (numbers, operators, parentheses).

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        # Remove spaces and validate characters
        expression = expression.replace(' ', '')
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters")

        # Use regex to split the expression into tokens
        token_pattern = r'(\d*\.?\d+|[-+*/()])'
        tokens = re.findall(token_pattern, expression)
        
        # Handle unary minus
        result = []
        for i, token in enumerate(tokens):
            if token == '-' and (i == 0 or tokens[i-1] in '(+-*/'):
                result.extend(['0', '-'])
            else:
                result.append(token)
                
        return result

    def validate_parentheses(self, tokens: List[str]) -> bool:
        """
        Check if parentheses are properly balanced.

        Args:
            tokens (List[str]): List of tokens to check.

        Returns:
            bool: True if parentheses are balanced, False otherwise.
        """
        stack = []
        for token in tokens:
            if token == '(':
                stack.append(token)
            elif token == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0

    def to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Convert infix notation to postfix notation using the Shunting Yard algorithm.

        Args:
            tokens (List[str]): List of tokens in infix notation.

        Returns:
            List[str]: List of tokens in postfix notation.
        """
        output = []
        operator_stack = []

        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Remove '('
            else:  # Operator
                while (operator_stack and operator_stack[-1] != '(' and
                       self.OPERATORS[operator_stack[-1]][0] >= self.OPERATORS[token][0]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return output

    def evaluate_postfix(self, tokens: List[str]) -> float:
        """
        Evaluate a postfix expression.

        Args:
            tokens (List[str]): List of tokens in postfix notation.

        Returns:
            float: Result of the evaluation.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
            ValueError: If the expression is invalid.
        """
        stack = []

        for token in tokens:
            if self._is_number(token):
                stack.append(Decimal(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                
                b = stack.pop()
                a = stack.pop()
                
                if token == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero")
                
                result = self.OPERATORS[token][1](a, b)
                stack.append(result)

        if len(stack) != 1:
            raise ValueError("Invalid expression")
            
        return float(stack[0])

    def calculate(self, expression: str) -> float:
        """
        Evaluate a mathematical expression.

        Args:
            expression (str): The mathematical expression to evaluate.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If the expression is invalid.
            ZeroDivisionError: If division by zero is attempted.
        """
        try:
            # Tokenize the expression
            tokens = self.tokenize(expression)
            
            # Validate parentheses
            if not self.validate_parentheses(tokens):
                raise ValueError("Unbalanced parentheses")

            # Convert to postfix and evaluate
            postfix = self.to_postfix(tokens)
            result = self.evaluate_postfix(postfix)
            
            return result

        except (ValueError, ZeroDivisionError) as e:
            raise
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    @staticmethod
    def _is_number(token: str) -> bool:
        """
        Check if a token is a valid number.

        Args:
            token (str): The token to check.

        Returns:
            bool: True if the token is a valid number, False otherwise.
        """
        try:
            Decimal(token)
            return True
        except InvalidOperation:
            return False


# Example usage
if __name__ == "__main__":
    calc = Calculator()
    
    # Test cases
    test_expressions = [
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2.5 * (3 + 4.2)",
        "-2 + 3",
        "10 / 2",
    ]
    
    for expr in test_expressions:
        try:
            result = calc.calculate(expr)
            print(f"{expr} = {result}")
        except Exception as e:
            print(f"Error evaluating {expr}: {str(e)}")
