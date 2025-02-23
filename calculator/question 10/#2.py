
class Calculator:
    def __init__(self):
        """
        Initializes the Calculator class.
        """
        self.operators = {'+', '-', '*', '/'}
        self.precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        :param expression: A string containing the arithmetic expression.
        :return: The result of the evaluated expression.
        :raises ValueError: If the expression contains invalid characters, unbalanced parentheses, or division by zero.
        """
        expression = self.normalize_expression(expression)
        if not self.is_balanced(expression):
            raise ValueError("Unbalanced parentheses in the expression.")

        postfix = self.infix_to_postfix(expression)
        return self.evaluate_postfix(postfix)

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes the expression by removing spaces and validating characters.

        :param expression: A string containing the arithmetic expression.
        :return: The normalized expression without spaces.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def is_balanced(self, expression: str) -> bool:
        """
        Checks whether the expression has properly paired parentheses.

        :param expression: A string containing the arithmetic expression.
        :return: True if parentheses are correctly paired, otherwise False.
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

    def infix_to_postfix(self, expression: str) -> list:
        """
        Converts infix expression to postfix expression (Reverse Polish Notation).

        :param expression: A string containing the arithmetic expression in infix notation.
        :return: A list representing the postfix expression.
        """
        stack = []
        postfix = []
        numbers = []
        current_number = []

        for char in expression:
            if char.isdigit() or char == '.':
                current_number.append(char)
            else:
                if current_number:
                    numbers.append(''.join(current_number))
                    current_number = []

                if char in self.operators:
                    while (stack and stack[-1] in self.operators and
                           self.precedence[char] <= self.precedence[stack[-1]]):
                        postfix.append(stack.pop())
                    stack.append(char)
                elif char == '(':
                    stack.append(char)
                elif char == ')':
                    while stack and stack[-1] != '(':
                        postfix.append(stack.pop())
                    if stack:
                        stack.pop()  # Pop the '('

        if current_number:
            numbers.append(''.join(current_number))

        while stack:
            postfix.append(stack.pop())

        # Combine numbers and operators into the final postfix list
        final_postfix = []
        num_index = 0
        for token in postfix:
            if token in self.operators:
                final_postfix.append(token)
            else:
                final_postfix.append(numbers[num_index])
                num_index += 1

        return final_postfix

    def evaluate_postfix(self, postfix: list) -> float:
        """
        Evaluates the postfix expression.

        :param postfix: A list representing the postfix expression.
        :return: The result of the evaluated expression.
        :raises ValueError: If division by zero is attempted.
        """
        stack = []

        for token in postfix:
            if token not in self.operators:
                stack.append(float(token))
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
                        raise ValueError("Division by zero.")
                    stack.append(a / b)

        return stack[0]


if __name__ == "__main__":
    calculator = Calculator()
    expression = "3 + 5 * (2 - 8)"
    try:
        result = calculator.calculate(expression)
        print(f"The result of '{expression}' is: {result}")
    except ValueError as e:
        print(f"Error: {e}")
