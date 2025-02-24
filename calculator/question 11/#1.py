import operator
import re

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
        Evaluates the given arithmetic expression.

        Args:
        expression (str): The arithmetic expression to evaluate.

        Returns:
        float: The result of the evaluation.

        Raises:
        ValueError: If the expression is invalid.
        """
        # Validate the expression
        self.validate_expression(expression)

        # Parse the expression into tokens
        tokens = self.tokenize(expression)

        # Convert tokens to Reverse Polish Notation (RPN)
        rpn = self.shunting_yard(tokens)

        # Evaluate the RPN expression
        result = self.evaluate_rpn(rpn)
        return result

    def validate_expression(self, expression: str):
        """
        Validates the given arithmetic expression.

        Args:
        expression (str): The arithmetic expression to validate.

        Raises:
        ValueError: If the expression is invalid.
        """
        # Check for unbalanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses")

        # Check for invalid characters
        if not re.match(r'^[\d\s()+\-*/.]*$', expression):
            raise ValueError("Invalid characters in expression")

        # Check for division by zero
        if re.search(r'/\s*0', expression):
            raise ValueError("Division by zero")

    def tokenize(self, expression: str) -> list:
        """
        Converts the given arithmetic expression into a list of tokens.

        Args:
        expression (str): The arithmetic expression to tokenize.

        Returns:
        list: A list of tokens.
        """
        # Remove whitespace from the expression
        expression = expression.replace(' ', '')

        # Split the expression into tokens
        tokens = re.findall(r'\d+\.\d+|\d+|[()+\-*/]', expression)
        return tokens

    def shunting_yard(self, tokens: list) -> list:
        """
        Converts a list of tokens to Reverse Polish Notation (RPN) using the Shunting Yard algorithm.

        Args:
        tokens (list): A list of tokens.

        Returns:
        list: A list of tokens in RPN.
        """
        output = []
        stack = []

        for token in tokens:
            if re.match(r'\d+(\.\d+)?', token):
                # If the token is a number, add it to the output queue
                output.append(token)
            elif token in self.operators:
                # If the token is an operator, process the operator stack
                while (stack and stack[-1] != '(' and
                       self.precedence[stack[-1]] >= self.precedence[token]):
                    output.append(stack.pop())
                stack.append(token)
            elif token == '(':
                # If the token is a left parenthesis, push it onto the stack
                stack.append(token)
            elif token == ')':
                # If the token is a right parenthesis, process the stack until a left parenthesis is found
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove the left parenthesis from the stack

        # Process any remaining operators in the stack
        while stack:
            output.append(stack.pop())

        return output

    def evaluate_rpn(self, rpn: list) -> float:
        """
        Evaluates a Reverse Polish Notation (RPN) expression.

        Args:
        rpn (list): A list of tokens in RPN.

        Returns:
        float: The result of the evaluation.
        """
        stack = []

        for token in rpn:
            if re.match(r'\d+(\.\d+)?', token):
                # If the token is a number, push it onto the stack
                stack.append(float(token))
            elif token in self.operators:
                # If the token is an operator, pop the top two numbers from the stack and apply the operator
                b = stack.pop()
                a = stack.pop()
                result = self.operators[token](a, b)
                stack.append(result)

        # The result of the evaluation is the only remaining value in the stack
        return stack[0]

# Example usage
if __name__ == "__main__":
    calculator = Calculator()
    expression = "3 + 5 * (2 - 8)"
    try:
        result = calculator.calculate(expression)
        print(f"The result of '{expression}' is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
