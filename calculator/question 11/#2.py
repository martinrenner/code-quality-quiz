class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction, multiplication, division,
    and parentheses with proper operator precedence. It validates inputs for correctness and security.
    """

    def __init__(self):
        self.operators = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.

        Args:
            expression (str): A string containing the arithmetic expression.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression contains invalid characters or is improperly formatted.
            ZeroDivisionError: If there is an attempt to divide by zero.
        """
        expression = self.normalize_expression(expression)
        if not self.is_balanced(expression):
            raise ValueError("Unbalanced parentheses.")

        try:
            result = self.evaluate_expression(expression)
        except ZeroDivisionError:
            raise ValueError("Division by zero error.")
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

        return result

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def is_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

        Args:
            expression (str): A string containing the mathematical expression.

        Returns:
            bool: True if parentheses are correctly paired, otherwise False.
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

    def evaluate_expression(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression using the Shunting Yard algorithm.

        Args:
            expression (str): A normalized arithmetic expression as a string.

        Returns:
            float: The result of the evaluated expression.
        """
        output_queue = []
        operator_stack = []
        i = 0

        while i < len(expression):
            char = expression[i]

            if char.isdigit() or char == '.':
                num_str = self.extract_number(expression, i)
                output_queue.append(float(num_str))
                i += len(num_str) - 1
            elif char in self.operators:
                while (operator_stack and operator_stack[-1] in self.operators and
                       self.precedence[operator_stack[-1]] >= self.precedence[char]):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                operator_stack.pop()
            i += 1

        while operator_stack:
            output_queue.append(operator_stack.pop())

        return self.compute_rpn(output_queue)

    def extract_number(self, expression: str, start: int) -> str:
        """
        Extracts a number (including decimals and negative numbers) from the expression.

        Args:
            expression (str): The arithmetic expression.
            start (int): The starting index of the number.

        Returns:
            str: The extracted number as a string.
        """
        end = start
        while end < len(expression) and (expression[end].isdigit() or expression[end] == '.'):
            end += 1
        return expression[start:end]

    def compute_rpn(self, rpn: list) -> float:
        """
        Computes the result of a Reverse Polish Notation (RPN) expression.

        Args:
            rpn (list): The RPN expression as a list of tokens.

        Returns:
            float: The result of the RPN expression.
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
