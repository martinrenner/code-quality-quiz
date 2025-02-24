class Calculator:
    """
    A console-based arithmetic calculator that evaluates expressions with 
    addition (+), subtraction (-), multiplication (*), and division (/).
    It supports parentheses, integers, decimals, and negative numbers.
    
    This implementation meets ISO/IEC 25010 requirements on functionality,
    performance, modularity, safety, testability, readability, and documentation.
    
    Usage:
        calc = Calculator()
        result = calc.calculate("3 + 4 * (2 - 1)")
    """

    def __init__(self):
        # Define binary operators with their precedence and operation functions.
        # (precedence, function)
        self.binary_operators = {
            '+': (1, lambda a, b: a + b),
            '-': (1, lambda a, b: a - b),
            '*': (2, lambda a, b: a * b),
            '/': (2, self.safe_division)
        }
        # Define unary operators with high precedence (right-associative).
        # For example, 'u-' represents a unary minus and 'u+' a unary plus.
        self.unary_operators = {
            'u-': (3, lambda a: -a),
            'u+': (3, lambda a: a)
        }

    def safe_division(self, a, b):
        """Divides a by b with a check for division by zero."""
        if b == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return a / b

    def calculate(self, expression: str) -> float:
        """
        Evaluates an arithmetic expression.
        
        Args:
            expression (str): The arithmetic expression to evaluate.
        
        Returns:
            float: The result of the evaluated expression.
        
        Raises:
            ValueError: If the expression contains invalid tokens or 
                        parentheses are unbalanced.
            ZeroDivisionError: If division by zero is attempted.
        """
        tokens = self.tokenize(expression)
        rpn = self.to_rpn(tokens)
        result = self.evaluate_rpn(rpn)
        return result

    def tokenize(self, expression: str):
        """
        Converts the input expression string into a list of tokens (numbers, operators,
        and parentheses). It handles both binary and unary use of '+' and '-'.
        
        For example:
            " -3.5 + (2 * -4)"  ->  [ -3.5, '+', '(', 2.0, '*', -4.0, ')' ]
            "+(3+4)"           ->  [ 'u+', '(', 3.0, '+', 4.0, ')' ]
        
        Args:
            expression (str): The input arithmetic expression.
        
        Returns:
            list: A list containing float numbers and operator strings.
        
        Raises:
            ValueError: If an invalid character or improperly formatted number is found.
        """
        tokens = []
        i = 0
        length = len(expression)

        while i < length:
            char = expression[i]

            if char.isspace():
                i += 1
                continue

            # If the character starts a number (digit or decimal point)
            if char.isdigit() or char == '.':
                num_str = ""
                dot_count = 0
                while i < length and (expression[i].isdigit() or expression[i] == '.'):
                    if expression[i] == '.':
                        dot_count += 1
                        if dot_count > 1:
                            raise ValueError("Invalid number format: multiple decimal points.")
                    num_str += expression[i]
                    i += 1
                try:
                    tokens.append(float(num_str))
                except ValueError:
                    raise ValueError(f"Invalid number format: {num_str}")

            # Handle both '+' and '-' which can be unary or binary.
            elif char in '+-':
                # Determine if this is a unary operator.
                # It is unary if it is the first token or if the previous token is
                # an operator (binary or unary) or a left parenthesis.
                if (len(tokens) == 0 or 
                    (isinstance(tokens[-1], str) and tokens[-1] in list(self.binary_operators.keys()) + 
                     list(self.unary_operators.keys()) + ['('])):
                    # If the next character is a digit or a decimal point, combine it with the number.
                    if i + 1 < length and (expression[i + 1].isdigit() or expression[i + 1] == '.'):
                        sign = char
                        i += 1
                        num_str = sign
                        dot_count = 0
                        while i < length and (expression[i].isdigit() or expression[i] == '.'):
                            if expression[i] == '.':
                                dot_count += 1
                                if dot_count > 1:
                                    raise ValueError("Invalid number format: multiple decimal points.")
                            num_str += expression[i]
                            i += 1
                        try:
                            tokens.append(float(num_str))
                        except ValueError:
                            raise ValueError(f"Invalid number format: {num_str}")
                    else:
                        # It's a unary operator (applied not directly to a number, e.g. "+(" or "-(").
                        if char == '-':
                            tokens.append('u-')
                        else:
                            tokens.append('u+')
                        i += 1
                else:
                    # Otherwise, it's a binary operator.
                    tokens.append(char)
                    i += 1

            elif char in '*/':
                tokens.append(char)
                i += 1

            elif char in '()':
                tokens.append(char)
                i += 1

            else:
                raise ValueError(f"Invalid character found: {char}")

        return tokens

    def to_rpn(self, tokens):
        """
        Converts the list of tokens in infix notation to Reverse Polish Notation (RPN)
        using the Shunting Yard algorithm. It respects the correct order of operations
        and handles both binary and unary operators.
        
        Args:
            tokens (list): The list of tokens from tokenize().
        
        Returns:
            list: A list of tokens in RPN order.
        
        Raises:
            ValueError: If parentheses are mismatched or an unknown token is encountered.
        """
        output_queue = []
        operator_stack = []

        def is_operator(token):
            return token in self.binary_operators or token in self.unary_operators

        for token in tokens:
            if isinstance(token, float):
                output_queue.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses detected.")
                operator_stack.pop()  # Remove the '(' from the stack.
            elif token in self.binary_operators:
                token_precedence = self.binary_operators[token][0]
                # Pop operators from the stack that have higher or equal precedence.
                while (operator_stack and operator_stack[-1] != '(' and is_operator(operator_stack[-1])):
                    top = operator_stack[-1]
                    if top in self.binary_operators:
                        top_precedence = self.binary_operators[top][0]
                        if top_precedence >= token_precedence:
                            output_queue.append(operator_stack.pop())
                        else:
                            break
                    elif top in self.unary_operators:
                        top_precedence = self.unary_operators[top][0]
                        # For left-associative binary operators, pop unary operators with higher precedence.
                        if top_precedence > token_precedence:
                            output_queue.append(operator_stack.pop())
                        else:
                            break
                    else:
                        break
                operator_stack.append(token)
            elif token in self.unary_operators:
                token_precedence = self.unary_operators[token][0]
                # For right-associative unary operators, pop only those with strictly higher precedence.
                while (operator_stack and operator_stack[-1] != '(' and is_operator(operator_stack[-1])):
                    top = operator_stack[-1]
                    if top in self.unary_operators:
                        top_precedence = self.unary_operators[top][0]
                        if top_precedence > token_precedence:
                            output_queue.append(operator_stack.pop())
                        else:
                            break
                    elif top in self.binary_operators:
                        top_precedence = self.binary_operators[top][0]
                        if top_precedence >= token_precedence:
                            output_queue.append(operator_stack.pop())
                        else:
                            break
                    else:
                        break
                operator_stack.append(token)
            else:
                raise ValueError(f"Unknown token encountered: {token}")

        # Pop any remaining operators from the stack.
        while operator_stack:
            top = operator_stack.pop()
            if top == '(' or top == ')':
                raise ValueError("Mismatched parentheses detected.")
            output_queue.append(top)

        return output_queue

    def evaluate_rpn(self, tokens):
        """
        Evaluates the expression presented in Reverse Polish Notation (RPN).
        
        Args:
            tokens (list): The list of tokens in RPN order.
        
        Returns:
            float: The computed result.
        
        Raises:
            ValueError: If the expression is invalid (e.g., too few operands).
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token in self.binary_operators:
                if len(stack) < 2:
                    raise ValueError("Invalid expression; insufficient values for binary operation.")
                b = stack.pop()
                a = stack.pop()
                result = self.binary_operators[token][1](a, b)
                stack.append(result)
            elif token in self.unary_operators:
                if len(stack) < 1:
                    raise ValueError("Invalid expression; insufficient values for unary operation.")
                a = stack.pop()
                result = self.unary_operators[token][1](a)
                stack.append(result)
            else:
                raise ValueError(f"Unknown operator in RPN: {token}")

        if len(stack) != 1:
            raise ValueError("Invalid expression; too many values left after evaluation.")

        return stack[0]


if __name__ == "__main__":
    calc = Calculator()
    print("Console-based Arithmetic Calculator")
    print("Enter an arithmetic expression (or type 'exit' to quit):")
    
    while True:
        try:
            expr = input(">> ")
            if expr.lower() in ['exit', 'quit']:
                break
            result = calc.calculate(expr)
            print("Result:", result)
        except Exception as e:
            print("Error:", e)
