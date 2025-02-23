
import re

class Calculator:
    def __init__(self):
        self.operators = {'+': (1, lambda x, y: x + y),
                          '-': (1, lambda x, y: x - y),
                          '*': (2, lambda x, y: x * y),
                          '/': (2, lambda x, y: x / y)}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If the expression contains invalid inputs.
        """
        # Validate the expression
        if not self._is_valid_expression(expression):
            raise ValueError("Invalid expression.")

        # Tokenize the expression
        tokens = self._tokenize(expression)

        # Convert tokens to Reverse Polish Notation (RPN)
        rpn = self._to_rpn(tokens)

        # Evaluate the RPN expression
        return self._evaluate_rpn(rpn)

    def _is_valid_expression(self, expression: str) -> bool:
        """
        Validates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to validate.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        # Check for unbalanced parentheses
        if expression.count('(') != expression.count(')'):
            return False

        # Check for invalid characters
        if re.search(r'[^0-9+\-*/(). ]', expression):
            return False

        return True

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            list: A list of tokens.
        """
        # Remove whitespace
        expression = expression.replace(' ', '')

        # Tokenize using regex
        tokens = re.findall(r'\d+\.\d+|\d+|[()+\-*/]', expression)

        return tokens

    def _to_rpn(self, tokens: list) -> list:
        """
        Converts the tokenized expression to Reverse Polish Notation (RPN).

        Args:
            tokens (list): The list of tokens.

        Returns:
            list: The RPN expression.
        """
        output = []
        stack = []

        for token in tokens:
            if token in self.operators:
                while (stack and stack[-1] in self.operators and
                       self.operators[stack[-1]][0] >= self.operators[token][0]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '(' from stack
            else:
                output.append(float(token))

        while stack:
            output.append(stack.pop())

        return output

    def _evaluate_rpn(self, rpn: list) -> float:
        """
        Evaluates the Reverse Polish Notation (RPN) expression.

        Args:
            rpn (list): The RPN expression.

        Returns:
            float: The result of the evaluation.
        """
        stack = []

        for token in rpn:
            if token in self.operators:
                y, x = stack.pop(), stack.pop()
                if token == '/' and y == 0:
                    raise ValueError("Division by zero.")
                stack.append(self.operators[token][1](x, y))
            else:
                stack.append(token)

        return stack[0]

# Example usage:
if __name__ == "__main__":
    calculator = Calculator()
    expression = "3 + 5 * (2 - 8) / 2"
    try:
        result = calculator.calculate(expression)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
