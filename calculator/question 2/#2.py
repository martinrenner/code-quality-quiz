
from typing import List, Union

class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        :param expression: The mathematical expression as a string.
        :return: The result of the expression as a floating-point number.
        :raises ValueError: If the expression is invalid or division by zero occurs.
        """
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        return self._evaluate_postfix(postfix)

    def _tokenize(self, expression: str) -> List[Union[str, float]]:
        """
        Tokenizes the expression into a list of operators, parentheses, and numbers.

        :param expression: The mathematical expression as a string.
        :return: A list of tokens representing the expression.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/().eE ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        tokens = []
        number = ""
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            elif char in 'eE' and number:
                number += char
            else:
                if number:
                    tokens.append(float(number))
                    number = ""
                if char != ' ':
                    tokens.append(char)
        if number:
            tokens.append(float(number))
        return tokens

    def _infix_to_postfix(self, tokens: List[Union[str, float]]) -> List[Union[str, float]]:
        """
        Converts an infix expression to postfix notation.

        :param tokens: A list of tokens representing the infix expression.
        :return: A list of tokens representing the postfix expression.
        :raises ValueError: If the expression has unbalanced parentheses.
        """
        stack = []
        postfix = []
        for token in tokens:
            if isinstance(token, float):
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if not stack:
                    raise ValueError("Unbalanced parentheses.")
                stack.pop()
            else:
                while stack and stack[-1] != '(' and self.operators[token] <= self.operators[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(token)
        while stack:
            if stack[-1] == '(':
                raise ValueError("Unbalanced parentheses.")
            postfix.append(stack.pop())
        return postfix

    def _evaluate_postfix(self, postfix: List[Union[str, float]]) -> float:
        """
        Evaluates a postfix expression and returns the result.

        :param postfix: A list of tokens representing the postfix expression.
        :return: The result of the expression as a floating-point number.
        :raises ValueError: If division by zero occurs.
        """
        stack = []
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                right = stack.pop()
                left = stack.pop()
                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                elif token == '/':
                    if right == 0:
                        raise ValueError("Division by zero.")
                    stack.append(left / right)
        return stack.pop()
