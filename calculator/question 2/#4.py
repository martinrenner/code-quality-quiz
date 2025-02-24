from typing import List, Tuple

class Calculator:
    """
    A class for performing arithmetic calculations with support for operator precedence and parentheses.
    """

    def __init__(self):
        self.operators = {
            '+': (1, lambda a, b: a + b),
            '-': (1, lambda a, b: a - b),
            '*': (2, lambda a, b: a * b),
            '/': (2, lambda a, b: a / b if b != 0 else float('inf'))
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        Args:
            expression (str): A string containing the mathematical expression to evaluate.

        Returns:
            float: The result of the calculation.

        Raises:
            ValueError: If the expression is invalid, contains invalid characters, or involves division by zero.
        """
        normalized_expr = self._normalize_expression(expression)
        if not self._is_balanced(normalized_expr):
            raise ValueError("Unbalanced parentheses in the expression.")
        
        tokens = self._tokenize(normalized_expr)
        postfix = self._infix_to_postfix(tokens)
        result = self._evaluate_postfix(postfix)
        
        if result == float('inf'):
            raise ValueError("Division by zero encountered.")
        
        return result

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789.+-*/()")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

        Args:
            expression: A string containing the mathematical expression.

        Returns:
            bool: True if parentheses are correctly paired, otherwise False.
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

    def _tokenize(self, expression: str) -> List[str]:
        """
        Breaks down the expression into a list of tokens.

        Args:
            expression (str): A normalized mathematical expression.

        Returns:
            List[str]: A list of tokens.
        """
        tokens = []
        current_number = ""
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(current_number)
                    current_number = ""
                if char in self.operators or char in '()':
                    tokens.append(char)
        if current_number:
            tokens.append(current_number)
        return tokens

    def _infix_to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Converts an infix expression to postfix (Reverse Polish Notation).

        Args:
            tokens (List[str]): A list of tokens representing the infix expression.

        Returns:
            List[str]: A list of tokens representing the postfix expression.
        """
        output_queue = []
        operator_stack = []
        for token in tokens:
            if token.replace('.', '').isdigit():
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
            elif token in self.operators:
                while operator_stack and operator_stack[-1] != '(' and self.operators[operator_stack[-1]][0] >= self.operators[token][0]:
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
        while operator_stack:
            output_queue.append(operator_stack.pop())
        return output_queue

    def _evaluate_postfix(self, postfix: List[str]) -> float:
        """
        Evaluates a postfix expression.

        Args:
            postfix (List[str]): A list of tokens representing the postfix expression.

        Returns:
            float: The result of the calculation.
        """
        stack = []
        for token in postfix:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            elif token in self.operators:
                b, a = stack.pop(), stack.pop()
                result = self.operators[token][1](a, b)
                stack.append(result)
        return stack[0]
