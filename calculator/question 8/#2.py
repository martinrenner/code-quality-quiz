class Calculator:
    """
    A calculator that evaluates arithmetic expressions following standard order of operations.
    
    This calculator supports:
    - Basic operations: addition, subtraction, multiplication, division
    - Parentheses for grouping
    - Decimal and negative numbers
    
    It follows the PEMDAS order of operations and includes comprehensive validation.
    """
    
    def calculate(self, expression: str) -> float:
        """
        Evaluates a given arithmetic expression and returns the result.
        
        Args:
            expression (str): The arithmetic expression to evaluate (e.g., "2 + 3 * (4 - 1)")
            
        Returns:
            float: The result of evaluating the expression
            
        Raises:
            ValueError: If the expression has invalid syntax, unbalanced parentheses,
                       invalid characters, or attempts division by zero
        """
        # Validate and normalize the input expression
        normalized_exp = self._normalize_expression(expression)
        # Parse and evaluate the expression
        return self._evaluate(normalized_exp)
    
    def _normalize_expression(self, expression: str) -> str:
        """
        Validates and normalizes an arithmetic expression.
        
        Args:
            expression (str): The raw arithmetic expression
            
        Returns:
            str: The normalized expression with spaces removed
            
        Raises:
            ValueError: If the expression contains invalid characters or has unbalanced parentheses
        """
        if not expression:
            raise ValueError("Expression cannot be empty")
            
        # Check for invalid characters
        allowed_chars = set("0123456789+-*/().^ ")
        if not all(char in allowed_chars for char in expression):
            invalid_chars = ''.join(set(char for char in expression if char not in allowed_chars))
            raise ValueError(f"Expression contains invalid characters: {invalid_chars}")
        
        # Check for balanced parentheses
        if not self._is_balanced(expression):
            raise ValueError("Expression has unbalanced parentheses")
            
        return expression.replace(" ", "")
    
    def _is_balanced(self, expression: str) -> bool:
        """
        Checks if the parentheses in an expression are properly balanced.
        
        Args:
            expression (str): The arithmetic expression
            
        Returns:
            bool: True if parentheses are balanced, False otherwise
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
    
    def _evaluate(self, expression: str) -> float:
        """
        Evaluates a normalized arithmetic expression.
        
        Args:
            expression (str): The normalized arithmetic expression
            
        Returns:
            float: The result of evaluating the expression
            
        Raises:
            ValueError: If division by zero is attempted or the expression is invalid
        """
        # Recursive descent parser to handle order of operations
        return self._parse_addition_subtraction(expression, 0)[0]
    
    def _parse_addition_subtraction(self, expression: str, index: int) -> tuple[float, int]:
        """
        Parses terms connected by addition and subtraction.
        
        Args:
            expression (str): The arithmetic expression
            index (int): The current position in the expression
            
        Returns:
            tuple[float, int]: The result value and the new index in the expression
            
        Raises:
            ValueError: If the expression has invalid syntax or operations
        """
        # Parse the first term
        value, index = self._parse_multiplication_division(expression, index)
        
        # Continue parsing if there are more terms
        while index < len(expression):
            if expression[index] == '+':
                # Addition
                right_value, index = self._parse_multiplication_division(expression, index + 1)
                value += right_value
            elif expression[index] == '-':
                # Subtraction
                right_value, index = self._parse_multiplication_division(expression, index + 1)
                value -= right_value
            else:
                # Not an addition or subtraction operator, exit the loop
                break
        
        return value, index
    
    def _parse_multiplication_division(self, expression: str, index: int) -> tuple[float, int]:
        """
        Parses factors connected by multiplication and division.
        
        Args:
            expression (str): The arithmetic expression
            index (int): The current position in the expression
            
        Returns:
            tuple[float, int]: The result value and the new index in the expression
            
        Raises:
            ValueError: If division by zero is attempted or expression is invalid
        """
        # Parse the first factor
        value, index = self._parse_factor(expression, index)
        
        # Continue parsing if there are more factors
        while index < len(expression):
            if expression[index] == '*':
                # Multiplication
                right_value, index = self._parse_factor(expression, index + 1)
                value *= right_value
            elif expression[index] == '/':
                # Division (check for division by zero)
                right_value, index = self._parse_factor(expression, index + 1)
                if right_value == 0:
                    raise ValueError("Division by zero is not allowed")
                value /= right_value
            else:
                # Not a multiplication or division operator, exit the loop
                break
        
        return value, index
    
    def _parse_factor(self, expression: str, index: int) -> tuple[float, int]:
        """
        Parses a factor: number, parenthesized expression, or negative value.
        
        Args:
            expression (str): The arithmetic expression
            index (int): The current position in the expression
            
        Returns:
            tuple[float, int]: The factor value and the new index in the expression
            
        Raises:
            ValueError: If the expression has invalid syntax
        """
        if index >= len(expression):
            raise ValueError("Unexpected end of expression")
        
        # Handle negative numbers
        if expression[index] == '-':
            value, index = self._parse_factor(expression, index + 1)
            return -value, index
            
        # Handle parenthesized expressions
        if expression[index] == '(':
            # Evaluate the expression inside the parentheses
            value, index = self._parse_addition_subtraction(expression, index + 1)
            
            # Check for closing parenthesis
            if index >= len(expression) or expression[index] != ')':
                raise ValueError("Missing closing parenthesis")
            
            return value, index + 1
        
        # Handle numbers (both integers and floating-point)
        if expression[index].isdigit() or expression[index] == '.':
            start_index = index
            # Parse the digits
            has_decimal = False
            while (index < len(expression) and 
                   (expression[index].isdigit() or 
                    (expression[index] == '.' and not has_decimal))):
                if expression[index] == '.':
                    has_decimal = True
                index += 1
            
            # Convert the substring to a number
            try:
                value = float(expression[start_index:index])
                return value, index
            except ValueError:
                raise ValueError(f"Invalid number format: {expression[start_index:index]}")
        
        # If we get here, the expression is invalid
        raise ValueError(f"Unexpected character at position {index}: {expression[index]}")


def main():
    """
    Main function to interact with the calculator via console.
    
    Provides an interactive console interface for the calculator, allowing
    users to input expressions and see results until they choose to exit.
    """
    calculator = Calculator()
    
    print("Console Calculator")
    print("Enter an arithmetic expression to calculate (or 'exit' to quit)")
    print("Examples: 2+3*4, (2.5+3.5)/2, 10-5*2")
    
    while True:
        user_input = input("\nEnter expression: ").strip()
        
        if user_input.lower() in ('exit', 'quit'):
            print("Goodbye!")
            break
            
        if not user_input:
            continue
            
        try:
            result = calculator.calculate(user_input)
            
            # For clean integer results, display without decimal places
            if result == int(result):
                print(f"Result: {int(result)}")
            else:
                print(f"Result: {result}")
                
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")


if __name__ == "__main__":
    main()
