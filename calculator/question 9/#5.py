import re  # Used for efficient input string parsing

class Calculator:
    """
    A console-based arithmetic calculator that evaluates expressions with
    addition, subtraction, multiplication, division, and parentheses.

    This implementation uses the Shunting Yard algorithm to handle operator
    precedence and a stack-based approach for evaluation.  It avoids using
    `eval()` or similar functions for security and control.
    """

    def __init__(self):
        self.operators = {
            '+': (1, self._add),
            '-': (1, self._subtract),
            '*': (2, self._multiply),
            '/': (2, self._divide),
        }

    def _add(self, a, b):
        return a + b

    def _subtract(self, a, b):
        return a - b

    def _multiply(self, a, b):
        return a * b

    def _divide(self, a, b):
        if b == 0:
            raise ZeroDivisionError("Division by zero")
        return a / b

    def _tokenize(self, expression):
        """
        Tokenizes the input expression string into numbers, operators, and parentheses.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            list: A list of tokens (numbers, operators, parentheses).
            
        Raises:
            ValueError: if expression contains not allowed characters
        """
        # \s*   : matches zero or more whitespace characters.
        # (     : start of a capturing group.
        # [+\-*/()] : matches any single character within the set +,-,*,/,( or ).
        # )     : end of the capturing group.
        # \s*   : matches zero or more whitespace characters again.
        tokens = re.findall(r'\s*([+\-*/()]|\d+\.?\d*)\s*', expression)

        # Validate tokens
        for token in tokens:
            if token not in self.operators and token not in '()' and not re.match(r'^-?\d+\.?\d*$', token):
                raise ValueError(f"Invalid character or token: {token}")
        return tokens


    def _shunting_yard(self, tokens):
        """
        Converts the tokenized expression to Reverse Polish Notation (RPN)
        using the Shunting Yard algorithm.

        Args:
            tokens (list): A list of tokens from the input expression.

        Returns:
            list: A list of tokens in RPN order.
        """
        output_queue = []
        operator_stack = []

        for token in tokens:
            if token.replace('.', '', 1).lstrip('-').isdigit():  # Check if it's a number (including floats and negatives)
                output_queue.append(float(token))
            elif token in self.operators:
                precedence, _ = self.operators[token]
                while (operator_stack and operator_stack[-1] != '(' and
                       self.operators[operator_stack[-1]][0] >= precedence):
                    output_queue.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output_queue.append(operator_stack.pop())
                if not operator_stack:
                    raise ValueError("Unbalanced parentheses")  # Missing opening parenthesis
                operator_stack.pop()  # Remove the '('

        while operator_stack:
            if operator_stack[-1] == '(':
                raise ValueError("Unbalanced parentheses")  # Missing closing parenthesis
            output_queue.append(operator_stack.pop())

        return output_queue

    def _evaluate_rpn(self, rpn_tokens):
        """
        Evaluates an expression in Reverse Polish Notation (RPN).

        Args:
            rpn_tokens (list): A list of tokens in RPN order.

        Returns:
            float: The result of the evaluation.
        """
        value_stack = []
        for token in rpn_tokens:
            if isinstance(token, float):
                value_stack.append(token)
            elif token in self.operators:
                _, operation = self.operators[token]
                if len(value_stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands")
                operand2 = value_stack.pop()  # Pop in reverse order
                operand1 = value_stack.pop()
                result = operation(operand1, operand2)
                value_stack.append(result)

        if len(value_stack) != 1:
            raise ValueError("Invalid Expression: too many operands")
        return value_stack[0]

    def calculate(self, expression: str) -> float:
        """
        Evaluates the arithmetic expression.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the expression evaluation.

        Raises:
            ValueError: If the expression is invalid.
            ZeroDivisionError: If the expression attempts division by zero.
        """
        tokens = self._tokenize(expression)
        rpn_tokens = self._shunting_yard(tokens)
        result = self._evaluate_rpn(rpn_tokens)
        return result

def main():
    """
    Main function to run the calculator in a loop, accepting user input.
    """
    calculator = Calculator()
    while True:
        try:
            expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break
            result = calculator.calculate(expression)
            print("Result:", result)
        except (ValueError, ZeroDivisionError) as e:
            print("Error:", e)
        except Exception as e:
            print("An unexpected error occurred:", e)

if __name__ == "__main__":
    main()

