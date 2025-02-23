
class Calculator:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the arithmetic expression.

        Raises:
            ValueError: If the expression contains invalid characters or unbalanced parentheses.
            ZeroDivisionError: If division by zero is attempted.
        """
        # Validate the expression
        self.validate_expression(expression)

        # Convert the expression to a list of tokens
        tokens = self.tokenize(expression)

        # Convert the tokens to Reverse Polish Notation (RPN)
        rpn = self.to_rpn(tokens)

        # Evaluate the RPN expression
        return self.evaluate_rpn(rpn)

    def validate_expression(self, expression: str):
        """
        Validates the arithmetic expression for invalid characters and unbalanced parentheses.

        Args:
            expression (str): The arithmetic expression to validate.

        Raises:
            ValueError: If the expression contains invalid characters or unbalanced parentheses.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    raise ValueError("Unbalanced parentheses")
                stack.pop()
            elif not (char.isdigit() or char in self.operators or char in {' ', '.', '-'}):
                raise ValueError(f"Invalid character: {char}")
        if stack:
            raise ValueError("Unbalanced parentheses")

    def tokenize(self, expression: str) -> list:
        """
        Tokenizes the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            list: A list of tokens.
        """
        tokens = []
        current_number = []
        for char in expression:
            if char.isdigit() or char == '.':
                current_number.append(char)
            else:
                if current_number:
                    tokens.append(float(''.join(current_number)))
                    current_number = []
                if char in self.operators or char in {'(', ')'}:
                    tokens.append(char)
        if current_number:
            tokens.append(float(''.join(current_number)))
        return tokens

    def to_rpn(self, tokens: list) -> list:
        """
        Converts the list of tokens to Reverse Polish Notation (RPN).

        Args:
            tokens (list): The list of tokens to convert.

        Returns:
            list: The RPN representation of the tokens.
        """
        stack = []
        output = []
        for token in tokens:
            if isinstance(token, float):
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()
            else:
                while (stack and stack[-1] in self.operators and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
        while stack:
            output.append(stack.pop())
        return output

    def evaluate_rpn(self, rpn: list) -> float:
        """
        Evaluates the Reverse Polish Notation (RPN) expression.

        Args:
            rpn (list): The RPN expression to evaluate.

        Returns:
            float: The result of the RPN expression.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        stack = []
        for token in rpn:
            if isinstance(token, float):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)
        return stack[0]

# Example usage
if __name__ == "__main__":
    calculator = Calculator()
    expression = "3 + 5 * (2 - 8)"
    try:
        result = calculator.calculate(expression)
        print(f"Result: {result}")
    except (ValueError, ZeroDivisionError) as e:
        print(f"Error: {e}")
