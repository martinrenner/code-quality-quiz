from typing import List, Union
from collections import deque
import re

class Calculator:
    """A calculator class that evaluates arithmetic expressions.
    
    Supports operations: +, -, *, /
    Handles parentheses and follows order of operations
    Accepts integers and decimal numbers (positive and negative)
    """
    
    def __init__(self):
        """Initialize calculator with operator precedence."""
        self.operators = {
            '+': {'precedence': 1, 'associativity': 'left'},
            '-': {'precedence': 1, 'associativity': 'left'},
            '*': {'precedence': 2, 'associativity': 'left'},
            '/': {'precedence': 2, 'associativity': 'left'}
        }

    def calculate(self, expression: str) -> float:
        """Evaluate the arithmetic expression and return the result.
        
        Args:
            expression (str): Arithmetic expression as string
            
        Returns:
            float: Result of the evaluation
            
        Raises:
            ValueError: If expression is invalid
        """
        try:
            # Validate and tokenize the expression
            tokens = self._tokenize(expression)
            # Convert to postfix notation
            postfix = self._infix_to_postfix(tokens)
            # Evaluate postfix expression
            result = self._evaluate_postfix(postfix)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _tokenize(self, expression: str) -> List[str]:
        """Convert expression string to list of tokens.
        
        Args:
            expression (str): Input expression
            
        Returns:
            List[str]: List of tokens
        """
        # Remove spaces and validate characters
        expression = expression.replace(' ', '')
        if not re.match(r'^[-+*/().\d]+$', expression):
            raise ValueError("Invalid characters in expression")

        # Handle negative numbers
        expression = self._handle_negative_numbers(expression)
        
        # Split into tokens
        tokens = []
        number = ''
        
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = ''
                tokens.append(char)
                
        if number:
            tokens.append(number)
            
        return tokens

    def _handle_negative_numbers(self, expression: str) -> str:
        """Handle negative numbers in the expression.
        
        Args:
            expression (str): Input expression
            
        Returns:
            str: Processed expression
        """
        # Replace negative numbers with temporary marker
        processed = expression
        processed = re.sub(r'(^-|\(-)', '(0-', processed)
        return processed

    def _infix_to_postfix(self, tokens: List[str]) -> List[str]:
        """Convert infix notation to postfix notation using shunting yard algorithm.
        
        Args:
            tokens (List[str]): List of tokens in infix notation
            
        Returns:
            List[str]: List of tokens in postfix notation
        """
        output = []
        operator_stack = deque()
        
        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Unmatched parentheses")
                operator_stack.pop()  # Remove '('
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                       (self.operators[operator_stack[-1]]['precedence'] >
                        self.operators[token]['precedence'] or
                        (self.operators[operator_stack[-1]]['precedence'] ==
                         self.operators[token]['precedence'] and
                         self.operators[token]['associativity'] == 'left'))):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Unmatched parentheses")
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, tokens: List[str]) -> float:
        """Evaluate postfix expression.
        
        Args:
            tokens (List[str]): List of tokens in postfix notation
            
        Returns:
            float: Result of evaluation
        """
        stack = deque()
        
        for token in tokens:
            if self._is_number(token):
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression")
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
                        raise ValueError("Division by zero")
                    stack.append(a / b)

        if len(stack) != 1:
            raise ValueError("Invalid expression")
            
        return stack[0]

    def _is_number(self, token: str) -> bool:
        """Check if token is a number.
        
        Args:
            token (str): Token to check
            
        Returns:
            bool: True if token is a number
        """
        try:
            float(token)
            return True
        except ValueError:
            return False


def main():
    calc = Calculator()
    
    # Test cases
    expressions = [
        "2 + 3",
        "2.5 * (3 + 4)",
        "-2 * 3",
        "(1 + 2) * (3 + 4)",
        "10 / 2"
    ]
    
    for expr in expressions:
        try:
            result = calc.calculate(expr)
            print(f"{expr} = {result}")
        except ValueError as e:
            print(f"Error evaluating '{expr}': {str(e)}")

if __name__ == "__main__":
    main()
