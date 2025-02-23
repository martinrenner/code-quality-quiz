
class Calculator:
    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def validate_expression(self, expression: str) -> bool:
        """Validate the expression for balanced parentheses and valid characters."""
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack or stack.pop() != '(':
                    return False
            elif char not in self.operators and not char.isdigit() and char not in {'.', ' ', '-'}:
                return False
        return not stack

    def parse_expression(self, expression: str):
        """Convert the expression to a list of tokens."""
        tokens = []
        number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(float(number) if '.' in number else int(number))
                    number = ''
                if char in self.operators or char in {'(', ')'}:
                    tokens.append(char)
        if number:
            tokens.append(float(number) if '.' in number else int(number))
        return tokens

    def apply_operator(self, operators, values):
        """Apply an operator to the values."""
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ValueError("Division by zero")
            values.append(left / right)

    def evaluate_expression(self, tokens):
        """Evaluate the expression using the Shunting Yard algorithm."""
        values = []
        operators = []
        for token in tokens:
            if isinstance(token, (int, float)):
                values.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    self.apply_operator(operators, values)
                operators.pop() # Remove the '('
            else:
                while (operators and operators[-1] in self.operators and
                       self.precedence[operators[-1]] >= self.precedence[token]):
                    self.apply_operator(operators, values)
                operators.append(token)
        while operators:
            self.apply_operator(operators, values)
        return values[0]

    def calculate(self, expression: str) -> float:
        """Evaluate the expression and return the result."""
        expression = expression.replace(' ', '')
        if not self.validate_expression(expression):
            raise ValueError("Invalid expression")
        tokens = self.parse_expression(expression)
        return self.evaluate_expression(tokens)

# Example usage:
if __name__ == "__main__":
    calculator = Calculator()
    expression = input("Enter your arithmetic expression: ")
    try:
        result = calculator.calculate(expression)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
