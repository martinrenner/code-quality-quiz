class Calculator:
    """
    A console-based arithmetic calculator supporting addition, subtraction,
    multiplication, division, and parentheses with correct order of operations.
    This calculator processes integer and decimal numbers (including negatives)
    and detects invalid inputs such as unbalanced parentheses, invalid characters,
    and division by zero.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates an arithmetic expression and returns the result as a float.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression is invalid (unbalanced parentheses, invalid
                        characters, syntax error, division by zero, etc.).
        """
        # Normalize expression (remove spaces and validate allowed characters)
        normalized_expr = self._normalize_expression(expression)
        # Check for balanced parentheses
        if not self._is_balanced(normalized_expr):
            raise ValueError("Unbalanced parentheses in expression.")
        # Tokenize the expression into numbers and operators
        tokens = self._tokenize(normalized_expr)
        # Convert infix tokens to postfix notation (Reverse Polish Notation)
        postfix_tokens = self._infix_to_postfix(tokens)
        # Evaluate the postfix expression
        result = self._evaluate_postfix(postfix_tokens)
        return result

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the arithmetic expression by removing spaces and validating characters.

        Args:
            expression (str): The raw arithmetic expression.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        for char in expression:
            if char not in allowed_chars:
                raise ValueError("Expression contains invalid characters.")
        return expression.replace(" ", "")

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks whether the arithmetic expression has properly balanced parentheses.

        Args:
            expression (str): The arithmetic expression.

        Returns:
            bool: True if parentheses are balanced; False otherwise.
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

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the normalized arithmetic expression into numbers and operators.

        Tokens:
            - Numbers (including negatives and decimals) are converted to float.
            - Operators and parentheses remain as strings.

        Args:
            expression (str): The normalized arithmetic expression.

        Returns:
            list: A list of tokens representing numbers and operators.

        Raises:
            ValueError: If an invalid number format is encountered.
        """
        tokens = []
        i = 0
        n = len(expression)
        while i < n:
            char = expression[i]

            # Check for a number: digit or a decimal point; consider unary minus.
            if (
                char.isdigit()
                or char == '.'
                or (
                    char == '-' and (i == 0 or expression[i - 1] in "(-+*/")
                    and (i + 1 < n and (expression[i + 1].isdigit() or expression[i + 1] == '.'))
                )
            ):
                num_str = ""
                # Handle unary minus by including it in the number token.
                if char == '-':
                    num_str += '-'
                    i += 1
                    if i >= n or (not expression[i].isdigit() and expression[i] != '.'):
                        raise ValueError("Invalid number format after '-'")
                # Accumulate the digit characters and at most one decimal point.
                dot_count = 0
                while i < n and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        dot_count += 1
                        if dot_count > 1:
                            raise ValueError("Invalid numeric format: multiple decimal points.")
                    num_str += expression[i]
                    i += 1
                try:
                    number = float(num_str)
                except ValueError:
                    raise ValueError("Invalid number format.")
                tokens.append(number)
            elif char in "+*/":
                tokens.append(char)
                i += 1
            elif char == '-':
                # A '-' not identified as unary (i.e., a binary operator)
                tokens.append(char)
                i += 1
            elif char in "()":
                tokens.append(char)
                i += 1
            else:
                # Although normalization should prevent this branch from executing,
                # we raise an error if an unknown token is encountered.
                raise ValueError(f"Invalid character encountered: {char}")
        return tokens

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts the list of tokens from infix notation to postfix notation using
        the Shunting Yard algorithm.

        Args:
            tokens (list): List of tokens (numbers and operators) in infix order.

        Returns:
            list: A list of tokens representing the postfix expression.

        Raises:
            ValueError: If there are mismatched parentheses.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []
        for token in tokens:
            if isinstance(token, float):
                output.append(token)
            elif token in precedence:
                while (
                    operator_stack
                    and operator_stack[-1] in precedence
                    and precedence[operator_stack[-1]] >= precedence[token]
                ):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                # Pop operators until the matching '(' is found.
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses.")
                operator_stack.pop()  # Remove '(' from the stack.
        # Append any remaining operators.
        while operator_stack:
            op = operator_stack.pop()
            if op == '(' or op == ')':
                raise ValueError("Mismatched parentheses.")
            output.append(op)
        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates a postfix (Reverse Polish Notation) expression and returns the result.

        Args:
            tokens (list): A list of tokens in postfix order.

        Returns:
            float: The result of the expression.

        Raises:
            ValueError: If there is a division by zero or the expression is invalid.
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token in {'+', '-', '*', '/'}:
                if len(stack) < 2:
                    raise ValueError("Invalid expression syntax.")
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
                        raise ValueError("Division by zero error.")
                    result = a / b
                stack.append(result)
            else:
                raise ValueError("Invalid token encountered during evaluation.")
        if len(stack) != 1:
            raise ValueError("Invalid expression syntax.")
        return stack[0]


def main():
    """
    Main function to run the console-based arithmetic calculator.
    Users can enter arithmetic expressions, and the result is printed.
    Type 'quit' to exit the application.
    """
    calc = Calculator()
    print("Console-based Arithmetic Calculator")
    print("Supports operations: addition (+), subtraction (-), multiplication (*), division (/), and parentheses ()")
    print("Enter 'quit' to exit.")
    while True:
        expression = input("Enter expression: ")
        if expression.lower() == "quit":
            break
        try:
            result = calc.calculate(expression)
            print("Result:", result)
        except ValueError as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
