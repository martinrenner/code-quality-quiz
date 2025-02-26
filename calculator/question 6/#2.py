from typing import List, Tuple, Optional
import re


class Calculator:
    """
    A calculator class that evaluates arithmetic expressions.
    Supports addition, subtraction, multiplication, division and parentheses.
    """

    def __init__(self):
        """Initialize the calculator."""
        self.operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x / y)
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        Args:
            expression (str): A string containing a mathematical expression.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression contains invalid characters or syntax.
            ZeroDivisionError: If the expression involves division by zero.
        """
        try:
            # Normalize and validate the expression
            normalized_expr = self._normalize_expression(expression)
            
            # Check for balanced parentheses
            if not self._is_parentheses_balanced(normalized_expr):
                raise ValueError("Unbalanced parentheses in the expression.")

            # Tokenize the expression
            tokens = self._tokenize(normalized_expr)
            
            # Convert to postfix notation and evaluate
            result = self._evaluate_expression(tokens)
            
            return result
        except (ValueError, ZeroDivisionError) as e:
            # Re-raise the exceptions to be handled by the caller
            raise e

    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.

        Args:
            expression (str): A mathematical expression as a string.

        Returns:
            str: The normalized expression without spaces.

        Raises:
            ValueError: If the expression contains invalid characters.
        """
        # Remove all whitespace
        expression = expression.replace(" ", "")
        
        # Check for valid characters
        allowed_chars = set("0123456789+-*/().")
        if not all(char in allowed_chars for char in expression):
            invalid_chars = [char for char in expression if char not in allowed_chars]
            raise ValueError(f"Expression contains invalid characters: {', '.join(invalid_chars)}")
        
        # Handle consecutive operators or misplaced operators
        if re.search(r'[+\-*/]{2,}', expression):
            raise ValueError("Expression contains consecutive operators.")
        
        # Check if expression starts with an invalid operator
        if expression and expression[0] in '*/':
            raise ValueError("Expression cannot start with * or / operator.")
        
        # Check if expression ends with an operator
        if expression and expression[-1] in '+-*/':
            raise ValueError("Expression cannot end with an operator.")
        
        return expression

    def _is_parentheses_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

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
        return not stack

    def _tokenize(self, expression: str) -> List:
        """
        Converts a mathematical expression string into a list of tokens.

        Args:
            expression (str): A normalized mathematical expression.

        Returns:
            List: A list of tokens (numbers and operators).
        """
        tokens = []
        i = 0
        
        # Handle negative numbers at the beginning of the expression
        if expression and expression[0] == '-':
            expression = '0' + expression
        
        # Handle negative numbers after open parenthesis
        expression = re.sub(r'\(-', '(0-', expression)
        
        while i < len(expression):
            char = expression[i]
            
            # If the character is a digit or decimal point, extract the full number
            if char.isdigit() or char == '.':
                num_str = ""
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    num_str += expression[i]
                    i += 1
                
                # Validate the number format
                if num_str.count('.') > 1:
                    raise ValueError(f"Invalid number format: {num_str}")
                
                tokens.append(float(num_str))
                continue
            
            # If the character is an operator or parenthesis, add it as a token
            if char in self.operators or char in '()':
                tokens.append(char)
            
            i += 1
            
        return tokens

    def _evaluate_expression(self, tokens: List) -> float:
        """
        Evaluates a tokenized expression using the Shunting Yard algorithm.

        Args:
            tokens (List): A list of tokens (numbers and operators).

        Returns:
            float: The result of the evaluation.

        Raises:
            ZeroDivisionError: If division by zero is attempted.
            ValueError: If the expression is syntactically invalid.
        """
        # Convert infix to postfix notation using Shunting Yard algorithm
        postfix = self._infix_to_postfix(tokens)
        
        # Evaluate the postfix expression
        value_stack = []
        
        for token in postfix:
            if isinstance(token, (int, float)):
                value_stack.append(token)
            else:
                # Token is an operator
                if len(value_stack) < 2:
                    raise ValueError("Invalid expression syntax: insufficient operands for operator.")
                
                b = value_stack.pop()
                a = value_stack.pop()
                
                # Apply the operator
                _, operation = self.operators[token]
                
                if token == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                
                value_stack.append(operation(a, b))
        
        if len(value_stack) != 1:
            raise ValueError("Invalid expression syntax: the expression did not evaluate to a single result.")
        
        return value_stack[0]

    def _infix_to_postfix(self, tokens: List) -> List:
        """
        Converts an infix expression to postfix notation using the Shunting Yard algorithm.

        Args:
            tokens (List): A list of tokens in infix notation.

        Returns:
            List: A list of tokens in postfix notation.
        """
        output = []
        operator_stack = []
        
        for token in tokens:
            # If token is a number, add it to the output
            if isinstance(token, (int, float)):
                output.append(token)
            # If token is an operator
            elif token in self.operators:
                precedence, _ = self.operators[token]
                # While there's an operator at the top of the stack with higher or equal precedence,
                # pop it to the output
                while (operator_stack and operator_stack[-1] in self.operators and 
                       self.operators[operator_stack[-1]][0] >= precedence):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            # If token is a left parenthesis, push it onto the stack
            elif token == '(':
                operator_stack.append(token)
            # If token is a right parenthesis, pop operators to output until left parenthesis
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()  # Discard the left parenthesis
                else:
                    raise ValueError("Mismatched parentheses in expression.")
        
        # Pop any remaining operators to the output
        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses in expression.")
            output.append(operator_stack.pop())
        
        return output


def calculate(expression: str) -> float:
    """
    Interface function to evaluate a mathematical expression.

    Args:
        expression (str): A string containing a mathematical expression.

    Returns:
        float: The result of the evaluated expression.

    Raises:
        ValueError: If the expression is invalid.
        ZeroDivisionError: If division by zero is attempted.
    """
    calculator = Calculator()
    return calculator.calculate(expression)
