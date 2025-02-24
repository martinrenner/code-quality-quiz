#!/usr/bin/env python3
"""
Console-Based Arithmetic Calculator

This calculator evaluates arithmetic expressions supporting addition (+),
subtraction (-), multiplication (*), division (/), parentheses grouping, proper
operator precedence, and both integer and floating-point numbers (including negatives).

It validates input for errors such as invalid characters, unbalanced parentheses, and division by zero.
The main interface is the calculate(expression: str) -> float method of the Calculator class.
"""

class CalculatorError(Exception):
    """
    Exception class for errors encountered in the Calculator.
    """
    pass

class Calculator:
    """
    A simple arithmetic calculator that supports +, -, *, /, and parenthesized expressions.
    
    The calculator uses a recursive descent parser to ensure correct operator precedence and 
    validation of the input expression.
    """
    
    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression provided as a string.
        
        :param expression: A string representing the arithmetic expression.
        :return: The result of the evaluated expression as a float.
        :raises CalculatorError: If the expression contains invalid syntax or operations (e.g., division by zero).
        """
        self.tokens = self._tokenize(expression)
        self.pos = 0
        result = self._parse_expression()
        if self.pos < len(self.tokens):
            raise CalculatorError(f"Unexpected token '{self.tokens[self.pos]}' at position {self.pos}.")
        return result

    def _tokenize(self, expression: str) -> list:
        """
        Convert the input expression into a list of tokens.
        
        Numbers are converted to float, while operators and parentheses remain as strings.
        
        :param expression: The arithmetic expression string.
        :return: List of tokens.
        :raises CalculatorError: If an invalid character is encountered or number formatting is invalid.
        """
        tokens = []
        index = 0
        while index < len(expression):
            char = expression[index]
            # Skip any whitespace characters.
            if char.isspace():
                index += 1
                continue
            # Process numbers (integer and floating-point).
            if char.isdigit() or char == '.':
                num_str = ''
                dot_count = 0
                while index < len(expression) and (expression[index].isdigit() or expression[index] == '.'):
                    if expression[index] == '.':
                        dot_count += 1
                        if dot_count > 1:
                            raise CalculatorError("Invalid number format: multiple decimals in a number.")
                    num_str += expression[index]
                    index += 1
                try:
                    number = float(num_str)
                except ValueError:
                    raise CalculatorError(f"Invalid number format: '{num_str}'")
                tokens.append(number)
                continue
            # Process valid operators and parentheses.
            if char in '+-*/()':
                tokens.append(char)
                index += 1
                continue
            # Any other character is considered invalid.
            raise CalculatorError(f"Invalid character encountered: '{char}'")
        return tokens

    def _parse_expression(self) -> float:
        """
        Parse and evaluate an expression which may consist of terms combined by '+' and '-'.
        
        :return: The numerical result of the expression.
        """
        value = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_term()
            if op == '+':
                value += right
            elif op == '-':
                value -= right
        return value

    def _parse_term(self) -> float:
        """
        Parse and evaluate a term, handling multiplication and division.
        
        :return: The numerical result of the term.
        :raises CalculatorError: If a division by zero is attempted.
        """
        value = self._parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('*', '/'):
            op = self.tokens[self.pos]
            self.pos += 1
            right = self._parse_factor()
            if op == '*':
                value *= right
            elif op == '/':
                if right == 0:
                    raise CalculatorError("Division by zero is not allowed.")
                value /= right
        return value

    def _parse_factor(self) -> float:
        """
        Parse and evaluate a factor which can be a number, a parenthesized expression,
        or an expression preceded by a unary '+' or '-'.

        :return: The numerical result of the factor.
        :raises CalculatorError: If the expression syntax is invalid (e.g., missing closing parenthesis).
        """
        if self.pos >= len(self.tokens):
            raise CalculatorError("Unexpected end of expression.")

        token = self.tokens[self.pos]

        # Handle unary minus (and unary plus).
        if token == '-':
            self.pos += 1
            return -self._parse_factor()
        if token == '+':
            self.pos += 1
            return self._parse_factor()

        # Handle parenthesized expressions.
        if token == '(':
            self.pos += 1
            value = self._parse_expression()
            if self.pos >= len(self.tokens) or self.tokens[self.pos] != ')':
                raise CalculatorError("Unbalanced parentheses: missing ')'.")
            self.pos += 1
            return value

        # Handle numeric tokens.
        if isinstance(token, float):
            self.pos += 1
            return token

        # If none of the above, the token is unexpected.
        raise CalculatorError(f"Unexpected token: {token}")

if __name__ == '__main__':
    # Create a Calculator instance.
    calculator = Calculator()
    print("Console-Based Arithmetic Calculator")
    print("Enter an arithmetic expression (or type 'exit' to quit):\n")
    
    while True:
        try:
            user_input = input("Enter expression: ")
            if user_input.strip().lower() == 'exit':
                print("Goodbye!")
                break
            result = calculator.calculate(user_input)
            print("Result:", result)
        except CalculatorError as error:
            print("Error:", error)
        except Exception as error:
            print("Unexpected Error:", error)
