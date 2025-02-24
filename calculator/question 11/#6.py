import operator
import re

class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction,
    multiplication, and division with correct operator precedence and parentheses.
    """

    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression as a string.

        Returns:
            float: The result of the arithmetic expression.

        Raises:
            ValueError: If the expression contains invalid characters or is malformed.
        """
        expression = self.normalize_expression(expression)
        if not self.is_balanced(expression):
            raise ValueError("Unbalanced parentheses in the expression.")

        tokens = self.tokenize(expression)
        result = self.evaluate_expression(tokens)
        return result

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def is_balanced(self, expression: str) -> bool:
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

    def tokenize(self, expression: str):
        """
        Converts the arithmetic expression into tokens (numbers and operators).

        Args:
            expression (str): The normalized arithmetic expression as a string.

        Returns:
            list: A list of tokens (numbers and operators).
        """
        token_pattern = re.compile(r'\d+\.\d+|\d+|[-+*/()]')
        tokens = token_pattern.findall(expression)
        return tokens

    def evaluate_expression(self, tokens):
        """
        Evaluates the list of tokens using the Shunting Yard algorithm.

        Args:
            tokens (list): A list of tokens.

        Returns:
            float: The result of the evaluated expression.
        """
        output_queue = []
        operator_stack = []

        for token in tokens:
            if re.match(r'\d+(\.\d+)?', token):
                output_queue.append(float(token))
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] in self.operators and
                       self.precedence[operator_stack[-1]] >= self.precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return self.compute_rpn(output_queue)

    def compute_rpn(self, rpn):
        """
        Computes the result of the Reverse Polish Notation (RPN) expression.

        Args:
            rpn (list): A list representing the RPN expression.

        Returns:
            float: The result of the RPN expression.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        stack = []

        for token in rpn:
            if isinstance(token, float):
                stack.append(token)
            elif token in self.operators:
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    raise ZeroDivisionError(" Division by zero.")
                result = self.operators[token](a, b)
                stack.append(result)

        return stack[0]
