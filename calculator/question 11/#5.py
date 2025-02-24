class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}
        self.parentheses = {'(': 0, ')': 0}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        :param expression: str - The arithmetic expression to evaluate
        :return: float - The result of the evaluation
        :raises ValueError: If the expression is invalid
        """
        # Validate the expression
        self._validate_expression(expression)

        # Convert the expression to Reverse Polish Notation (RPN)
        rpn_expression = self._infix_to_rpn(expression)

        # Evaluate the RPN expression
        return self._evaluate_rpn(rpn_expression)

    def _validate_expression(self, expression: str):
        """
        Validates the arithmetic expression for syntax errors.

        :param expression: str - The arithmetic expression to validate
        :raises ValueError: If the expression is invalid
        """
        stack = []
        for char in expression:
            if char in self.parentheses:
                if char == '(':
                    stack.append(char)
                elif char == ')':
                    if not stack:
                        raise ValueError("Unbalanced parentheses")
                    stack.pop()
            elif char not in self.operators and not char.isdigit() and char not in [' ', '.', '-']:
                raise ValueError(f"Invalid character: {char}")
        if stack:
            raise ValueError("Unbalanced parentheses")

    def _infix_to_rpn(self, expression: str):
        """
        Converts an infix expression to Reverse Polish Notation (RPN).

        :param expression: str - The infix arithmetic expression
        :return: list - The RPN expression
        """
        output = []
        stack = []
        tokens = self._tokenize(expression)

        for token in tokens:
            if token.isdigit() or '.' in token:  # Number
                output.append(float(token))
            elif token in self.operators:  # Operator
                while (stack and stack[-1] in self.operators and
                       self.operators[stack[-1]] >= self.operators[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove the '(' from the stack

        while stack:
            output.append(stack.pop())

        return output

    def _evaluate_rpn(self, rpn_expression):
        """
        Evaluates a Reverse Polish Notation (RPN) expression.

        :param rpn_expression: list - The RPN expression
        :return: float - The result of the evaluation
        :raises ValueError: If division by zero occurs
        """
        stack = []

        for token in rpn_expression:
            if isinstance(token, float):
                stack.append(token)
            elif token in self.operators:
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
                        raise ValueError("Division by zero")
                    stack.append(a / b)

        return stack[0]

    def _tokenize(self, expression: str):
        """
        Tokenizes the arithmetic expression.

        :param expression: str - The arithmetic expression to tokenize
        :return: list - The tokens of the expression
        """
        tokens = []
        current_token = []

        for char in expression:
            if char in self.operators or char in self.parentheses or char == ' ':
                if current_token:
                    tokens.append(''.join(current_token))
                    current_token = []
                if char != ' ':
                    tokens.append(char)
            else:
                current_token.append(char)

        if current_token:
            tokens.append(''.join(current_token))

        return tokens

# Example usage
if __name__ == "__main__":
    calculator = Calculator()
    expression = "3 + 5 * (2 - 8 / 4)"
    try:
        result = calculator.calculate(expression)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
