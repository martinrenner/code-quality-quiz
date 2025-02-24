import re


class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations,
    parentheses, and floating-point numbers.  Adheres to ISO/IEC 25010
    quality characteristics.
    """

    def __init__(self):
        self.operators = {
            '+': (1, self._add),
            '-': (1, self._subtract),
            '*': (2, self._multiply),
            '/': (2, self._divide),
        }

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression.

        Args:
            expression (str): The expression to evaluate.

        Returns:
            float: The result of the evaluation.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced
                parentheses, invalid characters, division by zero).
        """
        try:
            normalized_expression = self._normalize_expression(expression)
            if not self._is_balanced(normalized_expression):
                raise ValueError("Unbalanced parentheses.")

            tokens = self._tokenize(normalized_expression)
            postfix_tokens = self._infix_to_postfix(tokens)
            result = self._evaluate_postfix(postfix_tokens)
            return result
        except ZeroDivisionError:
            raise ValueError("Division by zero error.")
        except ValueError as e:
            raise e  # Re-raise ValueErrors for consistent error handling
        except Exception as e:
             raise ValueError(f"An unexpected error occurred: {e}")


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
        allowed_chars = set("0123456789+-*/().")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression has properly paired parentheses.

        :param expression: A string containing the mathematical expression.
        :return: True if parentheses are correctly paired, otherwise False.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes a mathematical expression into a list of numbers and operators.

        Args:
            expression (str): The mathematical expression.

        Returns:
            list: A list of tokens.
        """
        return re.findall(r"(\b\d+\.?\d*\b|\+|\-|\*|\/|\(|\))", expression) #Handles floats and integers

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts an infix expression (represented as a list of tokens) to postfix notation.

        Args:
            tokens (list):  List of tokens in infix notation.

        Returns:
            list: List of tokens in postfix notation.
        """
        output = []
        operator_stack = []

        for token in tokens:
            if re.match(r"\b\d+\.?\d*\b", token):  # Check for numbers (integers and floats)
                output.append(float(token))  # Convert to float immediately
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses.")
                operator_stack.pop()  # Pop the '('
            elif token in self.operators:
                while (operator_stack and operator_stack[-1] != '(' and
                       self.operators[operator_stack[-1]][0] >= self.operators[token][0]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            else:
                raise ValueError(f"Invalid token: {token}") # Should never reach here due to earlier checks

        while operator_stack:
            if operator_stack[-1] == '(':  # Check for unmatched opening parenthesis
                raise ValueError("Mismatched parentheses")
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates a postfix expression.

        Args:
            tokens (list): The postfix expression as a list of tokens.

        Returns:
            float: The result of the evaluation.
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):  # Check if it's a number (already converted to float)
                stack.append(token)
            elif token in self.operators:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands.") #Handle error robustly
                operand2 = stack.pop()
                operand1 = stack.pop()
                operation = self.operators[token][1]
                result = operation(operand1, operand2)
                stack.append(result)
            else: # Should not be reached, due to earlier token/type checking
                raise ValueError(f"Invalid token in postfix expression: {token}")
        if len(stack) != 1:
            raise ValueError("Invalid expression: too many operands.")
        return stack.pop()

    def _add(self, x: float, y: float) -> float:
        """Adds two numbers."""
        return x + y

    def _subtract(self, x: float, y: float) -> float:
        """Subtracts two numbers."""
        return x - y

    def _multiply(self, x: float, y: float) -> float:
        """Multiplies two numbers."""
        return x * y

    def _divide(self, x: float, y: float) -> float:
        """Divides two numbers."""
        if y == 0:
            raise ZeroDivisionError("Division by zero.")
        return x / y



def main():
    """
    Main function to run the calculator.
    """
    calculator = Calculator()

    while True:
        try:
            expression = input("Enter a mathematical expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break
            result = calculator.calculate(expression)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:",e)

if __name__ == "__main__":
    main()
