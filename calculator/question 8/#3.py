
class Calculator:
    """
    A console-based arithmetic calculator that evaluates expressions
    according to the order of operations, supporting parentheses,
    and handling invalid inputs.
    """

    def __init__(self):
        """
        Initializes the calculator with operator precedence.
        """
        self.precedence = {
            '+': 1,
            '-': 1,
            '*': 2,
            '/': 2,
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.

        Args:
            expression: The arithmetic expression as a string.

        Returns:
            The result of the expression as a float.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced
                parentheses, invalid characters, division by zero).
        """
        try:
            postfix = self._infix_to_postfix(expression)
            result = self._evaluate_postfix(postfix)
            return result
        except Exception as e:
            raise ValueError(f"Invalid expression: {e}")

    def _infix_to_postfix(self, expression: str) -> list:
        """
        Converts an infix expression to postfix notation (RPN)
        using the Shunting Yard algorithm.

        Args:
            expression: The infix expression.

        Returns:
            A list representing the postfix expression.
        """
        output = []
        operator_stack = []
        i = 0
        while i < len(expression):
            char = expression[i]

            if char.isspace():  # Skip whitespace
                i += 1
                continue
            elif char.isdigit() or (char == '-' and (i == 0 or expression[i-1] in '(+-*/')): # Handle numbers (including negative)
                num_str, next_i = self._parse_number(expression, i)
                output.append(num_str)
                i = next_i
                continue # Important: continue to the next iteration
            
            
            elif char in self.precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       self.precedence.get(operator_stack[-1], -1) >= self.precedence.get(char, -1)):
                    output.append(operator_stack.pop())
                operator_stack.append(char)
            elif char == '(':
                operator_stack.append(char)
            elif char == ')':
                if '(' not in operator_stack:  #unmatched closing parenthesis
                    raise ValueError("Unbalanced parentheses")
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack: #unmatched closing parenthesis
                    raise ValueError("Unbalanced parentheses")

                operator_stack.pop()  # Pop the '('
            else:
                raise ValueError(f"Invalid character: {char}")
            i += 1

        while operator_stack:
            if operator_stack[-1] == '(': # Unmatched opening paranthesis
                raise ValueError("Unbalanced parentheses")
            output.append(operator_stack.pop())
        return output

    def _parse_number(self, expression: str, start_index: int) -> tuple[str, int]:
        """
        Parses a number (integer or decimal) from the expression string.

        Args:
            expression: The expression string.
            start_index: The index to start parsing from.

        Returns:
            A tuple containing the parsed number as a string and the next index.
        """
        end_index = start_index
        if expression[end_index] == '-': # Handle optional negative integer and decimals
            end_index +=1
        while end_index < len(expression) and (expression[end_index].isdigit() or expression[end_index] == '.'):
            end_index += 1
        
        num_str = expression[start_index:end_index]

        # Check for multiple decimal points.
        if num_str.count('.') > 1:
            raise ValueError(f'Invalid number format {num_str}')

        return num_str, end_index
    
    def _evaluate_postfix(self, postfix: list) -> float:
        """
        Evaluates a postfix expression.

        Args:
            postfix: The postfix expression as a list.

        Returns:
            The result of the expression.

        Raises:
            ValueError: If division by zero is attempted.
        """
        stack = []
        for token in postfix:
            if token.replace('.', '', 1).lstrip('-').isdigit():  # Check if it's a number
                stack.append(float(token))
            else:
                if len(stack) < 2:
                    raise ValueError("Not enough operands for operator")
                operand2 = stack.pop()
                operand1 = stack.pop()
                if token == '+':
                    stack.append(operand1 + operand2)
                elif token == '-':
                    stack.append(operand1 - operand2)
                elif token == '*':
                    stack.append(operand1 * operand2)
                elif token == '/':
                    if operand2 == 0:
                        raise ValueError("Division by zero")
                    stack.append(operand1 / operand2)
        if len(stack) != 1:
            raise ValueError("Invalid postfix expression")
        return stack.pop()


def main():
    """
    Main function to run the calculator in a loop.
    """
    calculator = Calculator()
    while True:
        try:
            expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    main()


import unittest

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition(self):
        self.assertEqual(self.calculator.calculate("2 + 3"), 5)

    def test_subtraction(self):
        self.assertEqual(self.calculator.calculate("5 - 2"), 3)

    def test_multiplication(self):
        self.assertEqual(self.calculator.calculate("4 * 6"), 24)

    def test_division(self):
        self.assertEqual(self.calculator.calculate("10 / 2"), 5)

    def test_parentheses(self):
        self.assertEqual(self.calculator.calculate("(2 + 3) * 4"), 20)
        self.assertEqual(self.calculator.calculate("2 + (3 * 4)"), 14)
        self.assertEqual(self.calculator.calculate("((2+2)-1)/3"), 1)

    def test_order_of_operations(self):
        self.assertEqual(self.calculator.calculate("2 + 3 * 4"), 14)
        self.assertEqual(self.calculator.calculate("10 / 2 - 1"), 4)

    def test_decimal_numbers(self):
        self.assertEqual(self.calculator.calculate("2.5 + 3.5"), 6)
        self.assertEqual(self.calculator.calculate("5 / 2.5"), 2)
        self.assertEqual(self.calculator.calculate("1.2 + 3.4 * 5.6"), 20.24)

    def test_negative_numbers(self):
        self.assertEqual(self.calculator.calculate("-2 + 3"), 1)
        self.assertEqual(self.calculator.calculate("5 - -2"), 7)
        self.assertEqual(self.calculator.calculate("-4 * 6"), -24)
        self.assertEqual(self.calculator.calculate("10 / -2"), -5)
        self.assertEqual(self.calculator.calculate("-(2+3)"),-5)
        self.assertEqual(self.calculator.calculate("-2*-3"), 6)
        self.assertEqual(self.calculator.calculate("-2 * -3"), 6)
        self.assertEqual(self.calculator.calculate("(-2) * (-3)"), 6)
        self.assertEqual(self.calculator.calculate("-1*(2+3*(-4-5))"), 29)
    
    def test_whitespace(self):
        self.assertEqual(self.calculator.calculate(" 2 +  3 "), 5)
        self.assertEqual(self.calculator.calculate(" ( 2 + 3 ) * 4 "), 20)
    
    def test_division_by_zero(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate("5 / 0")
        self.assertIn("Division by zero", str(context.exception))
        with self.assertRaises(ValueError):
            self.calculator.calculate("5 / (2-2)")

    def test_unbalanced_parentheses(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate("(2 + 3")
        self.assertIn("Unbalanced parentheses", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.calculator.calculate("2 + 3)")
        self.assertIn("Unbalanced parentheses", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.calculator.calculate("((2+3)*4")
        self.assertIn("Unbalanced parentheses", str(context.exception))

    def test_invalid_characters(self):
        with self.assertRaises(ValueError) as context:
            self.calculator.calculate("2 + a")
        self.assertIn("Invalid character", str(context.exception))

        with self.assertRaises(ValueError) as context:
            self.calculator.calculate("2 $ 3")
        self.assertIn("Invalid character", str(context.exception))
     
    def test_invalid_number_format(self):
         with self.assertRaises(ValueError) as context:
              self.calculator.calculate("2.5.5 + 3")
         self.assertTrue("Invalid number format" in str(context.exception))
    
    def test_invalid_postfix(self):
       with self.assertRaises(ValueError) :
           self.calculator._evaluate_postfix(['2','+'])
    
    def test_complex_expressions(self):
        self.assertEqual(self.calculator.calculate("2 + 3 * (4 - 1) / 3 + (-2)"), 3)
        self.assertEqual(self.calculator.calculate("10 - (5 * (2 + 1) - 7) / 2"), 6)
       
if __name__ == '__main__':
    unittest.main()
