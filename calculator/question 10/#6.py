class Calculator:
    """
    A console-based arithmetic calculator that supports addition, subtraction,
    multiplication, and division with correct operator precedence and parentheses.

    Attributes:
        None
    """

    def __init__(self):
        """
        Initialize the Calculator object.

        Attributes:
            None
        """
        self.operators = {'+', '-', '*', '/'}

    def calculate(self, expression: str) -> float:
        """
        Evaluates a mathematical expression and returns the result.

        Args:
            expression (str): A string containing the mathematical expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression is invalid or contains division by zero.
        """
        # Normalize and validate the input expression
        normalized_expr = self._normalize_expression(expression)
        if not self._is_valid_expression(normalized_expr):
            raise ValueError("Invalid expression")

        # Tokenize the expression
        tokens = self._tokenize(normalized_expr)

        # Evaluate the expression
        result, _ = self._evaluate_expression(tokens)

        return result

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
        allowed_chars = set("0123456789+-*/(). ")
        if not all(char in allowed_chars for char in expression):
            raise ValueError("Expression contains invalid characters.")

        return expression.replace(" ", "")

    def _is_valid_expression(self, expression: str) -> bool:
        """
        Checks whether a mathematical expression is valid.

        Args:
            expression (str): A string containing the mathematical expression.

        Returns:
            bool: True if the expression is valid, False otherwise.
        """
        if not expression:
            return False

        stack = []
        for char in expression:
            if char == '(':
                stack.append(char)
            elif char == ')':
                if not stack:
                    return False
                stack.pop()

        if stack:
            return False

        # Check for consecutive operators
        for i in range(len(expression) - 1):
            if expression[i] in self.operators and expression[i + 1] in self.operators:
                return False

        # Check for leading or trailing operators
        if expression[0] in self.operators or expression[-1] in self.operators:
            return False

        return True

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes a mathematical expression into numbers and operators.

        Args:
            expression (str): A string containing the mathematical expression.

        Returns:
            list: A list of tokens (numbers as floats and operators as strings).
        """
        tokens = []
        current_number = ""
        for char in expression:
            if char.isdigit() or char == '.':
                current_number += char
            else:
                if current_number:
                    tokens.append(float(current_number))
                    current_number = ""
                if char in self.operators or char in "()":
                    tokens.append(char)
        if current_number:
            tokens.append(float(current_number))
        return tokens

    def _evaluate_expression(self, tokens: list) -> tuple:
        """
        Evaluates a tokenized mathematical expression recursively.

        Args:
            tokens (list): A list of tokens to evaluate.

        Returns:
            tuple: A tuple containing the result of the evaluation and the number of tokens consumed.
        """
        result = 0
        current_operator = '+'
        index = 0

        while index < len(tokens):
            token = tokens[index]
            if token == '(':
                subexpr_result, consumed = self._evaluate_expression(tokens[index + 1:])
                index += consumed + 1
                token = subexpr_result
                if tokens[index] != ')':
                    raise ValueError("Unbalanced parentheses")
                index += 1

            if isinstance(token, float):
                if current_operator == '+':
                    result += token
                elif current_operator == '-':
                    result -= token
                elif current_operator == '*':
                    result *= token
                elif current_operator == '/':
                    if token == 0:
                        raise ValueError("Division by zero")
                    result /= token
                current_operator = '+'
            elif token in self.operators:
                if token in '+-' and current_operator in '+-':
                    current_operator = token
                elif token in '*/' and current_operator in '*/':
                    current_operator = token
                else:
                    break
            index += 1

        if index < len(tokens) and tokens[index] in self.operators:
            next_result, consumed = self._evaluate_expression(tokens[index:])
            index += consumed
            if tokens[index - consumed] == '+':
                result += next_result
            elif tokens[index - consumed] == '-':
                result -= next_result
            elif tokens[index - consumed] == '*':
                result *= next_result
            elif tokens[index - consumed] == '/':
                if next_result == 0:
                    raise ValueError("Division by zero")
                result /= next_result

        return result, index
