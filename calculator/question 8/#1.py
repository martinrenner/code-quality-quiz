class Calculator:
    """
    A calculator class that evaluates arithmetic expressions following proper
    precedence rules and supporting parentheses.
    
    Implements ISO/IEC 25010 quality standards for correctness, performance,
    modularity, security, and maintainability.
    """
    
    def __init__(self):
        """Initialize the calculator with operator precedence rules."""
        # Define operator precedence (higher number means higher precedence)
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2
        }
        
    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression string and returns the result.
        
        Args:
            expression (str): A string representing a mathematical expression
                              (e.g., "2 + 3 * (4 - 1)")
        
        Returns:
            float: The result of the evaluated expression
            
        Raises:
            ValueError: If the expression is invalid (unbalanced parentheses,
                        invalid characters, division by zero)
        """
        try:
            # Remove all whitespace from the expression
            expression = expression.replace(" ", "")
            
            if not expression:
                raise ValueError("Expression cannot be empty")
                
            # Tokenize the expression
            tokens = self._tokenize(expression)
            
            # Convert to postfix notation and evaluate
            result = self._evaluate_postfix(self._infix_to_postfix(tokens))
            
            return result
        except Exception as e:
            # Re-raise calculator-specific exceptions
            if isinstance(e, ValueError):
                raise
            # Wrap any other exceptions as ValueError with a helpful message
            raise ValueError(f"Invalid expression: {str(e)}")
            
    def _tokenize(self, expression: str) -> list:
        """
        Convert an expression string into a list of tokens.
        
        Args:
            expression (str): The expression to tokenize
            
        Returns:
            list: A list of tokens (numbers and operators)
            
        Raises:
            ValueError: If the expression contains invalid characters
        """
        tokens = []
        i = 0
        
        while i < len(expression):
            char = expression[i]
            
            # Handle operators and parentheses
            if char in "+-*/()":
                tokens.append(char)
                i += 1
            # Handle numbers (including decimals and negative signs)
            elif char.isdigit() or (char == '.' and i + 1 < len(expression) and expression[i + 1].isdigit()):
                # Extract the full number
                number = char
                i += 1
                while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    number += expression[i]
                    i += 1
                # Convert string to float or int
                if '.' in number:
                    tokens.append(float(number))
                else:
                    tokens.append(int(number))
            # Handle negative numbers
            elif char == '-' and (i == 0 or expression[i-1] in '(+-*/'):
                # Look ahead to determine if this is a negative number
                number = char
                i += 1
                if i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                    while i < len(expression) and (expression[i].isdigit() or expression[i] == '.'):
                        number += expression[i]
                        i += 1
                    # Convert string to float or int
                    if '.' in number:
                        tokens.append(float(number))
                    else:
                        tokens.append(int(number))
                else:
                    # It's a standalone minus operator
                    tokens.append('-')
            else:
                raise ValueError(f"Invalid character in expression: '{char}'")
                
        return tokens
    
    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Convert an infix expression to postfix notation using the
        Shunting Yard algorithm.
        
        Args:
            tokens (list): List of tokens in infix notation
            
        Returns:
            list: List of tokens in postfix notation
            
        Raises:
            ValueError: If the expression has unbalanced parentheses
        """
        output = []
        operator_stack = []
        
        for token in tokens:
            # If token is a number, add to output
            if isinstance(token, (int, float)):
                output.append(token)
            # If token is an operator
            elif token in self.precedence:
                # Pop operators with higher precedence from the stack to output
                while (operator_stack and operator_stack[-1] != '(' and 
                       operator_stack[-1] in self.precedence and
                       self.precedence[operator_stack[-1]] >= self.precedence[token]):
                    output.append(operator_stack.pop())
                # Push the current operator to the stack
                operator_stack.append(token)
            # If token is an opening parenthesis, push to stack
            elif token == '(':
                operator_stack.append(token)
            # If token is a closing parenthesis
            elif token == ')':
                # Pop operators from stack to output until opening parenthesis is found
                while operator_stack and operator_stack[-1] != '(':
                    if not operator_stack:  # Stack is empty
                        raise ValueError("Mismatched parentheses: too many closing parentheses")
                    output.append(operator_stack.pop())
                
                # If we reach here, we should have an opening parenthesis on top of the stack
                if not operator_stack or operator_stack[-1] != '(':
                    raise ValueError("Mismatched parentheses: too many closing parentheses")
                
                # Remove the opening parenthesis
                operator_stack.pop()
        
        # Pop any remaining operators from the stack to the output
        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses: too many opening parentheses")
            output.append(operator_stack.pop())
        
        return output
    
    def _evaluate_postfix(self, postfix: list) -> float:
        """
        Evaluate a postfix expression.
        
        Args:
            postfix (list): List of tokens in postfix notation
            
        Returns:
            float: Result of the evaluation
            
        Raises:
            ValueError: If division by zero is attempted or the expression is invalid
        """
        if not postfix:
            raise ValueError("Empty expression")
            
        operand_stack = []
        
        for token in postfix:
            # If token is a number, push to stack
            if isinstance(token, (int, float)):
                operand_stack.append(token)
            # If token is an operator, pop operands, apply operator, push result
            elif token in self.precedence:
                if len(operand_stack) < 2:
                    raise ValueError("Invalid expression: not enough operands")
                
                # Pop operands (in reverse order)
                b = operand_stack.pop()
                a = operand_stack.pop()
                
                # Apply operator
                if token == '+':
                    operand_stack.append(a + b)
                elif token == '-':
                    operand_stack.append(a - b)
                elif token == '*':
                    operand_stack.append(a * b)
                elif token == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    operand_stack.append(a / b)
        
        # The final result should be the only item left on the stack
        if len(operand_stack) != 1:
            raise ValueError("Invalid expression: too many operands")
            
        return operand_stack[0]


def main():
    """
    Main function to run the calculator as a command-line application.
    Provides a simple console interface for the calculator.
    """
    calculator = Calculator()
    print("Console Calculator (enter 'exit' to quit)")
    print("Supported operations: +, -, *, / and parentheses")
    
    while True:
        try:
            expression = input("\nEnter an expression: ")
            
            if expression.lower() == 'exit':
                print("Exiting calculator. Goodbye!")
                break
                
            result = calculator.calculate(expression)
            
            # Format the result (avoid trailing zeros for whole numbers)
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
                
        except ValueError as e:
            print(f"Error: {str(e)}")
        except Exception as e:
            print(f"Unexpected error: {str(e)}")


if __name__ == "__main__":
    main()
