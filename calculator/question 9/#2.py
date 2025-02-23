
import re
from typing import List, Tuple

class Calculator:
    """
    A class to handle arithmetic calculations on mathematical expressions.

    This class provides methods to evaluate expressions with support for addition,
    subtraction, multiplication, division, and parentheses, ensuring correct operator
    precedence and input validation.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        :param expression: A string containing a valid mathematical expression.
        :return: The result of the evaluated expression as a float.
        :raises ValueError: If the expression is invalid or contains invalid operations.
        """
        # Normalize and validate the input expression
        normalized_expr = self._normalize_expression(expression)
        self._validate_expression(normalized_expr)

        # Convert to postfix notation and evaluate
        postfix = self._to_postfix(normalized_expr)
        result = self._evaluate_postfix(postfix)

        return result

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        :param expression: A mathematical expression as a string.
        :return: The normalized expression without spaces.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")
        
        return expression.replace(" ", "")

    def _validate_expression(self, expression: str) -> None:
        """
        Validates the mathematical expression for correctness.

        :param expression: The expression to validate.
        :raises ValueError: If the expression has unbalanced parentheses or invalid operations.
        """
        if not self._is_balanced(expression):
            raise ValueError("Unbalanced parentheses in the expression.")
        
        if not self._is_valid_operation(expression):
            raise ValueError("Invalid operation in the expression.")

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

        :param expression: A string containing the mathematical expression.
        :return: True if parentheses are correctly paired, otherwise False.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def _is_valid_operation(self, expression: str) -> bool:
        """
        Checks if the operations in the expression are valid.

        :param expression: The expression to check.
        :return: True if operations are valid, False otherwise.
        """
        operators = set("+-*/")
        prev_char = None
        for char in expression:
            if char in operators and prev_char in operators:
                return False
            prev_char = char
        return True

    def _to_postfix(self, expression: str) -> List[str]:
        """
        Converts an infix expression to postfix notation.

        :param expression: An infix expression as a string.
        :return: A list of tokens in postfix notation.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []

        for token in re.findall(r'\d+\.?\d*|\+|\-|*|/|\(|\)', expression):
            if token.isdigit() or (token.count('.') == 1 and token.replace('.', '').isdigit()):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")
            else:
                while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(token, 0):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output.append(stack.pop())

        return output

    def _evaluate_postfix(self, postfix: List[str]) -> float:
        """
        Evaluates a postfix expression.

        :param postfix: A list of tokens in postfix notation.
        :return: The result of the evaluation as a float.
        :raises ValueError: If there is a division by zero or other invalid operation.
        """
        stack = []
        for token in postfix:
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
    calc = Calculator()
    try:
        result = calc.calculate("(2 + 3) * 4 - 6 / 2")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
