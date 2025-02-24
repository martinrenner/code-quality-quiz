from typing import List, Union, Optional
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import re

@dataclass
class Token:
    """Represents a token in the mathematical expression."""
    type: str
    value: str

class Calculator:
    """A calculator that evaluates arithmetic expressions with proper operator precedence."""

    OPERATORS = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    def __init__(self):
        """Initializes the calculator."""
        self.tokens: List[Token] = []

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
            
            # Tokenize the expression
            self.tokens = self._tokenize(normalized_expr)
            
            # Convert to postfix notation and evaluate
            result = self._evaluate_postfix(self._to_postfix())
            
            return float(result)

        except (ValueError, ZeroDivisionError) as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes and validates the input expression.

        Args:
            expression (str): The input expression.

        Returns:
            str: Normalized expression.

        Raises:
            ValueError: If the expression contains invalid characters or structure.
        """
        # Remove whitespace
        expr = expression.replace(" ", "")
        
        # Validate characters
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expr):
            raise ValueError("Expression contains invalid characters")

        # Check parentheses balance
        if not self._is_balanced_parentheses(expr):
            raise ValueError("Unbalanced parentheses")

        return expr

    def _is_balanced_parentheses(self, expression: str) -> bool:
        """
        Checks if parentheses are properly balanced.

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

    def _tokenize(self, expression: str) -> List[Token]:
        """
        Converts the expression string into a list of tokens.

        Args:
            expression (str): The normalized expression.

        Returns:
            List[Token]: List of tokens.
        """
        tokens = []
        number = ''
        
        for i, char in enumerate(expression):
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(Token('NUMBER', number))
                    number = ''
                if char in self.OPERATORS or char in '()':
                    tokens.append(Token('OPERATOR', char))
                    
        if number:
            tokens.append(Token('NUMBER', number))
            
        return tokens

    def _to_postfix(self) -> List[Token]:
        """
        Converts the tokens to postfix notation using the Shunting Yard algorithm.

        Returns:
            List[Token]: Tokens in postfix notation.
        """
        output = []
        operator_stack = []

        for token in self.tokens:
            if token.type == 'NUMBER':
                output.append(token)
            elif token.value == '(':
                operator_stack.append(token)
            elif token.value == ')':
                while operator_stack and operator_stack[-1].value != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Remove '('
            else:
                while (operator_stack and operator_stack[-1].value != '(' and
                       self.OPERATORS[operator_stack[-1].value] >= 
                       self.OPERATORS[token.value]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, postfix: List[Token]) -> Decimal:
        """
        Evaluates a postfix expression.

        Args:
            postfix (List[Token]): The postfix expression tokens.

        Returns:
            Decimal: The result of the evaluation.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
            ValueError: If the expression is invalid.
        """
        stack = []

        for token in postfix:
            if token.type == 'NUMBER':
                try:
                    stack.append(Decimal(token.value))
                except InvalidOperation:
                    raise ValueError(f"Invalid number: {token.value}")
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                    
                b = stack.pop()
                a = stack.pop()

                if token.value == '+':
                    stack.append(a + b)
                elif token.value == '-':
                    stack.append(a - b)
                elif token.value == '*':
                    stack.append(a * b)
                elif token.value == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        return stack[0]


calculator = Calculator()

# Example calculations
print(calculator.calculate("2 + 3 * 4"))  # Output: 14.0
print(calculator.calculate("(2 + 3) * 4"))  # Output: 20.0
print(calculator.calculate("2.5 + 3.7"))  # Output: 6.2
