"""
A console-based arithmetic calculator that meets the requirements of ISO/IEC 25010.

Features:
    - Addition (+), Subtraction (-), Multiplication (*), Division (/)
    - Parentheses support
    - Correct operator precedence
    - Integer and floating-point support (including negative values)
    - Input validation: detect invalid characters, unbalanced parentheses, and division by zero
    - A function interface: calculate(expression: str) -> float
    - No usage of eval() or equivalent built-in evaluation methods
    - Modular, secure, and easily testable
"""

import sys

def tokenize(expression: str):
    """
    Convert the input expression string into a list of tokens.
    Handles numbers (positive, negative, integer, float) and operators (+, -, *, /, parentheses).
    Raises ValueError if invalid tokens are encountered.
    """
    tokens = []
    i = 0
    length = len(expression)

    # Characters allowed in token creation
    valid_chars = set("0123456789.+-*/() ")

    # Check for any invalid characters
    for ch in expression:
        if ch not in valid_chars:
            raise ValueError(f"Invalid character detected: {ch}")

    while i < length:
        char = expression[i]

        # Skip whitespace
        if char.isspace():
            i += 1
            continue

        # Parentheses or operators
        if char in "+-*/()":
            # Handle leading minus sign for negative numbers
            if char == '-':
                # If it's the very start or after an opening parenthesis or another operator,
                # then it's a negative sign for a number
                if (i == 0 or expression[i - 1] in '(+-*/'):
                    # Collect the numeric portion after the minus
                    num_str = '-'
                    i += 1
                    while i < length and (expression[i].isdigit() or expression[i] == '.'):
                        num_str += expression[i]
                        i += 1
                    # Validate the number format
                    if num_str == '-':
                        # Just a lone '-' operator
                        tokens.append('-')
                    else:
                        # Convert to float
                        try:
                            float(num_str)  # just to validate
                        except ValueError:
                            raise ValueError(f"Invalid numeric format: {num_str}")
                        tokens.append(num_str)
                    continue
                else:
                    tokens.append(char)
                    i += 1
                    continue
            else:
                tokens.append(char)
                i += 1
                continue

        # Numbers (integer or floating-point)
        elif char.isdigit() or char == '.':
            num_str = char
            i += 1
            # Read subsequent digits or decimal points
            while i < length and (expression[i].isdigit() or expression[i] == '.'):
                num_str += expression[i]
                i += 1

            # Validate number format
            try:
                float(num_str)  # just to validate
            except ValueError:
                raise ValueError(f"Invalid numeric format: {num_str}")

            tokens.append(num_str)
        else:
            # Any other character not caught is invalid
            raise ValueError(f"Invalid character in expression: {char}")

    return tokens


def to_rpn(tokens):
    """
    Convert a list of tokens (infix notation) to a list of tokens in RPN (Reverse Polish Notation)
    using the Shunting Yard algorithm.
    Raises ValueError if parentheses are unbalanced or other errors occur.
    """
    # Operator precedence and function mapping (precedence, operation)
    precedence = {
        '+': 1,
        '-': 1,
        '*': 2,
        '/': 2
    }

    output_queue = []
    operator_stack = []

    for token in tokens:
        # If token is a number, push to output queue
        try:
            float(token)  # If it can be converted to float, it's a number
            output_queue.append(token)
        except ValueError:
            # If not a number, must be an operator or parenthesis
            if token in precedence:  # an operator
                while (operator_stack and
                       operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)

            elif token == '(':
                operator_stack.append(token)

            elif token == ')':
                # Pop from stack to output until '(' is found
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses detected.")
                operator_stack.pop()  # pop '('
            else:
                raise ValueError(f"Invalid token encountered: {token}")

    # Pop any remaining operators to the output queue
    while operator_stack:
        top = operator_stack.pop()
        if top in ('(', ')'):
            raise ValueError("Mismatched parentheses detected.")
        output_queue.append(top)

    return output_queue


def evaluate_rpn(rpn_tokens):
    """
    Evaluate a list of tokens in Reverse Polish Notation and return the numeric result.
    Raises ValueError if there is a division by zero or invalid RPN structure.
    """
    stack = []

    for token in rpn_tokens:
        try:
            # If it's a number, push on the stack as float
            val = float(token)
            stack.append(val)
        except ValueError:
            # It's an operator
            if len(stack) < 2:
                raise ValueError("Invalid expression structure.")

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
                    raise ValueError("Division by zero.")
                result = a / b
            else:
                raise ValueError(f"Unknown operator: {token}")

            stack.append(result)

    if len(stack) != 1:
        raise ValueError("Invalid expression structure after evaluation.")

    return stack[0]


def calculate(expression: str) -> float:
    """
    Evaluate an arithmetic expression and return the numeric result as a float.

    :param expression: The arithmetic expression to evaluate
    :return: The numeric result of the expression
    :raises ValueError: If the expression contains errors (e.g., invalid tokens, division by zero)
    """
    # Strip and validate the expression
    expression = expression.strip()
    if not expression:
        raise ValueError("Empty expression.")

    # Tokenize the expression
    tokens = tokenize(expression)

    # Convert tokens to RPN
    rpn = to_rpn(tokens)

    # Evaluate RPN and return the result
    return evaluate_rpn(rpn)


def main():
    """
    Main function for console-based interaction. Reads user input in a loop,
    evaluates the expression, and prints the result.
    """
    print("Console-based Arithmetic Calculator (Type 'q' or 'quit' to exit)")

    while True:
        user_input = input("Enter expression: ").strip()
        if user_input.lower() in ("q", "quit"):
            print("Exiting calculator.")
            break

        try:
            result = calculate(user_input)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
