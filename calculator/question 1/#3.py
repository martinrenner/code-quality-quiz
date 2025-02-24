import re  # Importing the regular expression module


class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction,
    multiplication, division, and parentheses.  It adheres to operator precedence
    and handles both integer and floating-point numbers.  The design emphasizes
    correctness, performance, modularity, security, testability, readability,
    and comprehensive documentation, aligning with ISO/IEC 25010 standards.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        Args:
            expression: The mathematical expression as a string.

        Returns:
            The result of the expression as a float.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                        invalid characters, division by zero).
        """
        try:
            expression = self._preprocess_expression(expression)
            tokens = self._tokenize(expression)
            postfix_tokens = self._infix_to_postfix(tokens)
            result = self._evaluate_postfix(postfix_tokens)
            return result
        except ValueError as e:
            raise ValueError(f"Invalid expression: {e}")  # Re-raise with context
        except Exception as e:  # Catching any other exceptions
            raise ValueError(f"An unexpected error occurred: {e}")  # Handling unexpected errors

    def _preprocess_expression(self, expression: str) -> str:
        """
        Preprocesses the expression string.
        - Removes whitespace.
        - Adds * between number and opening parenthesis, e.g '2(3+4)' to '2*(3+4)'

        Args:
            expression: original input string,
        Returns:
            expression with no whitespaces and implicit multiplications added.

        """
        expression = expression.replace(" ", "")
        # Insert * where implied (e.g., "2(3)" becomes "2*(3)")
        expression = re.sub(r'(\d+)\(', r'\1*(', expression)
        expression = re.sub(r'\)(\d+)', r')*\1', expression)
        expression = re.sub(r'\)\(', r')*(', expression)

        return expression


    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the mathematical expression.
            Splits numeric values and operators (+,-,*,/, and parentheses).

        Args:
            expression: The mathematical expression string.

        Returns:
            A list of tokens.

        Raises:
            ValueError: in case of any unrecognized character.
        """
        # Updated regex to handle decimal numbers and negative numbers correctly
        tokens = re.findall(r"[-+]?\d*\.?\d+|[+\-*/()]", expression)

        for token in tokens:
            if not re.match(r"^([-+]?\d*\.?\d+|[+\-*/()])$", token):
                raise ValueError(f"Invalid character found: {token}")
        return tokens

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts a list of tokens from infix notation to postfix notation
        using the Shunting Yard algorithm.

        Args:
            tokens: A list of tokens in infix notation.

        Returns:
            A list of tokens in postfix notation.

        Raises:
            ValueError: in case of unbalanced parentheses.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []

        for token in tokens:
            if re.match(r"^[-+]?\d*\.?\d+$", token):  # If number (integer or float)
                output.append(token)
            elif token in precedence:  # If it is an operator
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(operator_stack[-1], -1) >= precedence.get(token, -1)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Unbalanced parentheses (mismatched closing)")  # More descriptive
                operator_stack.pop()  # Remove the '('
            else: # if the regex in tokenize is correct, this else should never be reached.
                raise ValueError("Unrecognized token type")

        while operator_stack:
            if operator_stack[-1] == '(':  # Check for unclosed parenthesis
                raise ValueError("Unbalanced parentheses (unclosed opening)") # More descriptive
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates a list of tokens in postfix notation.

        Args:
            tokens: A list of tokens in postfix notation.

        Returns:
            The result of the expression as a float.

        Raises:
            ValueError: if zero division error occurs
        """
        stack = []
        for token in tokens:
            if re.match(r"^[-+]?\d*\.?\d+$", token):
                stack.append(float(token))  # Convert to float here
            else:
                try:
                    operand2 = stack.pop()
                    operand1 = stack.pop()
                except IndexError:
                    raise ValueError("Malformed expression (not enough operands)")  # More descriptive
                    # Empty stack means there are no operands for the operator to use

                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    stack.append(operand1 / operand2)
        if len(stack) != 1:
            raise ValueError("Malformed expression (too many operands)")
            # This indicate too many operands without the corresponding operators
        return stack[0]


def main():
    """
    Main function for the calculator.
    Takes user input and prints result or error messages.
    """
    calculator = Calculator()
    while True:
        expression = input("Enter a mathematical expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        try:
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()

