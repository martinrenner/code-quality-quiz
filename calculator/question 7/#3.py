
class Calculator:
    def calculate(self, expression: str) -> float:
        """
        Evaluates the given arithmetic expression and returns the result.
        
        Args:
            expression (str): The arithmetic expression to evaluate.
        
        Returns:
            float: The result of the evaluated expression.
        
        Raises:
            ValueError: If the expression contains invalid characters, unbalanced parentheses, or division by zero.
        """
        tokens = self._tokenize(expression)
        postfix = self._infix_to_postfix(tokens)
        result = self._evaluate_postfix(postfix)
        return result


    def _tokenize(self, expression: str) -> list:
        """
        Tokenizes the given expression into a list of tokens.
        
        Args:
            expression (str): The arithmetic expression to tokenize.
        
        Returns:
            list: A list of tokens representing the expression.
        """
        tokens = []
        num = ""
        for char in expression:
            if char.isdigit() or char == '.':
                num += char
            else:
                if num:
                    tokens.append(float(num))
                    num = ""
                if char != ' ':
                    tokens.append(char)
        if num:
            tokens.append(float(num))
        return tokens


    def _infix_to_postfix(self, tokens: list) -> list:
        """
        Converts the infix expression to postfix using the shunting yard algorithm.
        
        Args:
            tokens (list): A list of tokens representing the infix expression.
        
        Returns:
            list: A list of tokens representing the postfix expression.
        """
        precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}
        operators = []
        output = []
        for token in tokens:
            if isinstance(token, float):
                output.append(token)
            elif token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    output.append(operators.pop())
                if not operators:
                    raise ValueError("Unbalanced parentheses")
                operators.pop()
            else:
                while operators and precedence[operators[-1]] >= precedence[token]:
                    output.append(operators.pop())
                operators.append(token)
        while operators:
            if operators[-1] == '(':
                raise ValueError("Unbalanced parentheses")
            output.append(operators.pop())
        return output


    def _evaluate_postfix(self, tokens: list) -> float:
        """
        Evaluates the postfix expression and returns the result.
        
        Args:
            tokens (list): A list of tokens representing the postfix expression.
        
        Returns:
            float: The result of the evaluated postfix expression.
        """
        stack = []
        for token in tokens:
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
                elif token == '/':
                    if b == 0:
                        raise ValueError("Division by zero")
                    stack.append(a / b)
        return stack[0]
