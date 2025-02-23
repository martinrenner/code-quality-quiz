
import re
from typing import Union


class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction,
    multiplication, division, and parentheses.  It handles operator precedence
    and input validation.
    """

    def __init__(self):
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression string and returns the result.

        Args:
            expression: The mathematical expression to evaluate (e.g., "1 + 2 * (3 - 1)").

        Returns:
            The result of the evaluation as a float.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                        invalid characters, division by zero).
        """
        try:
            tokens = self._tokenize(expression)
            postfix_tokens = self._infix_to_postfix(tokens)
            result = self._evaluate_postfix(postfix_tokens)
            return result
        except (ValueError, TypeError, ArithmeticError) as e:
            raise ValueError(f"Invalid expression: {e}") from e

    def _tokenize(self, expression: str) -> list[str]:
        """
        Tokenizes the input expression into numbers, operators, and parentheses.

        Args:
            expression: The mathematical expression string.

        Returns:
            A list of tokens (e.g., ["1", "+", "2", "*", "(", "3", "-", "1", ")"]).

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        # Regular expression to split the expression into tokens
        tokens = re.findall(r"(\d+\.?\d*|\+|\-|\*|\/|\(|\))", expression)

        # Validate characters
        for token in tokens:
            if not re.match(r"^\d+\.?\d*$|^[\+\-\*\/\(\)]$?", token):  # Improved regex
                raise ValueError(f"Invalid character: {token}")
        return tokens

    def _infix_to_postfix(self, tokens: list[str]) -> list[str]:
        """
        Converts a list of tokens from infix notation to postfix notation (Reverse Polish Notation).

        Args:
            tokens: A list of tokens in infix notation.

        Returns:
            A list of tokens in postfix notation.

        Raises:
            ValueError: If parentheses are unbalanced.
        """
        output_queue = []
        operator_stack = []
        for token in tokens:
            if re.match(r"^\d+\.?\d*$", token):  # Check if it is a number
                output_queue.append(token)
            elif token in self.precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       self.precedence[operator_stack[-1]] >= self.precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Unbalanced parentheses")
                operator_stack.pop()  # Pop the '('

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Unbalanced parentheses")
            output_queue.append(operator_stack.pop())

        return output_queue

    def _evaluate_postfix(self, tokens: list[str]) -> float:
        """
        Evaluates a list of tokens in postfix notation.

        Args:
            tokens: A list of tokens in postfix notation.

        Returns:
            The result of the evaluation as a float.

        Raises:
            ValueError: If the expression is invalid (e.g., division by zero).
        """
        operand_stack = []
        for token in tokens:
            if re.match(r"^\d+\.?\d*$", token):  # Check if it is a number.
                operand_stack.append(float(token))
            elif token in self.precedence:
                if len(operand_stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands")
                try:
                    operand2 = operand_stack.pop()
                    operand1 = operand_stack.pop()
                except IndexError:
                    raise ValueError("Invalid Expression: Not enough operands")

                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    if operand2 == 0:
                        raise ZeroDivisionError("Division by zero")
                    result = operand1 / operand2
                operand_stack.append(result)
        if len(operand_stack) != 1:
          raise ValueError("Invalid expression: too many operands")
        return operand_stack[0]
def main():
    calculator = Calculator()
    while True:
        expression = input("Enter an expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        try:
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    main()
