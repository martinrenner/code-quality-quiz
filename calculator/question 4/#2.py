class Calculator:
    """
    A console-based arithmetic calculator that evaluates mathematical expressions.
    
    This calculator supports:
    - Basic operations: addition, subtraction, multiplication, division
    - Parentheses for grouping expressions
    - Proper order of operations (PEMDAS)
    - Decimal and negative numbers
    - Error detection for invalid inputs
    """
    
    def __init__(self):
        """Initialize the Calculator object."""
        self.position = 0
        self.expression = ""
    
    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.
        
        Args:
            expression (str): A string containing a mathematical expression.
                Supports +, -, *, /, parentheses, integers, and decimals.
                
        Returns:
            float: The result of the evaluated expression.
            
        Raises:
            ValueError: If the expression contains syntax errors or invalid operations.
            ZeroDivisionError: If the expression involves division by zero.
        """
        # Reset state
        self.position = 0
        
        # Normalize and validate expression
        self.expression = self._normalize_expression(expression)
        
        # Check for balanced parentheses
        if not self._is_balanced_parentheses(self.expression):
            raise ValueError("Unbalanced parentheses in the expression.")
        
        # Parse and evaluate the expression
        result = self._parse_expression()
        
        # Check if the entire expression was consumed
        if self.position < len(self.expression):
            raise ValueError(f"Unexpected character '{self.expression[self.position]}' at position {self.position}")
        
        return result
    
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
        # Remove spaces
        normalized = expression.replace(" ", "")
        
        # Validate characters
        allowed_chars = set("0123456789+-*/().eE")
        if not all(char in allowed_chars for char in normalized):
            invalid_chars = [char for char in normalized if char not in allowed_chars]
            raise ValueError(f"Expression contains invalid characters: {invalid_chars}")
        
        # Basic initial structure validation
        if not normalized:
            raise ValueError("Empty expression.")
        
        return normalized
    
    def _is_balanced_parentheses(self, expression: str) -> bool:
        """
        Checks whether parentheses in the expression are properly balanced.
        
        Args:
            expression (str): A string containing a mathematical expression.
            
        Returns:
            bool: True if parentheses are balanced, False otherwise.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return len(stack) == 0
    
    def _parse_expression(self) -> float:
        """
        Parses and evaluates an expression.
        
        Returns:
            float: The result of the evaluated expression.
            
        Raises:
            ValueError: If the expression contains syntax errors.
        """
        return self._parse_addition_subtraction()
    
    def _parse_addition_subtraction(self) -> float:
        """
        Parses and evaluates addition and subtraction operations.
        
        Returns:
            float: The result of the evaluated expression.
        """
        left = self._parse_multiplication_division()
        
        while self.position < len(self.expression):
            operator = self.expression[self.position]
            
            if operator not in ['+', '-']:
                break
                
            self.position += 1
            right = self._parse_multiplication_division()
            
            if operator == '+':
                left += right
            else:  # operator == '-'
                left -= right
                
        return left
    
    def _parse_multiplication_division(self) -> float:
        """
        Parses and evaluates multiplication and division operations.
        
        Returns:
            float: The result of the evaluated expression.
            
        Raises:
            ZeroDivisionError: If division by zero is attempted.
        """
        left = self._parse_number_or_parenthesis()
        
        while self.position < len(self.expression):
            operator = self.expression[self.position]
            
            if operator not in ['*', '/']:
                break
                
            self.position += 1
            right = self._parse_number_or_parenthesis()
            
            if operator == '*':
                left *= right
            else:  # operator == '/'
                if right == 0:
                    raise ZeroDivisionError("Division by zero is not allowed.")
                left /= right
                
        return left
    
    def _parse_number_or_parenthesis(self) -> float:
        """
        Parses a number or a parenthesized expression.
        
        Returns:
            float: The parsed number or the result of the parenthesized expression.
            
        Raises:
            ValueError: If the syntax is invalid.
        """
        # Check for parenthesis
        if self.position < len(self.expression) and self.expression[self.position] == '(':
            self.position += 1  # Skip the opening parenthesis
            result = self._parse_expression()
            
            # Ensure closing parenthesis
            if self.position >= len(self.expression) or self.expression[self.position] != ')':
                raise ValueError("Missing closing parenthesis.")
                
            self.position += 1  # Skip the closing parenthesis
            return result
        
        # Handle unary plus/minus
        if self.position < len(self.expression) and self.expression[self.position] in ['+', '-']:
            sign = -1 if self.expression[self.position] == '-' else 1
            self.position += 1
            return sign * self._parse_number_or_parenthesis()
        
        # Parse a number
        return self._parse_number()
    
    def _parse_number(self) -> float:
        """
        Parses a numeric value from the current position in the expression.
        
        Returns:
            float: The parsed numeric value.
            
        Raises:
            ValueError: If a valid number cannot be parsed.
        """
        start_pos = self.position
        
        # Check if we're at the end of the expression
        if start_pos >= len(self.expression):
            raise ValueError("Expected a number but reached end of expression.")
        
        # Check if the character at the current position is a digit or decimal point
        if not (self.expression[start_pos].isdigit() or self.expression[start_pos] == '.'):
            raise ValueError(f"Expected a number at position {start_pos}, found '{self.expression[start_pos]}'")
        
        # Scan to find the end of the number
        while (self.position < len(self.expression) and 
               (self.expression[self.position].isdigit() or 
                self.expression[self.position] == '.' or 
                self.expression[self.position] in ['e', 'E'])):
            
            # Handle scientific notation correctly
            if self.expression[self.position] in ['e', 'E']:
                self.position += 1
                # Check for potential +/- after E
                if (self.position < len(self.expression) and 
                    self.expression[self.position] in ['+', '-']):
                    self.position += 1
            else:
                self.position += 1
        
        # Extract the number string
        number_str = self.expression[start_pos:self.position]
        
        try:
            # Convert to float
            return float(number_str)
        except ValueError:
            raise ValueError(f"Invalid number format: {number_str}")


def main():
    """
    Main function to run the calculator in console mode.
    Handles user input and displays results.
    """
    calculator = Calculator()
    print("Console Calculator - Type 'exit' to quit")
    
    while True:
        try:
            expression = input("Enter expression: ")
            if expression.lower() == 'exit':
                break
                
            result = calculator.calculate(expression)
            
            # Format output: keep as integer if it's a whole number
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
                
        except (ValueError, ZeroDivisionError) as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
