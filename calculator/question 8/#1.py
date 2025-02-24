from typing import List, Union
import re

class Calculator:
    """
    A calculator class that evaluates arithmetic expressions following operator precedence.
    Supports addition, subtraction, multiplication, division, and parentheses.
    """

    def __init__(self):
        """Initialize the calculator with operator precedence rules."""
        self.operators = {
            '+': (1, lambda x, y: x + y),
            '-': (1, lambda x, y: x - y),
            '*': (2, lambda x, y: x * y),
            '/': (2, lambda x, y: x / y)
        }

    def tokenize(self, expression: str) -> List[str]:
        """
        Convert expression string into tokens.
        
        Args:
            expression (str): The arithmetic expression to tokenize
            
        Returns:
            List[str]: List of tokens (numbers, operators, parentheses)
            
        Raises:
            ValueError: If invalid characters are found in the expression
        """
        # Remove whitespace and validate characters
        expression = expression.replace(' ', '')
        valid_chars = r'^[0-9+\-*/().,]+$'
        if not re.match(valid_chars, expression):
            raise ValueError("Expression contains invalid characters")

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

    def validate_parentheses(self, tokens: List[str]) -> None:
        """
        Validate parentheses balance in the expression.
        
        Args:
            tokens (List[str]): List of tokens
            
        Raises:
            ValueError: If parentheses are unbalanced
        """
        count = 0
        for token in tokens:
            if token == '(':
                count += 1
            elif token == ')':
                count -= 1
            if count < 0:
                raise ValueError("Unmatched closing parenthesis")
        if count != 0:
            raise ValueError("Unmatched opening parenthesis")

    def to_postfix(self, tokens: List[str]) -> List[str]:
        """
        Convert infix expression to postfix notation using Shunting Yard algorithm.
        
        Args:
            tokens (List[str]): List of tokens in infix notation
            
        Returns:
            List[str]: List of tokens in postfix notation
        """
        output = []
        stack = []

        for token in tokens:
            if token.replace('.', '').replace('-', '').isdigit():
                output.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    output.append(stack.pop())
                stack.pop()  # Remove '('
            else:
                while (stack and stack[-1] != '(' and 
                       self.operators[token][0] <= self.operators[stack[-1]][0]):
                    output.append(stack.pop())
                stack.append(token)

        while stack:
            output.append(stack.pop())

        return output

    def evaluate_postfix(self, tokens: List[str]) -> float:
        """
        Evaluate postfix expression.
        
        Args:
            tokens (List[str]): List of tokens in postfix notation
            
        Returns:
            float: Result of the expression
            
        Raises:
            ValueError: If division by zero is attempted
            ValueError: If expression is invalid
        """
        stack = []

        for token in tokens:
            if token in self.operators:
                try:
                    b = float(stack.pop())
                    a = float(stack.pop())
                    if token == '/' and b == 0:
                        raise ValueError("Division by zero")
                    result = self.operators[token][1](a, b)
                    stack.append(str(result))
                except IndexError:
                    raise ValueError("Invalid expression")
            else:
                stack.append(token)

        if len(stack) != 1:
            raise ValueError("Invalid expression")
        return float(stack[0])

    def calculate(self, expression: str) -> float:
        """
        Evaluate an arithmetic expression.
        
        Args:
            expression (str): The arithmetic expression to evaluate
            
        Returns:
            float: Result of the expression
            
        Raises:
            ValueError: If the expression is invalid
        """
        try:
            # Tokenize and validate
            tokens = self.tokenize(expression)
            self.validate_parentheses(tokens)
            
            # Convert to postfix and evaluate
            postfix = self.to_postfix(tokens)
            result = self.evaluate_postfix(postfix)
            
            return result
            
        except Exception as e:
            raise ValueError(f"Invalid expression: {str(e)}")


def main():
    """Main function to demonstrate calculator usage."""
    calculator = Calculator()
    
    print("Arithmetic Calculator")
    print("Enter 'quit' to exit")
    print("Supported operations: +, -, *, / and parentheses")
    
    while True:
        try:
            expression = input("\nEnter expression: ")
            if expression.lower() == 'quit':
                break
                
            result = calculator.calculate(expression)
            print(f"Result: {result}")
            
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()


# Test cases
calculator = Calculator()
print(calculator.calculate("2 + 3 * 4"))  # 14.0
print(calculator.calculate("(2 + 3) * 4"))  # 20.0
print(calculator.calculate("2.5 * (3 + 4.5)"))  # 18.75
print(calculator.calculate("-2 * 3.5"))  # -7.0
