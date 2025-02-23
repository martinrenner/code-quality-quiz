
import re
from typing import List, Union

class Calculator:
    """
    A class that implements a console-based arithmetic calculator.
    It supports operations like addition, subtraction, multiplication, and division,
    along with handling parentheses and operator precedence.
    """

    def __init__(self):
        self.operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else float('inf')
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.

        Args:
            expression (str): The mathematical expression to be evaluated.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the input expression is invalid or contains division by zero.
        """
        self._validate_expression(expression)
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        result = self._evaluate_postfix(postfix)
        return result

    def _validate_expression(self, expression: str) -> None:
        """
        Validates the input expression for correctness.

        Args:
            expression (str): The mathematical expression to be validated.

        Raises:
            ValueError: If the expression is invalid.
        """
        if not re.match(r'^[\d\s\+\-\*\/\(\)]+$', expression):
            raise ValueError("Invalid characters in the expression.")
        
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses in the expression.")

    def _tokenize(self, expression: str) -> List[str]:
        """
        Converts the expression into a list of tokens.

        Args:
            expression (str): The mathematical expression to be tokenized.

        Returns:
            List[str]: A list of tokens.
        """
        return re.findall(r'\d+\.?\d*|\+|\-|*|\/|\(|\)', expression)

    def _infix_to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Converts an infix expression to postfix notation.

        Args:
            tokens (List[str]): The list of tokens in infix notation.

        Returns:
            List[str]: The list of tokens in postfix notation.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        stack = []

        for token in tokens:
            if token.isdigit() or (token.replace('.', '', 1).isdigit() and token.count('.') <= 1):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    raise ValueError("Mismatched parentheses in the expression.")
            else:
                while stack and stack[-1] != '(' and precedence.get(token, 0) <= precedence.get(stack[-1], 0):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            if stack[-1] == '(':
                raise ValueError("Mismatched parentheses in the expression.")
            output.append(stack.pop())

        return output

    def _evaluate_postfix(self, postfix: List[str]) -> float:
        """
        Evaluates an expression in postfix notation.

        Args:
            postfix (List[str]): The list of tokens in postfix notation.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression results in division by zero.
        """
        stack = []

        for token in postfix:
            if token.replace('.', '', 1).isdigit():
                stack.append(float(token))
            else:
                b, a = stack.pop(), stack.pop()
                result = self.operators[token](a, b)
                if result == float('inf'):
                    raise ValueError("Division by zero.")
                stack.append(result)

        return stack[0]


if __name__ == "__main__":
    calculator = Calculator()
    while True:
        expression = input("Enter an expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        try:
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
