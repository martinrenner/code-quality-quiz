
"""
Console-Based Arithmetic Calculator

This module implements a calculator that evaluates arithmetic expressions
with addition (+), subtraction (-), multiplication (*), and division (/).
It supports floating-point and integer numbers (including negative numbers)
and handles parentheses with correct operator precedence.

The design meets the requirements in ISO/IEC 25010:
- Correctness: Uses recursive descent parsing for correct operator precedence.
- Performance: Efficient single-pass tokenization and recursive descent evaluation.
- Modularity: Code is structured into clearly separated methods.
- Security: Avoids use of eval() and validates input for invalid characters,
  unbalanced parentheses, and division by zero.
- Testability: The Calculator class and its calculate() method facilitate unit testing.
- Readability & Documentation: Clear variable names, inline comments, and docstrings.

Usage:
    calc = Calculator()
    result = calc.calculate("3 + 4 * (2 - 1) / 5")
    print(result)
    
Run this module to start a console-based interactive calculator.
"""

class Calculator:
    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression and return its result as a float.
        
        The expression may contain integers, floating-point numbers, parentheses,
        and the operators +, -, *, /.
        
        Parameters:
            expression (str): The arithmetic expression to evaluate.
            
        Returns:
            float: The result of the evaluated expression.
            
        Raises:
            ValueError: If the expression contains invalid syntax or characters.
            ZeroDivisionError: If a division by zero is encountered.
        """
        # Tokenize the string input
        self.tokens = self._tokenize(expression)
        self.index = 0  # Initialize the token pointer
        
        # Parse the tokens using a recursive descent parser
        result = self._parse_expression()
        
        # Ensure all tokens were consumed; otherwise, the input was invalid.
        if self.index < len(self.tokens):
            raise ValueError(f"Unexpected token '{self.tokens[self.index]}' at position {self.index}.")
        return result

    def _tokenize(self, expression: str):
        """
        Convert the input string into a list of tokens.
        
        Tokens may be floats (for numbers) or strings (for operators and parentheses).
        
        Parameters:
            expression (str): The input arithmetic expression.
        
        Returns:
            list: A list of tokens.
            
        Raises:
            ValueError: If an invalid character is encountered.
        """
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1
                continue
            elif char.isdigit() or char == '.':
                # Parse a number (integer or floating-point)
                num_str = char
                dot_count = 1 if char == '.' else 0
                i += 1
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        dot_count += 1
                        if dot_count > 1:
                            raise ValueError("Invalid number format: multiple decimal points.")
                    num_str += expression[i]
                    i += 1
                try:
                    number = float(num_str)
                except ValueError:
                    raise ValueError(f"Invalid number format: {num_str}")
                tokens.append(number)
            elif char in '+-*/()':
                tokens.append(char)
                i += 1
            else:
                raise ValueError(f"Invalid character encountered: {char}")
        return tokens

    def _parse_expression(self) -> float:
        """
        Parse and evaluate an expression with addition and subtraction.
        
        Returns:
            float: The evaluated result of the expression.
        """
        result = self._parse_term()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('+', '-'):
            op = self.tokens[self.index]
            self.index += 1
            term = self._parse_term()
            if op == '+':
                result += term
            else:
                result -= term
        return result

    def _parse_term(self) -> float:
        """
        Parse and evaluate a term with multiplication and division.
        
        Returns:
            float: The evaluated result of the term.
        """
        result = self._parse_factor()
        while self.index < len(self.tokens) and self.tokens[self.index] in ('*', '/'):
            op = self.tokens[self.index]
            self.index += 1
            factor = self._parse_factor()
            if op == '*':
                result *= factor
            else:
                if factor == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                result /= factor
        return result

    def _parse_factor(self) -> float:
        """
        Parse and evaluate a factor, which may be a number, a parenthesized expression,
        or a number preceded by a unary plus or minus.
        
        Returns:
            float: The evaluated result of the factor.
        """
        # Handle unary operators (plus or minus)
        if self.index < len(self.tokens) and self.tokens[self.index] in ('+', '-'):
            op = self.tokens[self.index]
            self.index += 1
            factor = self._parse_factor()
            return -factor if op == '-' else factor

        # Evaluate numbers and parentheses
        if self.index >= len(self.tokens):
            raise ValueError("Unexpected end of expression.")
        
        token = self.tokens[self.index]
        if isinstance(token, float):
            self.index += 1
            return token
        elif token == '(':
            self.index += 1  # Consume '('
            result = self._parse_expression()
            if self.index >= len(self.tokens) or self.tokens[self.index] != ')':
                raise ValueError("Mismatched parentheses: ')' expected.")
            self.index += 1  # Consume ')'
            return result
        else:
            raise ValueError(f"Unexpected token '{token}' encountered.")

if __name__ == '__main__':
    # Instantiate the Calculator
    calc = Calculator()
    print("Console-Based Arithmetic Calculator")
    print("Type 'exit' to quit.")

    while True:
        try:
            user_input = input("Enter expression: ").strip()
            if user_input.lower() == 'exit':
                print("Exiting the calculator. Goodbye!")
                break
            if not user_input:
                continue  # Skip empty input
            result = calc.calculate(user_input)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
