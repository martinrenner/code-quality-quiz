
from typing import List, Union
import re

class Calculator:
    """A calculator class that evaluates arithmetic expressions.
    
    Supports operations: +, -, *, /
    Handles parentheses and follows order of operations.
    """
    
    def __init__(self):
        """Initialize the calculator with operator precedence."""
        self.operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x / y)
        }

    def validate_expression(self, expression: str) -> bool:
        """Validate the input expression.
        
        Args:
            expression (str): The arithmetic expression to validate.
            
        Returns:
            bool: True if expression is valid, False otherwise.
            
        Raises:
            ValueError: If expression contains invalid characters or structure.
        """
        # Check for valid characters
        if not re.match(r'^[\d\s\+\-\*\/\(\)\.]+$', expression):
            raise ValueError("Expression contains invalid characters")
            
        # Check balanced parentheses
        parentheses_count = 0
        for char in expression:
            if char == '(':
                parentheses_count += 1
            elif char == ')':
                parentheses_count -= 1
            if parentheses_count < 0:
                raise ValueError("Unbalanced parentheses")
        if parentheses_count != 0:
            raise ValueError("Unbalanced parentheses")
            
        return True

    def tokenize(self, expression: str) -> List[str]:
        """Convert expression string into tokens.
        
        Args:
            expression (str): The arithmetic expression to tokenize.
            
        Returns:
            List[str]: List of tokens (numbers and operators).
        """
        # Add spaces around operators and parentheses
        for operator in '+-*/()':
            expression = expression.replace(operator, f' {operator} ')
            
        # Split into tokens and remove empty strings
        return [token for token in expression.split() if token]

    def to_postfix(self, tokens: List[str]) -> List[str]:
        """Convert infix notation to postfix notation using Shunting Yard algorithm.
        
        Args:
            tokens (List[str]): List of tokens in infix notation.
            
        Returns:
            List[str]: List of tokens in postfix notation.
        """
        output = []
        operator_stack = []

        for token in tokens:
            if self._is_number(token):
                output.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Remove '('
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                       self.operators[token][0] <= self.operators[operator_stack[-1]][0]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)

        while operator_stack:
            output.append(operator_stack.pop())

        return output

    def evaluate_postfix(self, tokens: List[str]) -> float:
        """Evaluate postfix expression.
        
        Args:
            tokens (List[str]): List of tokens in postfix notation.
            
        Returns:
            float: Result of the expression evaluation.
            
        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        stack = []

        for token in tokens:
            if self._is_number(token):
                stack.append(float(token))
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '/' and b == 0:
                    raise ZeroDivisionError("Division by zero")
                stack.append(self.operators[token][1](a, b))

        return stack[0]

    def calculate(self, expression: str) -> float:
        """Main method to evaluate an arithmetic expression.
        
        Args:
            expression (str): The arithmetic expression to evaluate.
            
        Returns:
            float: Result of the expression evaluation.
            
        Raises:
            ValueError: If expression is invalid.
            ZeroDivisionError: If division by zero is attempted.
        """
        # Remove spaces and validate
        expression = expression.replace(' ', '')
        self.validate_expression(expression)
        
        # Convert to tokens
        tokens = self.tokenize(expression)
        
        # Convert to postfix and evaluate
        postfix = self.to_postfix(tokens)
        return self.evaluate_postfix(postfix)

    def _is_number(self, token: str) -> bool:
        """Check if a token is a number.
        
        Args:
            token (str): Token to check.
            
        Returns:
            bool: True if token is a number, False otherwise.
        """
        try:
            float(token)
            return True
        except ValueError:
            return False


def main():
    """Example usage of the Calculator class."""
    calc = Calculator()
    
    while True:
        try:
            expression = input("Enter an expression (or 'q' to quit): ")
            if expression.lower() == 'q':
                break
                
            result = calc.calculate(expression)
            print(f"Result: {result}")
            
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


calc = Calculator()
print(calc.calculate("2 + 3 * 4"))  # Output: 14.0
print(calc.calculate("(2 + 3) * 4"))  # Output: 20.0
print(calc.calculate("-2.5 + 3.7"))  # Output: 1.2
