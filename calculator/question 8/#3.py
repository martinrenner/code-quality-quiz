class Calculator:
    """A console-based arithmetic calculator that evaluates mathematical expressions.
    
    This calculator supports basic arithmetic operations (+, -, *, /),
    handles parentheses, and follows the correct order of operations.
    """
    
    def __init__(self):
        """Initialize the Calculator."""
        self.pos = 0
        self.expression = ""
    
    def calculate(self, expression: str) -> float:
        """Evaluate a mathematical expression and return the result.
        
        Args:
            expression (str): The mathematical expression to evaluate.
            
        Returns:
            float: The result of the evaluated expression.
            
        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                       invalid characters, division by zero).
        """
        # Clean input by removing spaces
        self.expression = expression.replace(" ", "")
        self.pos = 0
        
        # Check for invalid characters
        valid_chars = set("0123456789.+-*/()e")
        if not all(char in valid_chars for char in self.expression):
            raise ValueError("Invalid characters in expression")
        
        # Validate balanced parentheses
        if not self._check_balanced_parentheses():
            raise ValueError("Unbalanced parentheses in expression")
            
        # Parse and evaluate
        result = self._parse_expression()
        
        # Check if the entire expression was consumed
        if self.pos < len(self.expression):
            raise ValueError(f"Unexpected character at position {self.pos}: '{self.expression[self.pos]}'")
        
        return result
    
    def _check_balanced_parentheses(self) -> bool:
        """Check if parentheses in the expression are balanced.
        
        Returns:
            bool: True if parentheses are balanced, False otherwise.
        """
        stack = []
        for char in self.expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:  # No matching opening parenthesis
                    return False
                stack.pop()
        return len(stack) == 0  # Stack should be empty if all parentheses are balanced
    
    def _parse_expression(self) -> float:
        """Parse and evaluate an expression.
        
        Returns:
            float: The value of the expression.
        """
        return self._parse_addition_subtraction()
    
    def _parse_addition_subtraction(self) -> float:
        """Parse and evaluate addition and subtraction operations.
        
        Returns:
            float: The result of the addition/subtraction operations.
        """
        left = self._parse_multiplication_division()
        
        while self.pos < len(self.expression) and self.expression[self.pos] in ('+', '-'):
            op = self.expression[self.pos]
            self.pos += 1
            right = self._parse_multiplication_division()
            
            if op == '+':
                left += right
            else:  # op == '-'
                left -= right
                
        return left
    
    def _parse_multiplication_division(self) -> float:
        """Parse and evaluate multiplication and division operations.
        
        Returns:
            float: The result of the multiplication/division operations.
            
        Raises:
            ValueError: If division by zero is attempted.
        """
        left = self._parse_factor()
        
        while self.pos < len(self.expression) and self.expression[self.pos] in ('*', '/'):
            op = self.expression[self.pos]
            self.pos += 1
            right = self._parse_factor()
            
            if op == '*':
                left *= right
            else:  # op == '/'
                if right == 0:
                    raise ValueError("Division by zero")
                left /= right
                
        return left
    
    def _parse_factor(self) -> float:
        """Parse and evaluate a factor (number, parenthesized expression, or negative).
        
        Returns:
            float: The value of the factor.
            
        Raises:
            ValueError: If the input is invalid.
        """
        # Handle negative numbers
        if self.pos < len(self.expression) and self.expression[self.pos] == '-':
            self.pos += 1
            return -self._parse_factor()
            
        # Handle parentheses
        if self.pos < len(self.expression) and self.expression[self.pos] == '(':
            self.pos += 1  # Skip '('
            result = self._parse_expression()
            
            # Expect closing parenthesis
            if self.pos >= len(self.expression) or self.expression[self.pos] != ')':
                raise ValueError("Expected closing parenthesis")
                
            self.pos += 1  # Skip ')'
            return result
            
        # Parse a number
        return self._parse_number()
    
    def _parse_number(self) -> float:
        """Parse a number from the expression.
        
        Returns:
            float: The parsed number.
            
        Raises:
            ValueError: If no valid number is found.
        """
        start = self.pos
        
        # Check for digits before decimal point
        while (self.pos < len(self.expression) and 
               (self.expression[self.pos].isdigit() or self.expression[self.pos] == '.')):
            self.pos += 1
            
        if start == self.pos:
            raise ValueError(f"Expected number at position {start}")
            
        try:
            return float(self.expression[start:self.pos])
        except ValueError:
            raise ValueError(f"Invalid number format: {self.expression[start:self.pos]}")


def main():
    """Main function to run the calculator interactively."""
    calculator = Calculator()
    
    print("Console-based Arithmetic Calculator")
    print("Type 'exit' to quit")
    
    while True:
        user_input = input("\nEnter an expression: ")
        
        if user_input.lower() == 'exit':
            print("Exiting calculator. Goodbye!")
            break
            
        try:
            result = calculator.calculate(user_input)
            # Format the output to avoid unnecessary decimal places for whole numbers
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")
            
            
if __name__ == "__main__":
    main()
