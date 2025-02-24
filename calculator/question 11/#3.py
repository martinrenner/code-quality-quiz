class Calculator:
    def __init__(self):
        self.operators = {'+': (1, lambda x, y: x + y),
                          '-': (1, lambda x, y: x - y),
                          '*': (2, lambda x, y: x * y),
                          '/': (2, lambda x, y: x / y)}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the arithmetic expression.
        """
        if not self.is_valid_expression(expression):
            raise ValueError("Invalid expression")

        tokens = self.tokenize(expression)
        output = self.evaluate(tokens)
        return output

    def is_valid_expression(self, expression: str) -> bool:
        """
        Validates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to validate.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
        return not stack

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
            if char in self.operators or char in '()':
                if current_number:
                    tokens.append(float(''.join(current_number)))
                    current_number = []
                tokens.append(char)
            elif char.isdigit() or char == '.':
                current_number.append(char)
            elif char == '-' and (not tokens or tokens[-1] in self.operators or tokens[-1] == '('):
                current_number.append(char)
            else:
                raise ValueError("Invalid character in expression")
        if current_number:
            tokens.append(float(''.join(current_number)))
        return tokens

    def evaluate(self, tokens: list) -> float:
        """
        Evaluates the tokenized arithmetic expression.

        Args:
            tokens (list): The list of tokens to evaluate.

        Returns:
            float: The result of the arithmetic expression.
        """
        def apply_operator(operators, values):
            operator = operators.pop()
            right = values.pop()
            left = values.pop()
            values.append(self.operators[operator][1](left, right))

        values = []
        operators = []
        for token in tokens:
            if token in self.operators:
                while (operators and operators[-1] in self.operators and
                       self.operators[operators[-1]][0] >= self.operators[token][0]):
                    apply_operator(operators, values)
                operators.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, values)
                operators.pop()
            else:
                values.append(token)

        while operators:
            apply_operator(operators, values)

        return values[0]

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    expression = "3 + 5 * (2 - 8 / 4)"
    try:
        result = calc.calculate(expression)
        print(f"The result of '{expression}' is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
