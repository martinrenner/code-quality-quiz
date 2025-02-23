
class Calculator:
    def __init__(self):
        self.operators = {'+': 1, '-': 1, '*': 2, '/': 2}

    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression and returns the result.

        Args:
            expression (str): The arithmetic expression to evaluate.

        Returns:
            float: The result of the evaluated expression.

        Raises:
            ValueError: If the expression is invalid or contains unsupported characters.
            ZeroDivisionError: If division by zero is encountered.
        """
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        result = self._evaluate_postfix(postfix)
        return result

    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the arithmetic expression into a list of tokens.

        Args:
            expression (str): The arithmetic expression to tokenize.

        Returns:
            list: A list of tokens representing the expression.
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

        Args:
            tokens (list): A list of tokens representing the infix expression.

        Returns:
            list: A list of tokens representing the postfix expression.
        """
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
                while stack and stack[-1] != '(' and self.operators[token] <= self.operators[stack[-1]]:
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

        Args:
            postfix (list): A list of tokens representing the postfix expression.

        Returns:
            float: The result of the evaluated postfix expression.

        Raises:
            ZeroDivisionError: If division by zero is encountered.
        """
        stack = []
        for token in postfix:
            if isinstance(token, float):
                stack.append(token)
            else:
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a + b)
                elif token == '-':
                    stack.append(a - b)
                elif token == '*':
                    stack.append(a * b)
                else:
                    if b == 0:
                        raise ZeroDivisionError("Division by zero")
                    stack.append(a / b)
        return stack.pop()
