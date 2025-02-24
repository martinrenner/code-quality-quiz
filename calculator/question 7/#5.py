class Calculator:
    """
    A console-based arithmetic calculator that evaluates expressions containing
    addition (+), subtraction (-), multiplication (*), division (/), and parentheses.
    It supports integers, floats, and negative numbers, while enforcing operator precedence
    and performing input validation (e.g., unbalanced parentheses, invalid tokens, division by zero).
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.
        
        Parameters:
            expression (str): The arithmetic expression to evaluate.
        
        Returns:
            float: The result of the evaluated expression.
            
        Raises:
            ValueError: If the expression has invalid characters, is malformed, or has unbalanced parentheses.
            ZeroDivisionError: If a division by zero is attempted.
        """
        self.tokens = self._tokenize(expression)
        self.pos = 0  # pointer to current token
        result = self._parse_expression()
        if self.pos < len(self.tokens):
            raise ValueError("Invalid expression: unexpected token(s) at the end.")
        return result

    def _tokenize(self, expression: str) -> list:
        """
        Converts the input expression string into a list of tokens.
        Tokens can be numbers (as strings), operators, or parentheses.
        
        Parameters:
            expression (str): The arithmetic expression.
        
        Returns:
            list: A list of tokens.
            
        Raises:
            ValueError: If an invalid character is encountered or a number contains multiple decimals.
        """
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            if char.isspace():
                i += 1  # skip whitespace
            elif char in "+-*/()":
                tokens.append(char)
                i += 1
            elif char.isdigit() or char == '.':
                num = char
                i += 1
                decimal_count = 1 if char == '.' else 0
                # Build the full number token
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        decimal_count += 1
                        if decimal_count > 1:
                            raise ValueError("Invalid number: multiple decimal points.")
                    num += expression[i]
                    i += 1
                tokens.append(num)
            else:
                raise ValueError(f"Invalid character '{char}' in expression.")
        return tokens

    def _parse_expression(self) -> float:
        """
        Expression := Term {('+' | '-') Term}
        
        Parses an expression and returns its evaluated result.
        """
        value = self._parse_term()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('+', '-'):
            op = self.tokens[self.pos]
            self.pos += 1
            next_value = self._parse_term()
            if op == '+':
                value += next_value
            else:
                value -= next_value
        return value

    def _parse_term(self) -> float:
        """
        Term := Factor {('*' | '/') Factor}
        
        Parses a term and returns its evaluated result.
        """
        value = self._parse_factor()
        while self.pos < len(self.tokens) and self.tokens[self.pos] in ('*', '/'):
            op = self.tokens[self.pos]
            self.pos += 1
            next_value = self._parse_factor()
            if op == '*':
                value *= next_value
            else:
                if next_value == 0:  # Detect division by zero
                    raise ZeroDivisionError("Division by zero is undefined.")
                value /= next_value
        return value

    def _parse_factor(self) -> float:
        """
        Factor := [ ('+' | '-') ] ( Number | '(' Expression ')' )
        
        Parses a factor and returns its evaluated result.
        Supports unary plus and minus as well as parenthesized expressions.
        """
        if self.pos >= len(self.tokens):
            raise ValueError("Unexpected end of expression.")

        token = self.tokens[self.pos]

        # Handle unary operators
        if token == '-':
            self.pos += 1
            return -self._parse_factor()
        elif token == '+':
            self.pos += 1
            return self._parse_factor()
        elif token == '(':
            self.pos += 1  # Consume '('
            value = self._parse_expression()
            if self.pos >= len(self.tokens) or self.tokens[self.pos] != ')':
                raise ValueError("Unbalanced parentheses: missing ')'.")
            self.pos += 1  # Consume ')'
            return value
        else:
            # It should be a numeric token.
            try:
                value = float(token)
                self.pos += 1
                return value
            except ValueError:
                raise ValueError(f"Invalid number: {token}")

if __name__ == "__main__":
    calc = Calculator()
    print("Welcome to the Console Arithmetic Calculator.")
    print("Enter an arithmetic expression to evaluate.")
    print("Type 'exit' or 'quit' to close the calculator.")
    
    while True:
        try:
            user_input = input(">> ")
            if user_input.strip().lower() in ("exit", "quit"):
                print("Goodbye!")
                break
            # Evaluate the expression and print the result.
            result = calc.calculate(user_input)
            print(result)
        except Exception as error:
            print("Error:", str(error))
