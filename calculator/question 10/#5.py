import re
from typing import List, Union

class ExpressionError(Exception):
    """Custom exception for expression-related errors."""
    pass

class Token:
    """Represents a token in the mathematical expression."""

    def __init__(self, type: str, value: Union[str, float]):
        self.type = type
        self.value = value

class Calculator:
    """
    A class that implements a calculator to evaluate arithmetic expressions.
    
    Supports addition (+), subtraction (-), multiplication (*), and division (/)
    as well as correct operator precedence and parentheses.
    """

    def __init__(self):
        self.operators = {
            '+': lambda a, b: a + b,
            '-': lambda a, b: a - b,
            '*': lambda a, b: a * b,
            '/': lambda a, b: a / b if b != 0 else float('inf')
        }
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the mathematical expression and returns the result.

        :param expression: The mathematical expression as a string
        :return: Result of the expression as a float
        :raises ExpressionError: If the expression is invalid
        """
        try:
            # Tokenize the expression
            tokens = self._tokenize(expression)
            # Convert to postfix notation
            postfix = self._infix_to_postfix(tokens)
            # Evaluate the postfix expression
            result = self._evaluate_postfix(postfix)
            return result
        except ExpressionError as e:
            raise ExpressionError(f"Error in expression: {e}")

    def _tokenize(self, expression: str) -> List[Token]:
        """Tokenizes the input expression into a list of tokens."""
        tokens = []
        number = ''
        for char in expression.replace(' ', ''):
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(Token('number', float(number)))
                    number = ''
                if char in self.operators or char in '()':
                    tokens.append(Token('operator', char))
                else:
                    raise ExpressionError(f"Invalid character: {char}")
        if number:
            tokens.append(Token('number', float(number)))
        return self._validate_tokens(tokens)

    def _validate_tokens(self, tokens: List[Token]) -> List[Token]:
        """Validates the tokens, ensuring balanced parentheses and no invalid sequences."""
        stack = []
        for token in tokens:
            if token.type == 'operator' and token.value == '(':
                stack.append(token)
            elif token.type == 'operator' and token.value == ')':
                if not stack or stack[-1].value != '(':
                    raise ExpressionError("Unbalanced parentheses")
                stack.pop()
        if stack:
            raise ExpressionError("Unbalanced parentheses")
        return tokens

    def _infix_to_postfix(self, tokens: List[Token]) -> List[Token]:
        """Converts infix notation to postfix notation using the Shunting Yard algorithm."""
        output = []
        operator_stack = []
        for token in tokens:
            if token.type == 'number':
                output.append(token)
            elif token.type == 'operator':
                if token.value == '(':
                    operator_stack.append(token)
                elif token.value == ')':
                    while operator_stack and operator_stack[-1].value != '(':
                        output.append(operator_stack.pop())
                    if operator_stack and operator_stack[-1].value == '(':
                        operator_stack.pop()
                    else:
                        raise ExpressionError("Unbalanced parentheses")
                else:
                    while (operator_stack and operator_stack[-1].value != '(' and
                           self.precedence[operator_stack[-1].value] >= self.precedence[token.value]):
                        output.append(operator_stack.pop())
                    operator_stack.append(token)
        while operator_stack:
            output.append(operator_stack.pop())
        return output

    def _evaluate_postfix(self, postfix: List[Token]) -> float:
        """Evaluates a postfix expression."""
        stack = []
        for token in postfix:
            if token.type == 'number':
                stack.append(token.value)
            elif token.type == 'operator':
                if len(stack) < 2:
                    raise ExpressionError("Invalid expression")
                b, a = stack.pop(), stack.pop()
                result = self.operators[token.value](a, b)
                stack.append(result)
        if len(stack) != 1:
            raise ExpressionError("Invalid expression")
        return stack[0]
