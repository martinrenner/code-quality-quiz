
import re
import operator

class Calculator:
    def __init__(self):
        self.operators = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv
        }
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression contains invalid syntax or unbalanced parentheses.
            ZeroDivisionError: If division by zero is detected.
        """
        # Validate the expression
        self._validate_expression(expression)

        # Tokenize the expression
        tokens = self._tokenize(expression)

        # Convert tokens to reverse polish notation (RPN)
        rpn = self._infix_to_rpn(tokens)

        # Evaluate the RPN
        return self._evaluate_rpn(rpn)

    def _validate_expression(self, expression: str):
        """
        Validates the arithmetic expression for syntax errors.

        Args:
            expression (str): The arithmetic expression to validate.

        Raises:
            ValueError: If the expression contains invalid syntax.
        """
        # Check for unbalanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses")

        # Check for invalid characters
        if not re.match(r'^[\d\s\+\-\*/\(\).]+$', expression):
            raise ValueError("Invalid characters in expression")

    def _tokenize(self, expression: str):
        """
        Tokenizes the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            list: A list of tokens (numbers and operators).
        """
        tokens = re.findall(r'\d+\.\d+|\d+|[+*/\-()]', expression)
        return tokens

    def _infix_to_rpn(self, tokens):
        """
        Converts infix notation to reverse polish notation (RPN).

        Args:
            tokens (list): A list of tokens (numbers and operators).

        Returns:
            list: A list of tokens in RPN.
        """
        output = []
        stack = []

        for token in tokens:
            if token.isdigit() or '.' in token:
                output.append(token)
            elif token in self.operators:
                while (stack and stack[-1] in self.operators and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()

        while stack:
            output.append(stack.pop())

        return output

    def _evaluate_rpn(self, rpn):
        """
        Evaluates the reverse polish notation (RPN).

        Args:
            rpn (list): A list of tokens in RPN.

        Returns:
            float: The result of the evaluated RPN.

        Raises:
            ZeroDivisionError: If division by zero is detected.
        """
        stack = []

        for token in rpn:
            if token.isdigit() or '.' in token:
                stack.append(float(token))
            elif token in self.operators:
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(self.operators[token](a, b))

        return stack[0]

if __name__ == "__main__":
    calculator = Calculator()
    while True:
        expression = input("Enter an arithmetic expression (or 'exit' to quit): ")
        if expression.lower() == 'exit':
            break
        try:
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except ZeroDivisionError as e:
            print(f"Error: {e}")
