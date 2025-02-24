from typing import List, Union, Optional
from decimal import Decimal, InvalidOperation
import re

class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations and parentheses.
    Implements the requirements of ISO/IEC 25010 for software quality.
    """

    OPERATORS = {
        '+': (1, lambda x, y: x + y),
        '-': (1, lambda x, y: x - y),
        '*': (2, lambda x, y: x * y),
        '/': (2, lambda x, y: x / y)
    }

    def __init__(self):
        """Initialize the calculator with empty state."""
        self.tokens: List[str] = []
        
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
            if not self._validate_expression(normalized_expr):
                raise ValueError("Invalid expression syntax")

            # Tokenize the expression
            self.tokens = self._tokenize(normalized_expr)
            
            # Convert to postfix and evaluate
            result = self._evaluate_postfix(self._to_postfix())
            
            return float(result)
            
        except (ValueError, ZeroDivisionError) as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the input expression by removing spaces and validating characters.

        Args:
            expression (str): The input mathematical expression.

        Returns:
            str: Normalized expression.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        # Remove all whitespace
        expr = expression.replace(" ", "")
        
        # Validate characters
        allowed_chars = set("0123456789+-*/.()")
        if not all(char in allowed_chars for char in expr):
            raise ValueError("Expression contains invalid characters")
            
        return expr

    def _validate_expression(self, expression: str) -> bool:
        """
        Validates the expression syntax.

        Args:
            expression (str): The normalized expression to validate.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        # Check parentheses balance
        parentheses_count = 0
        for char in expression:
            if char == '(':
                parentheses_count += 1
            elif char == ')':
                parentheses_count -= 1
            if parentheses_count < 0:
                return False
                
        if parentheses_count != 0:
            return False

        # Check for invalid operator combinations
        if re.search(r'[+\-*/]{2,}', expression):
            return False
            
        # Check if expression starts with valid character
        if not expression[0] in '0123456789.(':
            return False
            
        return True

    def _tokenize(self, expression: str) -> List[str]:
        """
        Converts the expression string into a list of tokens.

        Args:
            expression (str): The normalized expression to tokenize.

        Returns:
            List[str]: List of tokens.
        """
        tokens = []
        current_number = ''
        
        for char in expression:
            if char in '0123456789.':
                current_number += char
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ''
                tokens.append(char)
                
        if current_number:
            tokens.append(current_number)
            
        return tokens

    def _to_postfix(self) -> List[str]:
        """
        Converts the tokenized infix expression to postfix notation.

        Returns:
            List[str]: The expression in postfix notation.
        """
        output = []
        operator_stack = []
        
        for token in self.tokens:
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
                       self.OPERATORS[token][0] <= self.OPERATORS[operator_stack[-1]][0]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
                
        while operator_stack:
            output.append(operator_stack.pop())
            
        return output

    def _evaluate_postfix(self, postfix: List[str]) -> Decimal:
        """
        Evaluates a postfix expression.

        Args:
            postfix (List[str]): The expression in postfix notation.

        Returns:
            Decimal: The result of the evaluation.

        Raises:
            ValueError: If the expression is invalid.
            ZeroDivisionError: If division by zero is attempted.
        """
        stack = []
        
        for token in postfix:
            if self._is_number(token):
                stack.append(Decimal(token))
            else:
                b = stack.pop()
                a = stack.pop()
                
                if token == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero")
                    
                result = self.OPERATORS[token][1](a, b)
                stack.append(result)
                
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
print(calc.calculate("2 + 3 * 4"))  # Output: 14.0
print(calc.calculate("(2 + 3) * 4"))  # Output: 20.0
print(calc.calculate("2.5 + 3.5"))  # Output: 6.0


try:
    calc.calculate("2 + / 3")  # Raises ValueError for invalid syntax
    calc.calculate("2 / 0")    # Raises ZeroDivisionError
    calc.calculate("2 + @")    # Raises ValueError for invalid characters
except ValueError as e:
    print(f"Error: {e}")
except ZeroDivisionError as e:
    print(f"Error: {e}")
