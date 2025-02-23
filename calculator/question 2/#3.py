
import re  # Used for splitting the expression into tokens

class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations,
    parentheses, and floating-point numbers.  Adheres to ISO/IEC 25010
    quality characteristics.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression.

        :param expression: The mathematical expression as a string.
        :return: The result of the evaluation as a float.
        :raises ValueError: If the expression is invalid (e.g., unbalanced
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
            raise ValueError("Division by zero encountered.")
        except ValueError as e:  # Catch and re-raise ValueErrors for consistency
             raise e
        except Exception as e: # Catch any other exception
            raise ValueError(f"An unexpected error occurred: {e}")


    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes the expression by removing spaces and validating characters.

        :param expression: The input expression.
        :return: The normalized expression.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/().")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def _is_balanced(self, expression: str) -> bool:
        """
        Checks if the parentheses in the expression are balanced.

        :param expression: The expression string.
        :return: True if balanced, False otherwise.
        """
        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()
        return not stack  # True if the stack is empty (all parentheses matched)

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the expression into a list of numbers and operators.  Handles
        multi-digit numbers and floating-point numbers.

        :param expression: The normalized expression string.
        :return: A list of tokens.
        """
        # This regex splits the string by operators, keeping the operators as separate tokens.
        # It also handles floating-point numbers correctly.
        return re.findall(r"(\d+\.\d+|\d+|[+\-*/()])", expression)

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts an infix expression (represented as a list of tokens)
        to postfix notation (Reverse Polish Notation) using the Shunting Yard algorithm.

        :param tokens:  List of tokens in infix notation.
        :return: List of tokens in postfix notation.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []

        for token in tokens:
            if token.replace('.', '', 1).isdigit():  # Check if it's a number (integer or float)
                output.append(float(token))
            elif token in precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(operator_stack[-1], -1) >= precedence.get(token, -1)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Mismatched parentheses")  # Extra ')'
                operator_stack.pop()  # Remove the '('

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Mismatched parentheses")  # Extra '('
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates a postfix expression (represented as a list of tokens).

        :param tokens: List of tokens in postfix notation.
        :return: The result of the evaluation.
        :raises ValueError: If division by zero is attempted.
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            else:  # It's an operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression format.")
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
                        raise ValueError("Division by zero")  # Explicitly raise ValueError
                    stack.append(operand1 / operand2)
        if len(stack) != 1:
          raise ValueError("Invalid expression format.")
        return stack[0]



def main():
    """
    Main function to run the calculator in an interactive console session.
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

if __name__ == "__main__":
    main()
