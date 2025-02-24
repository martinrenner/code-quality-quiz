class Calculator:
    """
    A simple arithmetic calculator that supports addition, subtraction,
    multiplication, division, and parentheses. It accepts both integers
    and floating-point numbers (including negative values) and validates
    the input for unbalanced parentheses, invalid characters, and division by zero.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates an arithmetic expression and returns the result as a float.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression contains invalid characters,
                        unbalanced parentheses, or invalid syntax.
            ZeroDivisionError: If a division by zero occurs.
        """
        normalized_expr = self._normalize_expression(expression)
        if not self._is_balanced(normalized_expr):
            raise ValueError("The expression has unbalanced parentheses.")

        self.expression = normalized_expr
        self.index = 0  # Pointer to the current character in the expression

        result = self._parse_expression()

        if self.index < len(self.expression):
            raise ValueError("Invalid syntax: Unexpected characters found in the expression.")

        return result

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the expression by removing spaces and ensuring that all characters are allowed.

        Args:
            expression (str): The arithmetic expression as a string.

        Returns:
            str: The normalized expression with spaces removed.

        Raises:
            ValueError: If the expression contains disallowed characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")
        return expression.replace(" ", "")

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks if the parentheses in the expression are balanced.

        Args:
            expression (str): The normalized arithmetic expression.

        Returns:
            bool: True if parentheses are correctly paired, False otherwise.
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

    def _parse_expression(self) -> float:
        """
        Parses and evaluates an expression, handling additions and subtractions.

        Returns:
            float: The evaluated result of the expression.
        """
        result = self._parse_term()
        while self.index < len(self.expression) and self.expression[self.index] in "+-":
            operator = self.expression[self.index]
            self.index += 1
            operand = self._parse_term()
            if operator == '+':
                result += operand
            elif operator == '-':
                result -= operand
        return result

    def _parse_term(self) -> float:
        """
        Parses and evaluates a term, handling multiplication and division.

        Returns:
            float: The evaluated result of the term.
        """
        result = self._parse_factor()
        while self.index < len(self.expression) and self.expression[self.index] in "*/":
            operator = self.expression[self.index]
            self.index += 1
            operand = self._parse_factor()
            if operator == '*':
                result *= operand
            elif operator == '/':
                if operand == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result /= operand
        return result

    def _parse_factor(self) -> float:
        """
        Parses and evaluates a factor, which can be a number, a parenthesized expression,
        or an expression preceded by a unary operator (+ or -).

        Returns:
            float: The evaluated result of the factor.
        """
        # Handle unary operators
        if self.index < len(self.expression) and self.expression[self.index] in "+-":
            sign = self.expression[self.index]
            self.index += 1
            factor = self._parse_factor()
            return factor if sign == '+' else -factor

        # Handle parentheses
        if self.index < len(self.expression) and self.expression[self.index] == '(':
            self.index += 1  # Skip '('
            result = self._parse_expression()
            if self.index >= len(self.expression) or self.expression[self.index] != ')':
                raise ValueError("Missing closing parenthesis.")
            self.index += 1  # Skip ')'
            return result

        # Handle numbers
        return self._parse_number()

    def _parse_number(self) -> float:
        """
        Extracts a number (integer or floating-point) from the current position in the expression.

        Returns:
            float: The parsed numeric value.

        Raises:
            ValueError: If no valid number is found at the current position.
        """
        start_idx = self.index
        has_digit = False

        while self.index < len(self.expression) and (self.expression[self.index].isdigit() or self.expression[self.index] == '.'):
            if self.expression[self.index].isdigit():
                has_digit = True
            self.index += 1

        if not has_digit:
            raise ValueError(f"Expected a number at position {start_idx}.")

        number_str = self.expression[start_idx:self.index]
        try:
            return float(number_str)
        except ValueError:
            raise ValueError(f"Invalid number: {number_str}")


def main():
    """
    Console interface for the arithmetic calculator.
    Prompts the user for an expression, evaluates it, and prints the result.
    The loop continues until the user types 'exit'.
    """
    calculator = Calculator()
    print("Console-based Arithmetic Calculator")
    print("Enter an arithmetic expression (or type 'exit' to quit):")
    
    while True:
        try:
            expr = input(">> ").strip()
            if expr.lower() == 'exit':
                break
            if expr == "":
                continue
            result = calculator.calculate(expr)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()
