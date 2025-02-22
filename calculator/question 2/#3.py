
import re

class Calculator:
    """
    A simple arithmetic calculator that evaluates expressions without using eval().
    It supports addition, subtraction, multiplication, division, parentheses,
    and both integer and floating-point numbers.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression.

        Args:
            expression: The arithmetic expression string.

        Returns:
            The result of the expression as a float.

        Raises:
            ValueError: If the expression is invalid (e.g., unbalanced parentheses,
                        invalid characters, division by zero).
        """
        try:
            expression = self._preprocess(expression)
            tokens = self._tokenize(expression)
            postfix = self._infix_to_postfix(tokens)
            result = self._evaluate_postfix(postfix)
            return result
        except ValueError as e:
            raise ValueError(f"Invalid expression: {e}")
        except Exception as e:
             raise ValueError(f"Unexpected Error Occurred: {e}")


    def _preprocess(self, expression: str) -> str:
        """
        Preprocesses the expression string:
            - Removes whitespace.
            - Adds '*' between number and '(' and between ')' and number

        Args:
            expression: The input expression.
        Return:
          The preprocessed expression string.
        """
        expression = expression.replace(" ", "")
        expression = re.sub(r'(\d)([()])', r'\1*\2', expression)
        expression = re.sub(r'([()])(\d)', r'\1*\2', expression)
        return expression


    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the expression string.
        Args:
            expression: The expression string.
        Returns:
            A list of tokens.
        Raises:
            ValueError: If the expression is invalid (e.g., invalid characters).
        """

        # Use regular expression to allow both integers and floating-point numbers.
        # Also check for negative numbers (-(?![\d.]))?
        tokens = re.findall(r"(\d+\.\d+|\d+|[+\-*/()]|-(?![\d.]))", expression)

        # Input validation
        allowed_chars = r"[+\-*/().\d]"
        if not all(re.match(allowed_chars, char) for token in tokens for char in token):
            raise ValueError("Invalid characters in expression.")
        #check parenthesis validation
        self._validate_parentheses("".join(tokens))

        return tokens

    def _validate_parentheses(self, expression:str):
        """
        Validate if parenthesis are correct
        Args:
            expression: The expression string.
        Raises:
            ValueError: if the paranthesis are not correct
        """
        count = 0
        for char in expression:
            if char == '(':
                count += 1
            elif char == ')':
                count -= 1
            if count < 0:
                raise ValueError("Unbalanced parentheses.")
        if count != 0:
            raise ValueError("Unbalanced parentheses.")

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts an infix expression (list of tokens) to postfix notation (Reverse Polish Notation).
        Args:
            tokens: A list of tokens in infix notation.
        Returns:
              A list of tokens in postfix notation.
        """

        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []

        for token in tokens:
            if re.match(r"(\d+\.\d+|\d+)", token):  # Check if it is a number
                output.append(float(token))
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                operator_stack.pop()  # Remove the '('
            elif token in precedence:
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0)):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token.startswith("-") and (len(token) >1):
                output.append(float(token))
            elif token =='-': # if the operator is -
                #check if the element before is a operator or ( . I
                #If is true, the operator is a negative symbol instead minus
                if len(output) == 0 or (isinstance(output[-1],str) and output[-1] !=')'):
                    operator_stack.append(token)
                else:
                    while (operator_stack and operator_stack[-1] != '(' and
                       precedence.get(token, 0) <= precedence.get(operator_stack[-1], 0)):
                        output.append(operator_stack.pop())
                    operator_stack.append(token)
        while operator_stack:
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
          Evaluates a postfix expression.
          Args:
              tokens: A list of tokens in postfix notation..
          Returns:
              The result of the expression.
        Raises:
            ValueError: If the expression is invalid (e.g., division by zero)
        """
        stack = []

        for token in tokens:
            if isinstance(token,float):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Invalid expression: Insufficient operands for operator.")
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
                        raise ValueError("Division by zero.")
                    stack.append(operand1 / operand2)

        if len(stack) != 1:
             raise ValueError("Invalid expression: Too many operands.")
        return stack.pop()



def main():
    """Main function to run the calculator."""
    calculator = Calculator()
    while True:
        expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
        if expression.lower() == 'quit':
            break
        try:
            result = calculator.calculate(expression)
            print("Result:", result)
        except ValueError as e:
            print("Error:", e)

if __name__ == "__main__":
    main()
