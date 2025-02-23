
class Calculator:
    """
    A console-based arithmetic calculator that evaluates expressions
    with addition (+), subtraction (-), multiplication (*), division (/),
    and supports parentheses. It correctly applies operator precedence,
    accepts integers, floats, and negative values, and validates user input.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression and return the result as a float.
        
        :param expression: A string containing the arithmetic expression.
        :return: The evaluated result as a float.
        :raises ValueError: If the expression is invalid.
        """
        tokens = self._tokenize(expression)
        rpn = self._to_rpn(tokens)
        result = self._evaluate_rpn(rpn)
        return result

    def _tokenize(self, expression: str) -> list:
        """
        Tokenize the input expression into numbers and operators.
        Supports both binary operators and unary plus/minus.
        
        Tokens:
          - numbers are stored as floats
          - operators and parentheses are stored as strings
        
        :param expression: The arithmetic expression to tokenize.
        :return: A list of tokens.
        :raises ValueError: If an invalid character or syntax error is encountered.
        """
        tokens = []
        n = len(expression)
        i = 0

        while i < n:
            char = expression[i]

            # Skip whitespace
            if char.isspace():
                i += 1
                continue

            # If the character is a digit or a decimal point, parse a number.
            if char.isdigit() or char == '.':
                start = i
                dot_count = 0
                while i < n and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        dot_count += 1
                        if dot_count > 1:
                            raise ValueError("Invalid number format: multiple decimal points.")
                    i += 1
                num_str = expression[start:i]
                try:
                    num = float(num_str)
                except ValueError:
                    raise ValueError(f"Invalid number: {num_str}")
                tokens.append(num)
                continue

            # Check for a plus or minus sign.
            if char in '+-':
                # Determine if this is a unary operator.
                # It is unary if it appears at the beginning or after another operator or '('.
                if not tokens or (isinstance(tokens[-1], str) and tokens[-1] in "+-*/("):
                    # Process a sequence of unary signs (e.g., "--" or "+-")
                    sign = 1
                    while i < n and expression[i] in '+-':
                        if expression[i] == '-':
                            sign *= -1
                        # For '+' the sign remains the same.
                        i += 1
                    # Skip any whitespace following the sign(s)
                    while i < n and expression[i].isspace():
                        i += 1
                    # Check if the sign is applied to a number...
                    if i < n and (expression[i].isdigit() or expression[i] == '.'):
                        start = i
                        dot_count = 0
                        while i < n and (expression[i].isdigit() or expression[i] == '.'):
                            if expression[i] == '.':
                                dot_count += 1
                                if dot_count > 1:
                                    raise ValueError("Invalid number format: multiple decimal points.")
                            i += 1
                        num_str = expression[start:i]
                        try:
                            num = float(num_str) * sign
                        except ValueError:
                            raise ValueError(f"Invalid number: {num_str}")
                        tokens.append(num)
                        continue
                    # Alternatively, the unary operator might precede a parenthesized sub-expression.
                    elif i < n and expression[i] == '(':
                        # For a negative sign, convert "-(expr)" to "(-1) * (expr)"
                        if sign == -1:
                            tokens.append(-1.0)
                            tokens.append('*')
                        # If sign is positive, we simply let the '(' be processed normally.
                        # Do not increment i here so that the '(' is handled below.
                        continue
                    else:
                        raise ValueError("Invalid syntax: unary operator not followed by a number or '('.")
                else:
                    # Binary operator: add the '+' or '-' operator as a token.
                    tokens.append(char)
                    i += 1
                    continue

            # Process multiplication and division operators.
            if char in '*/':
                tokens.append(char)
                i += 1
                continue

            # Process parentheses.
            if char in '()':
                tokens.append(char)
                i += 1
                continue

            # If no valid token is found, raise an error.
            raise ValueError(f"Invalid character encountered: {char}")

        # Validate balanced parentheses.
        balance = 0
        for token in tokens:
            if token == '(':
                balance += 1
            elif token == ')':
                balance -= 1
                if balance < 0:
                    raise ValueError("Unbalanced parentheses: too many closing parentheses.")
        if balance != 0:
            raise ValueError("Unbalanced parentheses: missing closing parentheses.")
        return tokens

    def _to_rpn(self, tokens: list) -> list:
        """
        Convert the tokenized infix expression to Reverse Polish Notation (RPN)
        using the Shunting Yard algorithm.
        
        :param tokens: List of tokens in infix order.
        :return: List of tokens in RPN (postfix) order.
        :raises ValueError: If there is a parenthesis mismatch.
        """
        output = []
        operator_stack = []
        # Define operator precedence (all operators are left-associative).
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

        for token in tokens:
            if isinstance(token, float):
                output.append(token)
            elif token in precedence:
                while (operator_stack and operator_stack[-1] in precedence and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                # Pop operators until a left parenthesis is encountered.
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack or operator_stack[-1] != '(':
                    raise ValueError("Mismatched parentheses in the expression.")
                operator_stack.pop()  # Remove the '('
            else:
                raise ValueError(f"Unknown token: {token}")
        # Append any remaining operators to the output.
        while operator_stack:
            if operator_stack[-1] in '()':
                raise ValueError("Mismatched parentheses in the expression.")
            output.append(operator_stack.pop())
        return output

    def _evaluate_rpn(self, tokens: list) -> float:
        """
        Evaluate an expression in Reverse Polish Notation.
        
        :param tokens: List of tokens in RPN order.
        :return: The computed result as a float.
        :raises ValueError: If the expression is syntactically invalid or if division by zero occurs.
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token in ('+', '-', '*', '/'):
                if len(stack) < 2:
                    raise ValueError("Invalid syntax: insufficient values in expression.")
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
                        raise ValueError("Division by zero error.")
                    stack.append(a / b)
            else:
                raise ValueError(f"Unknown operator in evaluation: {token}")
        if len(stack) != 1:
            raise ValueError("Invalid syntax: too many values remain after evaluation.")
        return stack[0]


if __name__ == '__main__':
    calc = Calculator()
    print("Console-based Arithmetic Calculator")
    print("Enter an arithmetic expression (or 'exit' to quit):")
    while True:
        try:
            expr = input("> ")
            if expr.strip().lower() == 'exit':
                break
            result = calc.calculate(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
