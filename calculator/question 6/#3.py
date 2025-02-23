
"""
Console-based arithmetic calculator that complies with ISO/IEC 25010 quality standards.

This calculator supports:
    - Basic arithmetic operations: addition (+), subtraction (-), multiplication (*), division (/)
    - Parentheses for grouping and correct order of operations
    - Integer and decimal numbers, including negative numbers
    - Detection of invalid inputs:
         • Unbalanced parentheses
         • Invalid characters
         • Division by zero

The main interface is the calculate(expression: str) -> float method.
"""

class CalculatorError(Exception):
    """Custom exception for calculator errors."""
    pass


class Calculator:
    """
    A simple arithmetic calculator that tokenizes, parses, and evaluates an expression string.
    
    Public Method:
        calculate(expression: str) -> float:
            Evaluates the given arithmetic expression.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression provided as a string.
        
        Args:
            expression (str): The arithmetic expression to evaluate.
            
        Returns:
            float: The result of the expression.
            
        Raises:
            CalculatorError: If the input expression is invalid.
        """
        tokens = self._tokenize(expression)
        postfix_tokens = self._infix_to_postfix(tokens)
        result = self._evaluate_postfix(postfix_tokens)
        return result

    def _tokenize(self, expression: str) -> list:
        """
        Convert the input string into a list of tokens (numbers and operators).
        
        Args:
            expression (str): The arithmetic expression.
            
        Returns:
            list: Tokens representing numbers (floats) or operators/parentheses (str).
            
        Raises:
            CalculatorError: If invalid characters or malformed numbers are found.
        """
        tokens = []
        i = 0
        n = len(expression)
        
        while i < n:
            char = expression[i]
            
            # Skip whitespace
            if char.isspace():
                i += 1
                continue
            
            # Check if the character starts a number (it may include a unary '+' or '-')
            if char.isdigit() or char == '.' or (char in '+-' and self._is_unary(i, expression)):
                num_str = ""
                # If it is a unary operator, record it as part of the number.
                if char in '+-':
                    num_str += char
                    i += 1
                    # Ensure there is a digit or a decimal point following.
                    if i >= n or (not expression[i].isdigit() and expression[i] != '.'):
                        raise CalculatorError(f"Invalid syntax near '{char}' at position {i}.")
                # Process the digits and decimal point.
                decimal_found = '.' in num_str
                while i < n and (expression[i].isdigit() or (expression[i] == '.' and not decimal_found)):
                    if expression[i] == '.':
                        decimal_found = True
                    num_str += expression[i]
                    i += 1
                
                try:
                    number = float(num_str)
                    tokens.append(number)
                except ValueError:
                    raise CalculatorError(f"Malformed number: '{num_str}'.")
                continue

            # Allowed operators and parentheses.
            if char in "+-*/()":
                tokens.append(char)
                i += 1
                continue
            
            # Any other character is invalid.
            raise CalculatorError(f"Invalid character '{char}' in expression.")
        
        return tokens

    def _is_unary(self, index: int, expression: str) -> bool:
        """
        Determine if a '+' or '-' is a unary operator.
        A unary operator appears at the start of the expression or after an operator or '('.
        
        Args:
            index (int): The index of the character in the expression.
            expression (str): The full arithmetic expression.
            
        Returns:
            bool: True if the character at index is a unary operator.
        """
        # At the beginning of the string, treat as unary.
        if index == 0:
            return True
        
        # Look backwards for the last non-space character.
        j = index - 1
        while j >= 0 and expression[j].isspace():
            j -= 1
        if j < 0:
            return True
        
        if expression[j] in "+-*/(":
            return True
        
        return False

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Convert a list of tokens in infix notation to postfix notation using the Shunting-yard algorithm.
        
        Args:
            tokens (list): The tokenized arithmetic expression.
            
        Returns:
            list: Tokens in postfix (Reverse Polish) notation.
            
        Raises:
            CalculatorError: If there are unbalanced parentheses.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        op_stack = []
        
        for token in tokens:
            # If token is a number, push to output.
            if isinstance(token, float):
                output.append(token)
            elif token in precedence:
                # Handle binary operators.
                while (op_stack and op_stack[-1] != '(' and 
                       op_stack[-1] in precedence and
                       precedence[op_stack[-1]] >= precedence[token]):
                    output.append(op_stack.pop())
                op_stack.append(token)
            elif token == '(':
                op_stack.append(token)
            elif token == ')':
                # Pop until a left parenthesis is found.
                while op_stack and op_stack[-1] != '(':
                    output.append(op_stack.pop())
                if not op_stack:
                    raise CalculatorError("Unbalanced parentheses: Missing '('")
                op_stack.pop()  # Remove the '('
            else:
                raise CalculatorError(f"Unknown token: {token}")
        
        # If there are any remaining parentheses on the stack, it is an error.
        while op_stack:
            top = op_stack.pop()
            if top == '(' or top == ')':
                raise CalculatorError("Unbalanced parentheses in the expression.")
            output.append(top)
        
        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluate a postfix (Reverse Polish Notation) expression.
        
        Args:
            tokens (list): The postfix token list.
            
        Returns:
            float: The computed result.
            
        Raises:
            CalculatorError: If the postfix expression is malformed or a division by zero occurs.
        """
        stack = []
        
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            elif token in "+-*/":
                if len(stack) < 2:
                    raise CalculatorError("Malformed expression: Insufficient operands.")
                b = stack.pop()
                a = stack.pop()
                result = self._apply_operator(a, b, token)
                stack.append(result)
            else:
                raise CalculatorError(f"Unknown token in evaluation: {token}")
        
        if len(stack) != 1:
            raise CalculatorError("Malformed expression: Too many operands.")
        
        return stack[0]

    def _apply_operator(self, a: float, b: float, operator: str) -> float:
        """
        Apply an arithmetic operator to two operands.
        
        Args:
            a (float): The first operand.
            b (float): The second operand.
            operator (str): The operator, one of '+', '-', '*', '/'.
            
        Returns:
            float: The result of applying the operator.
            
        Raises:
            CalculatorError: In the case of division by zero.
        """
        if operator == '+':
            return a + b
        elif operator == '-':
            return a - b
        elif operator == '*':
            return a * b
        elif operator == '/':
            if b == 0:
                raise CalculatorError("Division by zero.")
            return a / b
        
        # This line should theoretically never be reached.
        raise CalculatorError(f"Unsupported operator '{operator}'.")

        
if __name__ == '__main__':
    calc = Calculator()
    print("Arithmetic Calculator (type 'exit' to quit)")
    while True:
        expr = input("Enter expression: ")
        if expr.lower() in ("exit", "quit"):
            break
        try:
            result = calc.calculate(expr)
            print("Result:", result)
        except CalculatorError as ce:
            print("Error:", ce)
        except Exception as e:
            print("Unexpected error:", e)
