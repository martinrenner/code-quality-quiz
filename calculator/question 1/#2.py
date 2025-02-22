
from typing import List, Union

class Calculator:
    def __init__(self):
        self.operators = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y,
                          '*': lambda x, y: x * y,
                          '/': lambda x, y: x / y}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression and returns the result.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression contains invalid characters or is malformed.
            ZeroDivisionError: If division by zero is encountered.
        """
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        result = self._evaluate_postfix(postfix)
        return result

    def _tokenize(self, expression: str) -> List[str]:
        """
        Tokenizes the given expression into a list of tokens.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            List[str]: A list of tokens representing the expression.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        tokens = []
        number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if char in self.operators or char in '()':
                    tokens.append(char)
                elif char.isspace():
                    continue
                else:
                    raise ValueError(f"Invalid character: {char}")
        if number:
            tokens.append(number)
        return tokens

    def _infix_to_postfix(self, tokens: List[str]) -> List[Union[str, float]]:
        """
        Converts the infix tokens to postfix notation using the Shunting Yard algorithm.

        Args:
            tokens (List[str]): A list of tokens in infix notation.

        Returns:
            List[Union[str, float]]: A list of tokens in postfix notation.

        Raises:
            ValueError: If the expression contains unbalanced parentheses.
        """
        output = []
        stack = []
        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                output.append(float(token))
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                if not stack:
                    raise ValueError("Unbalanced parentheses")
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.precedence[token] <= self.precedence[stack[-1]]:
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            if stack[-1] == '(':
                raise ValueError("Unbalanced parentheses")
            output.append(stack.pop())
        return output

    def _evaluate_postfix(self, postfix: List[Union[str, float]]) -> float:
        """
        Evaluates the postfix expression and returns the result.

        Args:
            postfix (List[Union[str, float]]): A list of tokens in postfix notation.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ZeroDivisionError: If division by zero is encountered.
        """
        stack = []
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '/' and operand2 == 0:
                    raise ZeroDivisionError("Division by zero")
                result = self.operators[token](operand1, operand2)
                stack.append(result)
        return stack.pop()


if __name__ == '__main__':
    calculator = Calculator()
    while True:
        try:
            expression = input("Enter an arithmetic expression (or 'q' to quit): ")
            if expression == 'q':
                break
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {str(e)}")
