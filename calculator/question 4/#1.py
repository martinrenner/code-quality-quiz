
class Calculator:
    """
    A calculator that evaluates arithmetic expressions containing
    addition, subtraction, multiplication, division, and parentheses.
    It supports both integers and decimals (including negative numbers) and
    validates the expression for invalid inputs.
    """

    def __init__(self, expression: str):
        """
        Initializes the Calculator instance by normalizing and validating the expression.
        
        :param expression: The arithmetic expression as a string.
        :raises ValueError: If the expression contains invalid characters or unbalanced parentheses.
        """
        self.expression = self.normalize_expression(expression)
        self.index = 0

    def calculate(self) -> float:
        """
        Evaluates the arithmetic expression.
        
        :return: The result of the expression as a float.
        :raises ValueError: If the expression is invalid or incomplete.
        """
        result = self.parse_expression()
        # After parsing, ensure the whole expression was consumed
        if self.index < len(self.expression):
            raise ValueError("Invalid expression: extra characters found.")
        return result

    def parse_expression(self) -> float:
        """
        Parses an expression following the grammar:
        expression = term { ('+' | '-') term }
        
        :return: The numeric value of the parsed expression.
        """
        value = self.parse_term()
        while self.index < len(self.expression) and self.expression[self.index] in ('+', '-'):
            operator = self.expression[self.index]
            self.index += 1  # consume the operator
            next_term = self.parse_term()
            if operator == '+':
                value += next_term
            else:
                value -= next_term
        return value

    def parse_term(self) -> float:
        """
        Parses a term following the grammar:
        term = factor { ('*' | '/') factor }
        
        :return: The numeric value of the parsed term.
        :raises ZeroDivisionError: If division by zero is encountered.
        """
        value = self.parse_factor()
        while self.index < len(self.expression) and self.expression[self.index] in ('*', '/'):
            operator = self.expression[self.index]
            self.index += 1  # consume the operator
            next_factor = self.parse_factor()
            if operator == '*':
                value *= next_factor
            elif operator == '/':
                if next_factor == 0:
                    raise ZeroDivisionError("Division by zero.")
                value /= next_factor
        return value

    def parse_factor(self) -> float:
        """
        Parses a factor which can be a number, an expression in parentheses,
        or a unary operator followed by a factor.
        
        :return: The numeric value of the parsed factor.
        :raises ValueError: If invalid syntax or mismatched parentheses are found.
        """
        # Handle unary operators + and -
        if self.index < len(self.expression) and self.expression[self.index] in ('+', '-'):
            sign = self.expression[self.index]
            self.index += 1
            factor = self.parse_factor()
            return factor if sign == '+' else -factor

        # Handle parentheses: '(' expression ')'
        if self.index < len(self.expression) and self.expression[self.index] == '(':
            self.index += 1  # consume '('
            value = self.parse_expression()
            if self.index >= len(self.expression) or self.expression[self.index] != ')':
                raise ValueError("Mismatched parentheses.")
            self.index += 1  # consume ')'
            return value

        return self.parse_number()

    def parse_number(self) -> float:
        """
        Parses a number (integer or decimal) from the current position.
        
        :return: The parsed number as a float.
        :raises ValueError: If an invalid number format is encountered.
        """
        start = self.index
        dot_count = 0

        # Allow numbers that begin with digits or a decimal point.
        while self.index < len(self.expression) and (self.expression[self.index].isdigit() or self.expression[self.index] == '.'):
            if self.expression[self.index] == '.':
                dot_count += 1
                if dot_count > 1:
                    raise ValueError("Invalid number: too many decimal points.")
            self.index += 1

        if start == self.index:
            current = self.expression[self.index] if self.index < len(self.expression) else "end of expression"
            raise ValueError(f"Expected a number but found '{current}'.")

        try:
            number_value = float(self.expression[start:self.index])
            return number_value
        except ValueError:
            raise ValueError("Invalid number format.")

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes the arithmetic expression by removing spaces and validating allowed characters.

        :param expression: The arithmetic expression as a string.
        :return: The normalized expression without spaces.
        :raises ValueError: If the expression contains invalid characters or unbalanced parentheses.
        """
        # Define allowed characters (digits, operators, parentheses, and decimal point).
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        # Remove whitespace
        expr = expression.replace(" ", "")

        # Validate balanced parentheses
        if not self.is_balanced(expr):
            raise ValueError("Expression contains unbalanced parentheses.")

        return expr

    def is_balanced(self, expression: str) -> bool:
        """
        Checks whether the expression has properly paired parentheses.
        
        :param expression: The arithmetic expression as a string.
        :return: True if all parentheses are paired correctly, otherwise False.
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


def calculate(expression: str) -> float:
    """
    Evaluates a mathematical arithmetic expression and returns the result.
    
    :param expression: The arithmetic expression as a string.
    :return: The result of the expression as a float.
    :raises Exception: If the expression is invalid.
    """
    calc = Calculator(expression)
    return calc.calculate()


if __name__ == '__main__':
    print("Console-Based Arithmetic Calculator")
    print("Supported operations: +, -, *, / and parentheses ().\n"
          "Enter 'quit' or 'exit' to close the calculator.\n")

    while True:
        try:
            user_input = input("Enter arithmetic expression: ")
            if user_input.lower() in ("quit", "exit"):
                print("Exiting calculator. Goodbye!")
                break
            result = calculate(user_input)
            print("Result:", result)
        except Exception as error:
            print("Error:", error)
