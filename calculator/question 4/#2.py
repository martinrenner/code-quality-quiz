from typing import List, Tuple
import re
from decimal import Decimal, InvalidOperation

class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations
    and follows the order of operations (PEMDAS).
    """

    def __init__(self):
        """Initialize the calculator with allowed operators and their precedence."""
        self.operators = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        Args:
            expression (str): The mathematical expression to evaluate.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If the expression is invalid or contains syntax errors.
            ZeroDivisionError: If division by zero is attempted.
        """
        try:
            # Normalize and validate the expression
            normalized_expr = self._normalize_expression(expression)
            if not self._is_balanced(normalized_expr):
                raise ValueError("Unbalanced parentheses")

            # Convert expression to tokens
            tokens = self._tokenize(normalized_expr)
            
            # Convert to postfix notation and evaluate
            postfix = self._to_postfix(tokens)
            result = self._evaluate_postfix(postfix)
            
            return float(result)

        except (ValueError, ZeroDivisionError) as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the expression by removing spaces and validating characters.

        Args:
            expression (str): The input expression.

        Returns:
            str: Normalized expression.

        Raises:
            ValueError: If invalid characters are found.
        """
        expression = expression.replace(" ", "")
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters")
        return expression

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks if parentheses in the expression are properly balanced.

        Args:
            expression (str): The normalized expression.

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
        Converts the expression string into a list of tokens.

        Args:
            expression (str): The normalized expression.

        Returns:
            List[str]: List of tokens (numbers and operators).
        """
        tokens = []
        number = ""
        
        for i, char in enumerate(expression):
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = ""
                if char in self.operators or char in '()':
                    tokens.append(char)
                    
        if number:
            tokens.append(number)
            
        return tokens

    def _to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Converts infix notation to postfix notation using the Shunting Yard algorithm.

        Args:
            tokens (List[str]): List of tokens in infix notation.

        Returns:
            List[str]: List of tokens in postfix notation.
        """
        output = []
        stack = []

        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '('
            else:
                while (stack and stack[-1] != '(' and 
                       self.operators.get(stack[-1], 0) >= self.operators.get(token, 0)):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    def _evaluate_postfix(self, tokens: List[str]) -> Decimal:
        """
        Evaluates a postfix expression.

        Args:
            tokens (List[str]): List of tokens in postfix notation.

        Returns:
            Decimal: The result of the evaluation.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        stack = []

        for token in tokens:
            if self._is_number(token):
                stack.append(Decimal(token))
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
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)

        return stack[0]

    @staticmethod
    def _is_number(token: str) -> bool:
        """
        Checks if a token is a valid number.

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


# Create calculator instance
calc = Calculator()

# Example calculations
try:
    print(calc.calculate("2 + 3 * 4"))  # Output: 14.0
    print(calc.calculate("(2 + 3) * 4"))  # Output: 20.0
    print(calc.calculate("2.5 + 3.7"))  # Output: 6.2
    print(calc.calculate("10 / 2"))  # Output: 5.0
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
