
class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction,
    multiplication, and division with proper handling of parentheses and operator precedence.

    This calculator accepts both integer and floating-point numbers (including negatives)
    and validates inputs to ensure they are syntactically correct. It raises descriptive
    errors for situations such as unbalanced parentheses, invalid characters, or division by zero.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates an arithmetic expression and returns the result as a float.

        :param expression: The arithmetic expression as a string.
        :return: The computed result.
        :raises ValueError: If the expression is malformed or contains invalid characters.
        :raises ZeroDivisionError: If there is an attempt to divide by zero.
        """
        # Remove whitespace and validate allowed characters
        normalized = self.normalize_expression(expression)

        # Validate that the parentheses are balanced
        if not self.is_balanced(normalized):
            raise ValueError("Unbalanced parentheses in expression.")

        # Tokenize the expression into numbers, operators, and parentheses
        tokens = self.tokenize(normalized)

        # Convert the infix expression to postfix using the Shunting Yard algorithm
        postfix_tokens = self.infix_to_postfix(tokens)

        # Evaluate the postfix expression and return the result
        return self.evaluate_postfix(postfix_tokens)

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes an arithmetic expression by removing whitespace and checking for allowed characters.

        Allowed characters are digits, period, the four arithmetic operators, and parentheses.

        :param expression: The input expression.
        :return: The normalized expression (whitespace removed).
        :raises ValueError: If any invalid character is found.
        """
        allowed_chars = set("0123456789+-*/().")
        normalized = expression.replace(" ", "")
        for char in normalized:
            if char not in allowed_chars:
                raise ValueError(f"Invalid character in expression: '{char}'")
        return normalized

    def is_balanced(self, expression: str) -> bool:
        """
        Checks whether the parentheses in the expression are properly balanced.

        :param expression: The normalized expression.
        :return: True if balanced, False otherwise.
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
        Splits the normalized expression into tokens (numbers, operators, and parentheses).

        It handles unary plus and minus appropriately, so that negative numbers
        or numbers prefixed with a '+' sign are recognized correctly.

        :param expression: The normalized arithmetic expression.
        :return: A list of tokens as strings.
        :raises ValueError: If the expression format is invalid.
        """
        tokens = []
        i = 0
        length = len(expression)

        while i < length:
            char = expression[i]

            # Check if we are at the start of a number (could be preceded by a unary + or -)
            if char.isdigit() or char == '.' or (
                char in '+-' and 
                (i == 0 or expression[i - 1] in "(-+*/") and 
                (i + 1 < length and (expression[i + 1].isdigit() or expression[i + 1] == '.'))
            ):
                token_chars = []

                # Handle a unary operator: if at the start or following an operator/parenthesis.
                if char in '+-':
                    # Unary plus is redundant. Preserve '-' for negative numbers.
                    if char == '-':
                        token_chars.append('-')
                    i += 1
                    if i >= length or not (expression[i].isdigit() or expression[i] == '.'):
                        raise ValueError("Invalid expression: expected a number after unary operator.")
                    while i < length and (expression[i].isdigit() or expression[i] == '.'):
                        token_chars.append(expression[i])
                        i += 1
                    tokens.append(''.join(token_chars))
                    continue
                else:
                    # Parse a positive number (integer or float)
                    while i < length and (expression[i].isdigit() or expression[i] == '.'):
                        token_chars.append(expression[i])
                        i += 1
                    tokens.append(''.join(token_chars))
                    continue

            elif char in "+-*/()":
                # Operators and parentheses are added as individual tokens.
                tokens.append(char)
                i += 1
            else:
                # Should not happen because invalid characters are filtered in normalize_expression.
                raise ValueError(f"Unexpected character encountered: '{char}'")
        return tokens

    def infix_to_postfix(self, tokens: list) -> list:
        """
        Converts an infix token list to postfix (Reverse Polish Notation) using the Shunting Yard algorithm.

        This method respects operator precedence: multiplication/division are evaluated
        before addition/subtraction.

        :param tokens: A list of tokens in infix order.
        :return: A list of tokens in postfix order.
        :raises ValueError: If there are mismatched parentheses.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []

        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token in precedence:
                # Pop operators from the stack with higher or equal precedence
                while (
                    operator_stack and
                    operator_stack[-1] in precedence and
                    precedence[operator_stack[-1]] >= precedence[token]
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                # Pop until we find the matching '('
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses encountered.")
                operator_stack.pop()  # Remove the '(' from the stack
            else:
                raise ValueError(f"Unknown token encountered: '{token}'")

        # Append any remaining operators to the output
        while operator_stack:
            if operator_stack[-1] in '()':
                raise ValueError("Mismatched parentheses encountered.")
            output.append(operator_stack.pop())

        return output

    def evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates a postfix (Reverse Polish Notation) expression and returns the computed result.

        :param tokens: A list of tokens in postfix order.
        :return: The evaluation result as a float.
        :raises ValueError: If the postfix expression is invalid.
        :raises ZeroDivisionError: If division by zero occurs.
        """
        stack = []
        for token in tokens:
            if self._is_number(token):
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient values for operation.")
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
                        raise ZeroDivisionError("Division by zero is undefined.")
                    stack.append(left / right)
                else:
                    raise ValueError(f"Unsupported operator encountered: '{token}'")

        if len(stack) != 1:
            raise ValueError("Invalid expression: too many values remaining.")
        return stack[0]

    def _is_number(self, token: str) -> bool:
        """
        Determines whether a token represents a number.

        :param token: The token as a string.
        :return: True if the token can be converted to a float; False otherwise.
        """
        try:
            float(token)
            return True
        except ValueError:
            return False


if __name__ == "__main__":
    """
    Console interface for the Calculator.

    Users can input arithmetic expressions and receive evaluation results.
    The program continues until the user types 'exit'.
    """
    calc = Calculator()
    print("Welcome to the Arithmetic Calculator!")
    print("Supported operations: addition (+), subtraction (-), multiplication (*), division (/)")
    print("You may use parentheses to enforce precedence.")
    print("Type 'exit' to quit the program.\n")

    while True:
        try:
            user_input = input("Enter expression: ")
            if user_input.strip().lower() == "exit":
                print("Goodbye!")
                break
            result = calc.calculate(user_input)
            print(f"Result: {result}\n")
        except Exception as error:
            print(f"Error: {error}\n")
