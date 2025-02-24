import re  # Used for tokenization

class Calculator:
    """
    A console-based arithmetic calculator that evaluates expressions using the
    Shunting Yard algorithm and Reverse Polish Notation (RPN).
    """

    def __init__(self):
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
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                        invalid characters, division by zero).
        """
        try:
            tokens = self._tokenize(expression)
            postfix = self._shunting_yard(tokens)
            result = self._evaluate_rpn(postfix)
            return result
        except ValueError as e:
            raise ValueError(f"Invalid expression: {e}")


    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the input expression.

        Args:
            expression: The expression string.

        Returns:
            A list of tokens (numbers, operators, parentheses).
        """
        # Regex to split the expression:  Find numbers (integers and decimals, including negative numbers),
        # operators, and parentheses.  The capturing groups are used correctly to include the operators
        # and parentheses in the resulting list.
        tokens = re.findall(r"(-?\d+\.?\d*|\+|\-|\*|\/|\(|\))", expression)

        # Check for invalid characters (anything that's not a number, operator, or parenthesis)
        for token in tokens:
            if not re.match(r"^-?\d+\.?\d*$|^[\+\-\*/()]$", token):
                raise ValueError(f"Invalid character: {token}")

        return tokens

    def _shunting_yard(self, tokens: list) -> list:
        """
        Converts the tokenized infix expression to postfix (RPN) using the Shunting Yard algorithm.

        Args:
            tokens: A list of tokens in infix notation.

        Returns:
            A list of tokens in postfix (RPN) notation.
        """
        output = []
        operator_stack = []

        for token in tokens:
            if re.match(r"^-?\d+\.?\d*$", token):  # If it's a number
                output.append(float(token))
            elif token in self.precedence:  # If it's an operator
                while (operator_stack and operator_stack[-1] != '(' and
                       self.precedence[operator_stack[-1]] >= self.precedence[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Unbalanced parentheses")
                operator_stack.pop()  # Pop the '('
            else:
                raise ValueError(f"Invalid token Shunting Yard: {token}")     
        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Unbalanced parentheses")
            output.append(operator_stack.pop())

        return output

    def _evaluate_rpn(self, postfix: list) -> float:
        """
        Evaluates a postfix (RPN) expression.

        Args:
            postfix: A list of tokens in postfix notation.

        Returns:
            The result of the expression.

        Raises:
            ValueError: If there's a division by zero or an invalid operator.
        """
        stack = []
        for token in postfix:
            if isinstance(token, float):  # Check if it's a number (already converted to float)
                stack.append(token)
            else:  # It's an operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression (not enough operands)")
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
                else:
                    raise ValueError(f"Invalid operator: {token}")

        if len(stack) != 1:
             raise ValueError("Invalid expression (too many operands)")
        return stack[0]


def main():
    """
    Main function to run the calculator.
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
        except Exception as ex:
            # General exception handler prevents unexpected crashes
            print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    main()


import unittest
# Assuming the calculator code is in a file named 'calculator.py'

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_tokenize(self):
        self.assertEqual(self.calculator._tokenize("2 + 3 * (4 - 1)"), ['2', '+', '3', '*', '(', '4', '-', '1', ')'])
        self.assertEqual(self.calculator._tokenize("-5.2 + 3"), ['-5.2', '+', '3'])
        with self.assertRaises(ValueError):
            self.calculator._tokenize("2 + x")  # Invalid character

    def test_shunting_yard(self):
        self.assertEqual(self.calculator._shunting_yard(['2', '+', '3', '*', '4']), [2.0, 3.0, 4.0, '*', '+'])
        self.assertEqual(self.calculator._shunting_yard(['(', '2', '+', '3', ')', '*', '4']), [2.0, 3.0, '+', 4.0, '*'])
        with self.assertRaises(ValueError):
            self.calculator._shunting_yard(['(', '2', '+', '3']) #Unbalanced

    def test_evaluate_rpn(self):
        self.assertEqual(self.calculator._evaluate_rpn([2.0, 3.0, '+']), 5.0)
        self.assertEqual(self.calculator._evaluate_rpn([2.0, 3.0, 4.0, '*', '+']), 14.0)
        with self.assertRaises(ValueError):
            self.calculator._evaluate_rpn([2.0, 0.0, '/'])  # Division by zero

    def test_calculate(self):
        self.assertEqual(self.calculator.calculate("2 + 3 * 4"), 14.0)
        self.assertEqual(self.calculator.calculate("(1 + 2) * (3 - 4) / 5"), -0.6)
        self.assertEqual(self.calculator.calculate("-5 + 3.2"), -1.8)
        with self.assertRaises(ValueError):
          self.calculator.calculate("4 ( 5 + 3)") #Invalid
        with self.assertRaises(ValueError):
          self.calculator.calculate("") #Empty
        with self.assertRaises(ValueError):
          self.calculator.calculate("2 / 0") #Divide by zero

if __name__ == '__main__':
    unittest.main()
