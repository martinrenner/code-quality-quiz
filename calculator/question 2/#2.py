
from typing import List, Union, Optional
from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import re

@dataclass
class Token:
    """Represents a token in the mathematical expression."""
    type: str  # 'NUMBER', 'OPERATOR', 'PARENTHESIS'
    value: str

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions.
    Supports operations: +, -, *, / and parentheses ().
    """
    
    OPERATORS = {
        '+': (1, lambda x, y: x + y),
        '-': (1, lambda x, y: x - y),
        '*': (2, lambda x, y: x * y),
        '/': (2, lambda x, y: x / y)
    }

    def __init__(self):
        """Initialize the calculator."""
        self.tokens: List[Token] = []

    def tokenize(self, expression: str) -> None:
        """
        Convert the input expression into tokens.

        Args:
            expression: The mathematical expression to tokenize.

        Raises:
            ValueError: If the expression contains invalid characters or format.
        """
        # Remove whitespace and validate characters
        expression = expression.replace(' ', '')
        if not re.match(r'^[\d+\-*/().]+$', expression):
            raise ValueError("Expression contains invalid characters")

        # Convert expression to tokens
        number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    self.tokens.append(Token('NUMBER', number))
                    number = ''
                if char in '()':
                    self.tokens.append(Token('PARENTHESIS', char))
                elif char in self.OPERATORS:
                    self.tokens.append(Token('OPERATOR', char))
        if number:
            self.tokens.append(Token('NUMBER', number))

    def validate_tokens(self) -> None:
        """
        Validate the token sequence.

        Raises:
            ValueError: If the token sequence is invalid.
        """
        parentheses_count = 0
        for i, token in enumerate(self.tokens):
            if token.type == 'PARENTHESIS':
                if token.value == '(':
                    parentheses_count += 1
                else:
                    parentheses_count -= 1
                if parentheses_count < 0:
                    raise ValueError("Unmatched parentheses")

            if token.type == 'OPERATOR':
                if i == 0 or i == len(self.tokens) - 1:
                    raise ValueError("Invalid operator position")
                if self.tokens[i-1].type == 'OPERATOR':
                    raise ValueError("Consecutive operators not allowed")

        if parentheses_count != 0:
            raise ValueError("Unmatched parentheses")

    def evaluate_expression(self, tokens: List[Token]) -> Decimal:
        """
        Evaluate a list of tokens using the Shunting Yard algorithm.

        Args:
            tokens: List of tokens to evaluate.

        Returns:
            The result of the expression evaluation.

        Raises:
            ValueError: If the expression is invalid or division by zero occurs.
        """
        output_queue: List[Decimal] = []
        operator_stack: List[str] = []

        for token in tokens:
            if token.type == 'NUMBER':
                try:
                    output_queue.append(Decimal(token.value))
                except InvalidOperation:
                    raise ValueError(f"Invalid number format: {token.value}")
            
            elif token.type == 'OPERATOR':
                while (operator_stack and operator_stack[-1] != '(' and
                       self.OPERATORS[token.value][0] <= self.OPERATORS[operator_stack[-1]][0]):
                    self._apply_operator(output_queue, operator_stack.pop())
                operator_stack.append(token.value)
            
            elif token.value == '(':
                operator_stack.append(token.value)
            
            elif token.value == ')':
                while operator_stack and operator_stack[-1] != '(':
                    self._apply_operator(output_queue, operator_stack.pop())
                if operator_stack:
                    operator_stack.pop()  # Remove '('

        while operator_stack:
            self._apply_operator(output_queue, operator_stack.pop())

        if len(output_queue) != 1:
            raise ValueError("Invalid expression")
        
        return output_queue[0]

    def _apply_operator(self, stack: List[Decimal], operator: str) -> None:
        """
        Apply an operator to the top two values in the stack.

        Args:
            stack: The operand stack.
            operator: The operator to apply.

        Raises:
            ValueError: If division by zero is attempted.
        """
        if len(stack) < 2:
            raise ValueError("Invalid expression")
        
        b = stack.pop()
        a = stack.pop()
        
        try:
            if operator == '/' and b == 0:
                raise ValueError("Division by zero")
            result = self.OPERATORS[operator][1](a, b)
            stack.append(result)
        except (OverflowError, InvalidOperation):
            raise ValueError("Arithmetic error")

    def calculate(self, expression: str) -> float:
        """
        Calculate the result of a mathematical expression.

        Args:
            expression: The mathematical expression to evaluate.

        Returns:
            The result of the calculation as a float.

        Raises:
            ValueError: If the expression is invalid.
        """
        self.tokens = []
        self.tokenize(expression)
        self.validate_tokens()
        result = self.evaluate_expression(self.tokens)
        return float(result)


def main():
    calculator = Calculator()
    
    try:
        # Test cases
        expressions = [
            "2 + 3 * 4",
            "(2 + 3) * 4",
            "2.5 * (3 + 4.2)",
            "10 / (2 + 3)",
            "-2 + 3"
        ]
        
        for expr in expressions:
            result = calculator.calculate(expr)
            print(f"{expr} = {result}")
            
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
