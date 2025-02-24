from typing import List, Dict, Union
from collections import deque
import re

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions following mathematical precedence rules.
    Supports operations: +, -, *, / and parentheses ().
    """
    
    def __init__(self):
        """Initialize calculator with operator precedence and supported operations."""
        self.operators: Dict[str, int] = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        
        self.operations = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluate the given arithmetic expression and return the result.
        
        Args:
            expression (str): The arithmetic expression to evaluate
            
        Returns:
            float: The result of the evaluation
            
        Raises:
            ValueError: If the expression is invalid
            ZeroDivisionError: If division by zero is attempted
        """
        try:
            # Validate and tokenize the expression
            tokens = self._tokenize(expression)
            
            # Convert to postfix notation
            postfix = self._to_postfix(tokens)
            
            # Evaluate the postfix expression
            result = self._evaluate_postfix(postfix)
            
            return result
            
        except (ValueError, ZeroDivisionError) as e:
            raise e
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")

    def _tokenize(self, expression: str) -> List[str]:
        """
        Convert expression string into tokens.
        
        Args:
            expression (str): The expression to tokenize
            
        Returns:
            List[str]: List of tokens
            
        Raises:
            ValueError: If invalid characters are found
        """
        # Remove whitespace and validate characters
        expression = expression.replace(' ', '')
        if not re.match(r'^[-0-9+*/(). ]+$', expression):
            raise ValueError("Expression contains invalid characters")

        # Check for balanced parentheses
        if expression.count('(') != expression.count(')'):
            raise ValueError("Unbalanced parentheses")

        tokens = []
        number = ''
        
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(number)
                    number = ''
                if char in self.operators or char in '()':
                    tokens.append(char)
                    
        if number:
            tokens.append(number)
            
        return tokens

    def _to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Convert infix tokens to postfix notation using the Shunting Yard algorithm.
        
        Args:
            tokens (List[str]): List of tokens in infix notation
            
        Returns:
            List[str]: List of tokens in postfix notation
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
            else:  # Operator
                while (operator_stack and operator_stack[-1] != '(' and 
                       self.operators.get(operator_stack[-1], 0) >= 
                       self.operators.get(token, 0)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
                
        while operator_stack:
            output.append(operator_stack.pop())
            
        return output

    def _evaluate_postfix(self, tokens: List[str]) -> float:
        """
        Evaluate a postfix expression.
        
        Args:
            tokens (List[str]): List of tokens in postfix notation
            
        Returns:
            float: Result of the evaluation
            
        Raises:
            ZeroDivisionError: If division by zero is attempted
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
                    
                result = self.operations[token](a, b)
                stack.append(result)
                
        return stack[0]

    @staticmethod
    def _is_number(token: str) -> bool:
        """
        Check if a token is a number.
        
        Args:
            token (str): Token to check
            
        Returns:
            bool: True if token is a number, False otherwise
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
        "2 + 3 * 4",
        "(2 + 3) * 4",
        "2.5 * (3 + 4.5)",
        "-2 + 3"
    ]
    
    for expr in expressions:
        try:
            result = calc.calculate(expr)
            print(f"{expr} = {result}")
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error evaluating {expr}: {str(e)}")

if __name__ == "__main__":
    main()
