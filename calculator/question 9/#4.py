
import re
from typing import List, Union

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions following the order of operations.
    Supports addition, subtraction, multiplication, division, and parentheses.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given mathematical expression.

        :param expression: A string representing the mathematical expression.
        :return: The result of the expression as a float.
        :raises ValueError: If the expression is invalid or contains invalid operations.
        """
        # Normalize the expression
        normalized_expr = self._normalize_expression(expression)
        
        # Validate the expression
        if not self._is_valid_expression(normalized_expr):
            raise ValueError("Invalid expression")

        # Evaluate the expression
        result = self._evaluate_expression(normalized_expr)
        
        return result
    
    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the input expression by removing spaces and validating characters.

        :param expression: The input expression as a string.
        :return: The normalized expression.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")
        
        return expression.replace(" ", "")

    def _is_valid_expression(self, expression: str) -> bool:
        """
        Validates the expression for proper structure and balanced parentheses.

        :param expression: The normalized expression to validate.
        :return: True if the expression is valid, False otherwise.
        """
        # Check for balanced parentheses
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        if stack:
            return False

        # Check for consecutive operators
        if re.search(r'[+\-*/]{2,}', expression):
            return False

        # Check for division by zero
        if re.search(r'/0(\D|$)', expression):
            return False

        # Check for proper structure
        if not re.match(r'^(\d+|\((\d+|\((\d+|\(\d+\))*\))*\))((\+|\-|*|/)(\d+|\((\d+|\((\d+|\(\d+\))*\))*\)))*$', expression):
            return False

        return True

    def _evaluate_expression(self, expression: str) -> float:
        """
        Evaluates the normalized and validated expression.

        :param expression: The normalized and validated expression.
        :return: The result of the expression as a float.
        """
        # Handle parentheses first
        while '(' in expression:
            expression = re.sub(r'\(([^()]+)\)', lambda m: str(self._evaluate_expression(m.group(1))), expression)

        # Evaluate multiplication and division
        while '*' in expression or '/' in expression:
            expression = re.sub(r'(-?\d+(?:\.\d+)?)([*/])(-?\d+(?:\.\d+)?)', 
                                lambda m: str(self._apply_operation(float(m.group(1)), m.group(2), float(m.group(3)))), 
                                expression)

        # Evaluate addition and subtraction
        result = float(re.split(r'([+\-])', expression)[0])
        for i in range(1, len(re.split(r'([+\-])', expression)) - 1, 2):
            operation = re.split(r'([+\-])', expression)[i]
            number = float(re.split(r'([+\-])', expression)[i + 1])
            result = self._apply_operation(result, operation, number)

        return result

    def _apply_operation(self, a: float, operator: str, b: float) -> float:
        """
        Applies the specified operation to two numbers.

        :param a: The first number.
        :param b: The second number.
        :param operator: The operation to apply ('+', '-', '*', or '/').
        :return: The result of the operation.
        :raises ValueError: If an invalid operator is provided or division by zero is attempted.
        """
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise ValueError("Division by zero")
            return a / b
        else:
            raise ValueError(f"Invalid operator: {operator}")
