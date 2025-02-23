
import re  # Used for tokenization

class Calculator:
    """
    A console-based arithmetic calculator that supports basic operations,
    parentheses, and error handling.
    """

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression.

        :param expression: The mathematical expression as a string.
        :return: The result of the expression as a float.
        :raises ValueError: If the expression is invalid.
        """
        try:
            normalized_expression = self._normalize_expression(expression)
            if not self._is_balanced(normalized_expression):
                raise ValueError("Unbalanced parentheses.")

            tokens = self._tokenize(normalized_expression)
            postfix_tokens = self._shunting_yard(tokens)
            result = self._evaluate_postfix(postfix_tokens)
            return result
        except ZeroDivisionError:
            raise ValueError("Division by zero.")
        except ValueError as e:
            raise ValueError(f"Invalid expression: {e}")


    def _normalize_expression(self, expression: str) -> str:
        """
        Normalizes a mathematical expression by removing spaces and validating characters.
        Also handles implicit multiplication before parentheses (e.g., 2(3+4) -> 2*(3+4)).

        :param expression: A mathematical expression as a string.
        :return: The normalized expression without spaces.
        :raises ValueError: If the expression contains invalid characters.
        """
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        normalized = expression.replace(" ", "")
        
        # Handle implicit multiplication: Add '*' where needed.
        normalized = re.sub(r'(\d)\(', r'\1*(', normalized)  # 2(3+4) -> 2*(3+4)
        normalized = re.sub(r'\)(\d)', r')*\1', normalized)   # (3+4)2 -> (3+4)*2
        normalized = re.sub(r'\)\(', r')*(', normalized)     # (3+4)(1+2) -> (3+4)*(1+2)
          
        return normalized
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
        Tokenizes a mathematical expression.

        :param expression: The normalized mathematical expression.
        :return: A list of tokens (numbers, operators, parentheses).
        """
        # Use regular expression to handle numbers (including decimals and negatives),
        # operators, and parentheses.
        return re.findall(r"[-+]?\d*\.?\d+|[-+*/()]", expression)

    def _shunting_yard(self, tokens: list) -> list:
        """
        Converts an infix expression (represented as a list of tokens) to postfix notation.

        :param tokens: A list of tokens representing the infix expression.
        :return: A list of tokens representing the postfix expression.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
        output = []
        operator_stack = []

        for token in tokens:
            if re.match(r"[-+]?\d*\.?\d+", token):  # If it's a number
                output.append(float(token))
            elif token in precedence:  # If it's an operator
                while (operator_stack and operator_stack[-1] != '(' and
                       precedence[operator_stack[-1]] >= precedence[token]):
                    output.append(operator_stack.pop())
                operator_stack.append(token)
            elif token == '(':
                operator_stack.append(token)
            elif token == ')':
                while operator_stack and operator_stack[-1] != '(':
                    output.append(operator_stack.pop())
                if not operator_stack: # Check for mismatched parentheses
                    raise ValueError("Mismatched parentheses")
                operator_stack.pop()  # Pop the '('

        while operator_stack:
            if operator_stack[-1] == '(':   # Check for mismatched parentheses
                raise ValueError("Mismatched parentheses")
            output.append(operator_stack.pop())

        return output

    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates a postfix expression.

        :param tokens: A list of tokens representing the postfix expression.
        :return: The result of the expression.
        """
        stack = []
        for token in tokens:
            if isinstance(token, float):
                stack.append(token)
            else:  # It's an operator
                if len(stack) < 2:
                    raise ValueError("Invalid expression: insufficient operands for operator.")
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
                        raise ZeroDivisionError("Division by zero.")
                    stack.append(operand1 / operand2)
        if len(stack) != 1:
            raise ValueError("Invalid Expression: too many operands")
        return stack[0]


calculator = Calculator()

# Valid expressions
print(calculator.calculate("2 + 3 * 4"))  # Output: 14.0
print(calculator.calculate("(2 + 3) * 4"))  # Output: 20.0
print(calculator.calculate("-5 + 2 * (10 - 4) / 3"))  # Output: -1.0
print(calculator.calculate("10 / 2"))     # Output: 5.0
print(calculator.calculate("2*(3+4)"))   #Output = 14.0
print(calculator.calculate("(3+4)2"))   #Output = 14.0
print(calculator.calculate("(3+4)(1+2)"))   #Output = 21.0
print(calculator.calculate("2.5 * 4"))  # Output: 10.0
print(calculator.calculate("-1.5 * -4")) # Output 6.0
# Invalid expressions (these will raise ValueErrors)
try:
    print(calculator.calculate("2 + (3 * 4"))  # Unbalanced parentheses
except ValueError as e:
    print(e)

try:
    print(calculator.calculate("10 / 0"))  # Division by zero
except ValueError as e:
    print(e)

try:
    print(calculator.calculate("2 + a * 4"))  # Invalid character
except ValueError as e:
    print(e)

try:
    print(calculator.calculate("5 -"))
except ValueError as e:
    print(e)  # Invalid expression: Insufficient operands

try:
    print(calculator.calculate("5 5"))
except ValueError as e:
    print(e) # Invalid expression: too many operands
