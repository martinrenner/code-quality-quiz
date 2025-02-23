
import re  # Used for more robust input splitting

class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction,
    multiplication, division, and parentheses.  It handles operator precedence,
    floating-point numbers, and input validation.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates an arithmetic expression.

        Args:
            expression: The arithmetic expression as a string.

        Returns:
            The result of the evaluation as a float.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                        invalid characters, division by zero).
        """
        try:
            tokens = self._tokenize(expression)
            parsed_expression = self._parse(tokens)
            result = self._evaluate(parsed_expression)
            return result
        except ValueError as e:
            raise ValueError(f"Invalid expression: {e}")


    def _tokenize(self, expression: str) -> list[str]:
        """
        Tokenizes the input expression into a list of numbers, operators, and parentheses.

        Args:
            expression: The arithmetic expression.

        Returns:
           A list of tokens.

        Raises:
            ValueError:  If the expression contains invalid characters.
        """
        # Use regular expressions for more robust tokenization.  This handles
        # whitespace, negative numbers gracefully, and catches invalid characters.
        tokens = re.findall(r"(\d+\.?\d*|\.\d+|[-+*/()]|\s+)", expression)
        tokens = [t for t in tokens if not t.isspace()]  # Remove whitespace

        # Check for invalid characters (anything not a digit, operator, ., or parenthesis).
        for token in tokens:
            if not re.match(r"^\d+\.?\d*$|^\.\d+$|^[-+*/()]$", token):
                raise ValueError(f"Invalid character: {token}")
        return tokens

    def _parse(self, tokens: list[str]) -> list:
         """
         Parses tokens into Reverse Polish Notation (RPN) using the Shunting Yard algorithm.
         This handles operator precedence and parentheses.

         Args:
             tokens: A list of tokens from the _tokenize method.

         Returns:
             A list representing the expression in RPN.

        Raises:
            ValueError: If parentheses are unbalanced.
         """
         output_queue = []
         operator_stack = []
         precedence = {'+': 1, '-': 1, '*': 2, '/': 2}

         for token in tokens:
             if re.match(r"^\d+\.?\d*$|^\.\d+$", token):  # Is it a number?
                 output_queue.append(float(token))
             elif token in precedence:  # Is it an operator?
                 while (operator_stack and operator_stack[-1] != '(' and
                        precedence.get(operator_stack[-1], -1) >= precedence.get(token, -1)):
                     output_queue.append(operator_stack.pop())
                 operator_stack.append(token)
             elif token == '(':
                 operator_stack.append(token)
             elif token == ')':
                 while operator_stack and operator_stack[-1] != '(':
                     output_queue.append(operator_stack.pop())
                 if not operator_stack:
                     raise ValueError("Unbalanced parentheses")
                 operator_stack.pop()  # Remove the '('

         while operator_stack:
             if operator_stack[-1] == '(':  # Check for leftover '('
                 raise ValueError("Unbalanced parentheses")
             output_queue.append(operator_stack.pop())

         return output_queue

    def _evaluate(self, rpn_expression: list) -> float:
        """
        Evaluates an expression in Reverse Polish Notation (RPN).

        Args:
            rpn_expression: A list representing the expression in RPN.

        Returns:
            The result of the evaluation.

        Raises:
            ValueError: If division by zero occurs or if the expression is invalid.
        """
        stack = []
        for token in rpn_expression:
            if isinstance(token, float):
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
        if len(stack) != 1:
            raise ValueError("Invalid expression (too many operands)")
        return stack[0]
def main():
    """
    Main function to run the calculator in a console loop.
    """
    calculator = Calculator()
    while True:
        expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        try:
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

