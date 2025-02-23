
class Calculator:
    def __init__(self):
        self.operators = {'+': lambda x, y: x + y,
                          '-': lambda x, y: x - y,
                          '*': lambda x, y: x * y,
                          '/': lambda x, y: x / y}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression and returns the result.

        :param expression: str - The arithmetic expression to evaluate
        :return: float - The result of the evaluated expression
        :raises: ValueError - If the expression contains invalid characters or is malformed
        """
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        return self._evaluate_postfix(postfix)

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the given expression into a list of tokens.

        :param expression: str - The arithmetic expression to tokenize
        :return: list - The list of tokens
        :raises: ValueError - If the expression contains invalid characters
        """
        tokens = []
        number = ''
        for char in expression:
            if char.isdigit() or char == '.':
                number += char
            else:
                if number:
                    tokens.append(float(number))
                    number = ''
                if char in self.operators or char in '()':
                    tokens.append(char)
                elif char.isspace():
                    continue
                else:
                    raise ValueError(f"Invalid character: {char}")
        if number:
            tokens.append(float(number))
        return tokens

    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts the infix expression to postfix notation.

        :param tokens: list - The list of tokens in infix notation
        :return: list - The list of tokens in postfix notation
        :raises: ValueError - If the expression is malformed (e.g., unbalanced parentheses)
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        stack = []
        postfix = []
        for token in tokens:
            if isinstance(token, float):
                postfix.append(token)
            elif token == '(':
                stack.append(token)
            elif token == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                if not stack:
                    raise ValueError("Unbalanced parentheses")
                stack.pop()
            else:
                while stack and precedence[token] <= precedence.get(stack[-1], 0):
                    postfix.append(stack.pop())
                stack.append(token)
        while stack:
            if stack[-1] == '(':
                raise ValueError("Unbalanced parentheses")
            postfix.append(stack.pop())
        return postfix

    def _evaluate_postfix(self, postfix: list) -> float:
        """
        Evaluates the postfix expression and returns the result.

        :param postfix: list - The list of tokens in postfix notation
        :return: float - The result of the evaluated expression
        :raises: ValueError - If the expression is malformed or division by zero is attempted
        """
        stack = []
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                if len(stack) < 2:
                    raise ValueError("Malformed expression")
                right = stack.pop()
                left = stack.pop()
                if token == '/' and right == 0:
                    raise ValueError("Division by zero")
                stack.append(self.operators[token](left, right))
        if len(stack) != 1:
            raise ValueError("Malformed expression")
        return stack[0]


# Example usage
if __name__ == "__main__":
    calculator = Calculator()

    while True:
        try:
            expression = input("Enter an arithmetic expression (or 'quit' to exit): ")
            if expression.lower() == 'quit':
                break
            result = calculator.calculate(expression)
            print(f"Result: {result}")
        except ValueError as e:
            print(f"Error: {str(e)}")
