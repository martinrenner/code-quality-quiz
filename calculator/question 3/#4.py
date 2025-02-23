
from typing import List, Union
import re

class Token:
    def __init__(self, type: str, value: Union[str, float]):
        self.type = type
        self.value = value

class Calculator:
    def __init__(self):
        self.operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x / y if y != 0 else float('inf'))
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression and returns the result.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the expression evaluation.

        Raises:
            ValueError: If the expression is invalid.
        """
        tokens = self._tokenize(expression)
        postfix_tokens = self._to_postfix(tokens)
        result = self._evaluate_postfix(postfix_tokens)
        return result

    def _tokenize(self, expression: str) -> List[Token]:
        """
        Converts an expression string into a list of tokens.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            List[Token]: A list of tokens representing the expression.

        Raises:
            ValueError: If the expression contains invalid syntax or unbalanced parentheses.
        """
        tokens = []
        number = ''
        for char in expression.replace(' ', ''):
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(Token('NUMBER', float(number)))
                    number = ''
                if char in self.operators:
                    tokens.append(Token('OPERATOR', char))
                elif char == '(':
                    tokens.append(Token('LPAREN', char))
                elif char == ')':
                    tokens.append(Token('RPAREN', char))
                else:
                    raise ValueError(f"Invalid character: {char}")

        if number:
            tokens.append(Token('NUMBER', float(number)))

        # Check for unbalanced parentheses
        paren_count = 0
        for token in tokens:
            if token.type == 'LPAREN':
                paren_count += 1
            elif token.type == 'RPAREN':
                paren_count -= 1
                if paren_count < 0:
                    raise ValueError("Unbalanced parentheses")

        if paren_count != 0:
            raise ValueError("Unbalanced parentheses")

        return tokens

    def _to_postfix(self, tokens: List[Token]) -> List[Token]:
        """
        Converts infix notation to postfix notation (Reverse Polish Notation).

        Args:
            tokens (List[Token]): The infix tokens.

        Returns:
            List[Token]: The postfix tokens.
        """
        output = []
        stack = []
        for token in tokens:
            if token.type == 'NUMBER':
                output.append(token)
            elif token.type == 'OPERATOR':
                while stack and stack[-1].type == 'OPERATOR' and \
                      self.operators[stack[-1].value][0] >= self.operators[token.value][0]:
                    output.append(stack.pop())
                stack.append(token)
            elif token.type == 'LPAREN':
                stack.append(token)
            elif token.type == 'RPAREN':
                while stack and stack[-1].type != 'LPAREN':
                    output.append(stack.pop())
                if stack and stack[-1].type == 'LPAREN':
                    stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")

        while stack:
            if stack[-1].type == 'LPAREN':
                raise ValueError("Mismatched parentheses")
            output.append(stack.pop())

        return output

    def _evaluate_postfix(self, tokens: List[Token]) -> float:
        """
        Evaluates a postfix expression.

        Args:
            tokens (List[Token]): The postfix tokens.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If division by zero occurs.
        """
        stack = []
        for token in tokens:
            if token.type == 'NUMBER':
                stack.append(token.value)
            elif token.type == 'OPERATOR':
                b, a = stack.pop(), stack.pop()
                result = self.operators[token.value][1](a, b)
                if result == float('inf'):
                    raise ValueError("Division by zero")
                stack.append(result)

        if len(stack) != 1:
            raise ValueError("Invalid expression")
        return stack[0]

# Example usage:
if __name__ == "__main__":
    calculator = Calculator()
    expressions = [
        "3 + 4 * 2 / ( 1 - 5 ) ^ 2 ^ 3",
        "10 + 2 * 3",
        "100 / (2 + 3) * 4 - 5",
        "-3 + 4 * -2",
        "3.14 + 2.86"
    ]

    for expr in expressions:
        try:
            result = calculator.calculate(expr)
            print(f"{expr} = {result}")
        except ValueError as e:
            print(f"Error in '{expr}': {str(e)}")
