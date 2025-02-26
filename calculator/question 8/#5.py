"""
Arithmetic Calculator Module

This module implements a console-based arithmetic calculator that supports basic
arithmetic operations, parentheses, and follows correct operator precedence rules.
"""
from typing import List, Dict, Union, Tuple
import re


class Calculator:
    """
    A calculator class that evaluates arithmetic expressions.
    
    The calculator supports addition, subtraction, multiplication, division,
    and parentheses with proper operator precedence.
    """
    
    def __init__(self):
        """Initialize the calculator with operator precedence."""
        self.operators = {
            '+': {'precedence': 1, 'associativity': 'left'},
            '-': {'precedence': 1, 'associativity': 'left'},
            '*': {'precedence': 2, 'associativity': 'left'},
            '/': {'precedence': 2, 'associativity': 'left'}
        }
    
    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression and return the result.
        
        Args:
            expression (str): The arithmetic expression to evaluate
            
        Returns:
            float: The result of the expression
            
        Raises:
            ValueError: If the expression is invalid or contains syntax errors
            ZeroDivisionError: If division by zero is attempted
        """
        try:
            # Validate and preprocess the expression
            expression = self._preprocess_expression(expression)
            
            # Convert to postfix notation using the Shunting Yard algorithm
            postfix = self._convert_to_postfix(expression)
            
            # Evaluate the postfix expression
            result = self._evaluate_postfix(postfix)
            return result
        
        except (ValueError, ZeroDivisionError) as e:
            # Re-raise with a more descriptive message
            raise type(e)(f"{str(e)}") from None
            
    def _preprocess_expression(self, expression: str) -> List[str]:
        """
        Validate and preprocess the expression, converting it to a token list.
        
        Args:
            expression (str): The arithmetic expression to preprocess
            
        Returns:
            List[str]: A list of tokens (numbers, operators, parentheses)
            
        Raises:
            ValueError: If the expression is invalid or contains syntax errors
        """
        # Remove whitespace
        expression = expression.replace(' ', '')
        
        if not expression:
            raise ValueError("Expression cannot be empty")
            
        # Validate parentheses
        self._validate_parentheses(expression)
        
        # Tokenize the expression
        tokens = []
        i = 0
        while i < len(expression):
            char = expression[i]
            
            # Handle operators and parentheses
            if char in '+-*/()':
                tokens.append(char)
                i += 1
                
            # Handle numbers (including negatives and decimals)
            elif char.isdigit() or (char == '-' and (i == 0 or expression[i-1] in '(+-*/')):
                # Handle negative numbers
                if char == '-':
                    tokens.append(char)
                    i += 1
                    if i >= len(expression) or not (expression[i].isdigit() or expression[i] == '.'):
                        raise ValueError("Invalid negative number format")
                
                # Extract the complete number
                j = i
                decimal_found = False
                while j < len(expression) and (expression[j].isdigit() or (expression[j] == '.' and not decimal_found)):
                    if expression[j] == '.':
                        decimal_found = True
                    j += 1
                
                number = expression[i:j]
                if number == '.':
                    raise ValueError("Invalid number format: standalone decimal point")
                    
                tokens.append(number)
                i = j
                
            else:
                raise ValueError(f"Invalid character in expression: '{char}'")
        
        # Process unary negations
        processed_tokens = []
        for i, token in enumerate(tokens):
            if token == '-' and (i == 0 or tokens[i-1] in '(+-*/'):
                # This is a unary minus
                if i + 1 < len(tokens) and tokens[i+1] not in '+-*/()':
                    # Next token is a number, combine them
                    next_value = tokens[i+1]
                    if next_value.startswith('-'):
                        # Handle double negation
                        processed_tokens.append(next_value[1:])
                    else:
                        processed_tokens.append(f"-{next_value}")
                    tokens[i+1] = None  # Mark as processed
                else:
                    raise ValueError("Invalid use of negation operator")
            elif token is not None:
                processed_tokens.append(token)
                
        return processed_tokens
        
    def _validate_parentheses(self, expression: str) -> None:
        """
        Validate that parentheses in the expression are balanced.
        
        Args:
            expression (str): The expression to validate
            
        Raises:
            ValueError: If parentheses are unbalanced
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    raise ValueError("Unbalanced parentheses: too many closing parentheses")
                stack.pop()
                
        if stack:
            raise ValueError("Unbalanced parentheses: too many opening parentheses")
    
    def _convert_to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Convert infix notation to postfix (Reverse Polish Notation) using the Shunting Yard algorithm.
        
        Args:
            tokens (List[str]): A list of tokens in infix notation
            
        Returns:
            List[str]: A list of tokens in postfix notation
        """
        output_queue = []
        operator_stack = []
        
        for token in tokens:
            # Number
            if token not in self.operators and token not in '()':
                output_queue.append(token)
                
            # Left parenthesis
            elif token == '(':
                operator_stack.append(token)
                
            # Right parenthesis
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                    
                if operator_stack and operator_stack[-1] == '(':
                    operator_stack.pop()  # Discard the left parenthesis
                else:
                    raise ValueError("Mismatched parentheses")
                    
            # Operator
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                       ((self.operators[token]['associativity'] == 'left' and
                         self.operators[token]['precedence'] <= self._get_precedence(operator_stack[-1])) or
                        (self.operators[token]['associativity'] == 'right' and
                         self.operators[token]['precedence'] < self._get_precedence(operator_stack[-1])))):
                    output_queue.append(operator_stack.pop())
                    
                operator_stack.append(token)
        
        # Pop any remaining operators to the output queue
        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")
            output_queue.append(operator_stack.pop())
            
        return output_queue
    
    def _get_precedence(self, operator: str) -> int:
        """
        Get the precedence of an operator.
        
        Args:
            operator (str): The operator
            
        Returns:
            int: The precedence value
        """
        if operator in self.operators:
            return self.operators[operator]['precedence']
        return 0
    
    def _evaluate_postfix(self, postfix: List[str]) -> float:
        """
        Evaluate a postfix expression.
        
        Args:
            postfix (List[str]): A list of tokens in postfix notation
            
        Returns:
            float: The result of the expression
            
        Raises:
            ValueError: If the expression is invalid
            ZeroDivisionError: If division by zero is attempted
        """
        stack = []
        
        for token in postfix:
            if token in self.operators:
                # Not enough operands
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands")
                    
                # Pop the operands in reverse order (b is first operand, a is second)
                b = stack.pop()
                a = stack.pop()
                
                # Convert operands to float
                try:
                    a, b = float(a), float(b)
                except ValueError:
                    raise ValueError(f"Invalid number format: '{a}' or '{b}'")
                
                # Perform the operation
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ZeroDivisionError("Division by zero is not allowed")
                    stack.append(a / b)
            else:
                # It's a number
                try:
                    stack.append(float(token))
                except ValueError:
                    raise ValueError(f"Invalid number format: '{token}'")
        
        # The result should be the only item left on the stack
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands")
            
        return stack[0]


def main():
    """
    Main function to run the calculator in interactive mode.
    """
    calculator = Calculator()
    print("Arithmetic Calculator (type 'exit' to quit)")
    print("Supported operations: +, -, *, /, and parentheses")
    
    while True:
        try:
            expression = input("\nEnter an expression: ")
            if expression.lower() in ['exit', 'quit']:
                break
                
            result = calculator.calculate(expression)
            
            # Format the result (remove trailing zeros for integers)
            if result.is_integer():
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
                
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {str(e)}")
        except KeyboardInterrupt:
            print("\nExiting...")
            break


if __name__ == "__main__":
    main()
