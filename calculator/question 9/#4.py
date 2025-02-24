import re  # Importing the regular expression module

class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations,
    parentheses, and error handling.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression.

        Args:
            expression (str): The mathematical expression to evaluate.

        Returns:
            float: The result of the expression.

        Raises:
            ValueError: If the expression is invalid, contains unbalanced
                        parentheses, or involves division by zero.
        """
        try:
            normalized_expression = self.normalize_expression(expression)
            if not self.is_balanced(normalized_expression):
                raise ValueError("Unbalanced parentheses.")
            tokens = self.tokenize(normalized_expression)
            postfix_tokens = self.shunting_yard(tokens)
            result = self.evaluate_postfix(postfix_tokens)
            return result
        except ValueError as e:
            raise ValueError(f"Error evaluating expression: {e}")

    def normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating
        characters.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/().")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def is_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired
        parentheses.

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
        return not stack  # Stack should be empty if balanced

    def tokenize(self, expression: str) -> list:
        """
        Tokenizes a mathematical expression into a list of numbers, operators,
        and parentheses.  Handles multi-digit numbers and decimal points.

        Args:
            expression (str): The normalized mathematical expression.

        Returns:
            list: A list of tokens.
        """
        # Use regular expression to split the expression into tokens
        return re.findall(r"(\d+\.?\d*|\.\d+|[+\-*/()]|\d+)", expression)

    def precedence(self, operator: str) -> int:
        """
        Returns the precedence of a given operator.

        Args:
            operator (str): The operator (+, -, *, /).

        Returns:
            int: The precedence of the operator (higher value means higher
                 precedence).
        """
        if operator in ('+', '-'):
            return 1
        elif operator in ('*', '/'):
            return 2
        return 0  # For parentheses

    def apply_op(self, operators: list, values: list) -> None:
        """Applies operator to values

        Args:
            operators (list): operators stack.
            values (list): values stack.

        Raises:
            ValueError: If there are not enough operands or division by zero
        """
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
                raise ValueError("Division by zero.")
            values.append(left / right)
        else:
            raise ValueError(f"Unknown operator {operator}")

    def shunting_yard(self, tokens: list) -> list:
        """Convert infix notation to postfix notation (Reverse Polish Notation)

        Args:
            tokens (list): List of tokens in infix notation

        Returns:
            list: list of tokens in postfix notation
        """
        output = []
        operators = []
        for token in tokens:
            if re.match(r"(\d+\.?\d*|\.\d+)", token):  # If it's a number
                output.append(float(token))  # Convert to float immediately
            elif token in ('+', '-', '*', '/'):
                # Handle precedence and associativity
                while (operators and operators[-1] != '(' and
                       self.precedence(operators[-1]) >= self.precedence(token)):
                    output.append(operators.pop())
                operators.append(token)

            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators:
                    raise ValueError("Mismatched parentheses")
                operators.pop()  # Pop the '('
            else:
                raise ValueError(f"Invalid token: {token}")  # Shouldn't happen

        while operators:
            if operators[-1] =='(':
                raise ValueError("Mismatched parentheses")
            output.append(operators.pop())
        return output

    def evaluate_postfix(self, postfix_tokens: list) -> float:
        """Evaluates a postfix expression

        Args:
            postfix_tokens (list): List of tokens in postfix notation

        Returns:
            float: Result of evaluation

        Raises:
            ValueError: If invalid expression. For example: 2 2 + -
        """
        values = []
        for token in postfix_tokens:
            if isinstance(token, float):
                values.append(token)
            else:
                self.apply_op(['',token], values)

        if len(values) != 1:
            raise ValueError("Invalid expression")
        return values[0]

# Example Usage and Testing
if __name__ == "__main__":
    calculator = Calculator()

    test_cases = [
        ("1 + 2", 3.0),
        ("1+2*3", 7.0),
        ("(1 + 2) * 3", 9.0),
        ("10 - 5 * 2", 0.0),
        ("10 / 2 - 3", 2.0),
        ("10.5 + 2.5", 13.0),
        ("-5 + 10", 5.0),
        ("2 * (3 + 4) / (1 + 1)", 7.0),
        ("1 + 2 * (3 - 1) / 2", 3.0),
        ("2*(10 - 2*(2 + 1))", 8.0),
        ("1.2*2.4", 2.88)

    ]
    failed_cases = 0
    for expression, expected in test_cases:
        try:
            result = calculator.calculate(expression)
            print(f"'{expression}' = {result}")
            if abs(result - expected) > 1e-9:  # Floating-point comparison
                print(f"  ERROR: Expected {expected}, got {result}")
                failed_cases +=1
        except ValueError as e:
            print(f"'{expression}' - ERROR: {e}")
            failed_cases += 1


    error_cases = [
        ("1 / 0", "Division by zero."),
        ("1 + (2 * 3", "Unbalanced parentheses."),
        ("(1 + 2) * 3)", "Mismatched parentheses"), # Testing closing parenthesis error
        ("1 & 2", "Expression contains invalid characters."),
        ("2 2 + -", "Invalid expression") # Testing incorrect postfix
    ]
    for expression, expected_error in error_cases:
        try:
            result = calculator.calculate(expression)
            print(f"'{expression}' = {result}  (Should have raised an error)")
            failed_cases += 1
        except ValueError as e:
            print(f"'{expression}' - ERROR (as expected): {e}")
            if str(e).find(expected_error) ==-1:
                print(f"  ERROR Message test failed.  Expected message {expected_error}, got {e}")
                failed_cases += 1
    print(f"Tests completed. Failed cases count: {failed_cases}")


    while True:
        try:
            user_input = input("Enter a mathematical expression (or 'quit'): ")
            if user_input.lower() == 'quit':
                break
            result = calculator.calculate(user_input)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

