import re
from typing import List, Union

class Calculator:
    """
    A class implementing a simple arithmetic calculator.
    Supports addition, subtraction, multiplication, division, and parentheses.
    """

    def __init__(self):
        """Initialize the Calculator with precedence rules and token patterns."""
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.token_pattern = re.compile(r'\s*([()+\-*/]|\d*\.?\d+)\s*')

    def calculate(self, expression: str) -> float:
        """
        Calculate the result of the given arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the expression.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses, invalid characters, division by zero).
        """
        tokens = self.tokenize(expression)
        postfix = self.infix_to_postfix(tokens)
        return self.evaluate_postfix(postfix)

    def tokenize(self, expression: str) -> List[str]:
        """
        Tokenize the input expression into a list of tokens.

        Args:
            expression (str): The input expression to tokenize.

        Returns:
            List[str]: List of tokens.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        tokens = []
        for match in self.token_pattern.finditer(expression):
            token = match.group(1)
            if token in '+-*/()' or token.replace('.', '').isdigit():
                tokens.append(token)
            else:
                raise ValueError(f"Invalid character in expression: {token}")
        return tokens

    def infix_to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Convert infix notation to postfix notation using the Shunting Yard algorithm.

        Args:
            tokens (List[str]): List of tokens in infix notation.

        Returns:
            List[str]: List of tokens in postfix notation.

        Raises:
            ValueError: If the expression has unbalanced parentheses.
        """
        output = []
        operators = []
        for token in tokens:
            if token.replace('.', '').isdigit():
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators or operators.pop() != '(':
                    raise ValueError("Unbalanced parentheses in expression")
            elif token in self.precedence:
                while (operators and operators[-1] != '(' and
                       self.precedence.get(operators[-1], 0) >= self.precedence[token]):
                    output.append(operators.pop())
                operators.append(token)
        
        while operators:
            if operators[-1] == '(':
                raise ValueError("Unbalanced parentheses in expression")
            output.append(operators.pop())
        
        return output

    def evaluate_postfix(self, postfix: List[str]) -> float:
        """
        Evaluate a postfix expression.

        Args:
            postfix (List[str]): List of tokens in postfix notation.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If division by zero is attempted.
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
        result = calc.calculate("(3 + 4) * 2 / (1 - 5)")
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
