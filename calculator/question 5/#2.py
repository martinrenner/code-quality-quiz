
from typing import List, Union, Dict
from decimal import Decimal, InvalidOperation
from collections import deque

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions following standard operator precedence.
    Supports: +, -, *, /, (), negative numbers, and decimal numbers.
    """

    def __init__(self):
        """Initialize calculator with operator precedence and supported operators."""
        self.precedence: Dict[str, int] = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        self.operators: set = {'+', '-', '*', '/'}

    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression and return the result.

        Args:
            expression (str): The arithmetic expression to evaluate

        Returns:
            float: The result of the expression evaluation

        Raises:
            ValueError: If the expression is invalid or contains syntax errors
            ZeroDivisionError: If division by zero is attempted
        """
        try:
            # Remove whitespace and validate characters
            expression = self._sanitize_input(expression)
            # Convert infix to postfix notation
            postfix = self._infix_to_postfix(expression)
            # Evaluate postfix expression
            result = self._evaluate_postfix(postfix)
            return float(result)
        except (ValueError, ZeroDivisionError) as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _sanitize_input(self, expression: str) -> str:
        """
        Sanitize and validate the input expression.

        Args:
            expression (str): The input expression

        Returns:
            str: Sanitized expression

        Raises:
            ValueError: If the expression contains invalid characters
        """
        # Remove whitespace
        expression = ''.join(expression.split())
        
        # Validate characters
        valid_chars = set('0123456789.+-*/() ')
        if not all(c in valid_chars for c in expression):
            raise ValueError("Expression contains invalid characters")

        # Validate parentheses
        if not self._check_parentheses(expression):
            raise ValueError("Unbalanced parentheses")

        return expression

    def _check_parentheses(self, expression: str) -> bool:
        """
        Check if parentheses are balanced in the expression.

        Args:
            expression (str): The expression to check

        Returns:
            bool: True if parentheses are balanced, False otherwise
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

    def _infix_to_postfix(self, expression: str) -> List[str]:
        """
        Convert infix expression to postfix notation using Shunting Yard algorithm.

        Args:
            expression (str): The infix expression

        Returns:
            List[str]: The expression in postfix notation
        """
        output: List[str] = []
        operator_stack: List[str] = []
        number = ""
        
        i = 0
        while i < len(expression):
            char = expression[i]

            # Handle numbers (including decimals and negatives)
            if char.isdigit() or char == '.' or (char == '-' and 
                (i == 0 or expression[i-1] in '(+')):
                number += char
                if i == len(expression) - 1 or not (expression[i+1].isdigit() or expression[i+1] == '.'):
                    output.append(number)
                    number = ""
            
            # Handle operators and parentheses
            elif char in self.operators and not number:
                while (operator_stack and operator_stack[-1] != '(' and 
                       self.precedence[char] <= self.precedence[operator_stack[-1]]):
                    output.append(operator_stack.pop())
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()  # Remove '('

            i += 1

        # Append remaining operators
        while operator_stack:
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, postfix: List[str]) -> Decimal:
        """
        Evaluate a postfix expression.

        Args:
            postfix (List[str]): The postfix expression

        Returns:
            Decimal: The result of the evaluation

        Raises:
            ValueError: If the expression is invalid
            ZeroDivisionError: If division by zero is attempted
        """
        stack: deque = deque()

        for token in postfix:
            if token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
                
                b = Decimal(stack.pop())
                a = Decimal(stack.pop())

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
            else:
                try:
                    stack.append(Decimal(token))
                except InvalidOperation:
                    raise ValueError(f"Invalid number: {token}")

        if len(stack) != 1:
            raise ValueError("Invalid expression")

        return stack[0]


calculator = Calculator()

# Basic operations
print(calculator.calculate("2 + 3"))  # 5.0
print(calculator.calculate("2.5 * 4"))  # 10.0
print(calculator.calculate("(2 + 3) * 4"))  # 20.0
print(calculator.calculate("-2 * 3"))  # -6.0


def test_calculator():
    calc = Calculator()
    assert calc.calculate("2 + 3") == 5.0
    assert calc.calculate("2 * (3 + 4)") == 14.0
    assert calc.calculate("-2 * 3") == -6.0
    assert calc.calculate("2.5 / 0.5") == 5.0
    assert calc.calculate("(2 + 3) * (4 + 5)") == 45.0
