#!/usr/bin/env python3
"""
Console-based Arithmetic Calculator

This module implements a calculator that evaluates arithmetic expressions
supporting addition (+), subtraction (-), multiplication (*), division (/),
parentheses for grouping, and proper operator precedence. Both integers and
floating-point numbers (including negative values) are supported.

Designed to meet ISO/IEC 25010 requirements for functionality, performance,
modularity, security, testability, and readability.
"""

class Calculator:
    """
    A Calculator that parses and evaluates arithmetic expressions.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression provided as a string and returns the result.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses)
                        or contains invalid characters or number formats.
            ZeroDivisionError: If division by zero occurs.
        """
        # Normalize the expression: remove whitespace and validate characters.
        normalized_expr = self.normalize_expression(expression)
        # Validate that all parentheses are correctly paired.
        if not self.is_balanced(normalized_expr):
            raise ValueError("Unbalanced parentheses in expression.")
        # Tokenize the normalized expression into numbers and operators.
        tokens = self.tokenize(normalized_expr)
        # Convert the infix tokens to postfix notation using the Shunting-yard algorithm.
        postfix_tokens = self.infix_to_postfix(tokens)
        # Evaluate the postfix expression to get the final result.
        return self.evaluate_rpn(postfix_tokens)

    @staticmethod
    def normalize_expression(expression: str) -> str:
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

    @staticmethod
    def is_balanced(expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

        Args:
            expression (str): The expression to check.

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

    def tokenize(self, expression: str) -> list:
        """
        Tokenizes the arithmetic expression into numbers and operators.

        This function recognizes numbers (including floating point and negatives)
        and the operators +, -, *, /, as well as parentheses.

        Args:
            expression (str): The normalized arithmetic expression.

        Returns:
            list: A list of tokens where numbers are represented as float and
                  operators/parentheses as str.

        Raises:
            ValueError: If an invalid numeric format is encountered.
        """
        tokens = []
        i = 0
        length = len(expression)
        operators = set("+-*/")
        # Process each character in the expression.
        while i < length:
            char = expression[i]

            # Check if the current character starts a number token.
            # A '-' is treated as a unary minus if it is:
            # - at the beginning of the expression, or
            # - immediately following an operator or '('.
            if (char.isdigit() or char == '.' or
                (char == '-' and (i == 0 or expression[i - 1] in operators.union({"(", "["}))
                 and (i + 1 < length and (expression[i + 1].isdigit() or expression[i + 1] == '.')))):
                num_str = ""
                # Handle unary minus.
                if char == '-':
                    num_str += "-"
                    i += 1
                    if i >= length:
                        raise ValueError("Invalid expression: lone '-' sign.")
                    char = expression[i]

                dot_count = 0
                # Build the full number token.
                while i < length and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        dot_count += 1
                        if dot_count > 1:
                            raise ValueError("Invalid number format with multiple decimal points.")
                    num_str += expression[i]
                    i += 1
                try:
                    number = float(num_str)
                except ValueError:
                    raise ValueError(f"Invalid number format: {num_str}")
                tokens.append(number)
            # Process operator tokens.
            elif char in operators:
                tokens.append(char)
                i += 1
            # Process parentheses.
            elif char in "()":
                tokens.append(char)
                i += 1
            else:
                # Should never reach here due to prior normalization.
                raise ValueError(f"Invalid character encountered: {char}")
        return tokens

    @staticmethod
    def infix_to_postfix(tokens: list) -> list:
        """
        Converts infix tokens to postfix (Reverse Polish Notation) tokens
        using the Shunting-yard algorithm.

        Args:
            tokens (list): The list of tokens from tokenization.

        Returns:
            list: A list of tokens in postfix order.

        Raises:
            ValueError: If there are unmatched parentheses.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output_queue = []
        operator_stack = []

        for token in tokens:
            # If token is a number, add it directly to the output queue.
            if isinstance(token, float):
                output_queue.append(token)
            # If token is an operator, process according to precedence.
            elif token in precedence:
                while (operator_stack and operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            # Left parenthesis: push onto the operator stack.
            elif token == '(':
                operator_stack.append(token)
            # Right parenthesis: pop operators until the matching '('.
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack or operator_stack[-1] != '(':
                    raise ValueError("Mismatched parentheses in expression.")
                operator_stack.pop()  # Discard the '('
            else:
                raise ValueError(f"Unknown token: {token}")

        # Pop any remaining operators from the stack.
        while operator_stack:
            if operator_stack[-1] in '()':
                raise ValueError("Mismatched parentheses in expression.")
            output_queue.append(operator_stack.pop())

        return output_queue

    @staticmethod
    def evaluate_rpn(postfix_tokens: list) -> float:
        """
        Evaluates a postfix (Reverse Polish Notation) expression.

        Args:
            postfix_tokens (list): The list of tokens in postfix order.

        Returns:
            float: The result of evaluating the expression.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
            ValueError: If the expression is invalid.
        """
        stack = []
        for token in postfix_tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token in {'+', '-', '*', '/'}:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient values.")
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    result = a + b
                elif token == '-':
                    result = a - b
                elif token == '*':
                    result = a * b
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero is undefined.")
                    result = a / b
                stack.append(result)
            else:
                raise ValueError(f"Unknown token in RPN expression: {token}")
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many values remain.")
        return stack[0]

def main():
    """
    Main function to run the console-based arithmetic calculator.
    
    It prompts the user to enter an arithmetic expression, evaluates it,
    and prints the result. The loop continues until the user types 'exit' or 'quit'.
    """
    calc = Calculator()
    print("Console-based Arithmetic Calculator")
    print("Enter an arithmetic expression to evaluate (or type 'exit' to quit).")

    while True:
        try:
            user_input = input("Expression: ").strip()
            if user_input.lower() in {'exit', 'quit'}:
                print("Exiting calculator. Goodbye!")
                break
            result = calc.calculate(user_input)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
