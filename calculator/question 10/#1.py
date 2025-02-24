import re

class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction, multiplication, and division,
    with correct operator precedence and parentheses.

    Attributes:
        expression (str): The mathematical expression to be evaluated.
    """

    def __init__(self, expression: str):
        """
        Initialize the Calculator with the given expression.

        Args:
            expression (str): The mathematical expression to evaluate.

        Raises:
            ValueError: If the expression contains invalid characters or unbalanced parentheses.
        """
        self.expression = expression
        self._validate_expression()

    def _validate_expression(self):
        """
        Validate the expression for correctness.

        Raises:
            ValueError: If the expression contains invalid characters or unbalanced parentheses.
        """
        if not re.match(r'^[\d\s\+\-\*\/\(\)]+$', self.expression):
            raise ValueError("Invalid characters in expression.")
        
        if self.expression.count('(') != self.expression.count(')'):
            raise ValueError("Unbalanced parentheses in expression.")

    def calculate(self) -> float:
        """
        Evaluate the arithmetic expression and return the result.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If division by zero is attempted.
        """
        try:
            tokens = self._tokenize()
            postfix = self._infix_to_postfix(tokens)
            return self._evaluate_postfix(postfix)
        except ZeroDivisionError:
            raise ValueError("Division by zero is not allowed.")

    def _tokenize(self) -> list:
        """
        Convert the input string into a list of tokens.

        Returns:
            list: A list of tokens representing numbers and operators.
        """
        token_pattern = r'\d*\.?\d+|\+|\-|*|\/|\(|\)'
        return re.findall(token_pattern, self.expression)

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Convert an infix expression to postfix notation using the Shunting Yard algorithm.

        Args:
            tokens (list): A list of tokens in infix notation.

        Returns:
            list: A list of tokens in postfix notation.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.replace('.', '').isdigit():
                output_queue.append(token)
            elif token in '+-*/':
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(operator_stack[-1], 0) >= precedence[token]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()
                else:
                    raise ValueError("Mismatched parentheses")

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(operator_stack.pop())

        return output_queue

    def _evaluate_postfix(self, postfix: list) -> float:
        """
        Evaluate a postfix expression.

        Args:
            postfix (list): A list of tokens in postfix notation.

        Returns:
            float: The result of the evaluated postfix expression.
        """
        stack = []

        for token in postfix:
            if token.replace('.', '').isdigit():
                stack.append(float(token))
            else:
                b, a = stack.pop(), stack.pop()
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

# Example usage:
if __name__ == "__main__":
    try:
        calc = Calculator("3 + 4 * (2 - 1)")
        result = calc.calculate()
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
