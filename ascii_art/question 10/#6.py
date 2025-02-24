class AsciiArt:
    """
    A class to generate ASCII art shapes such as squares, rectangles, circles, triangles, and pyramids.
    
    All methods return a multi-line string representation of the requested shape filled with the chosen symbol.
    """

    @staticmethod
    def validate_positive_integer(value: int, param_name: str) -> None:
        """
        Validates that the given value is a positive integer.

        Args:
            value (int): The value to validate.
            param_name (str): The name of the parameter being validated, used in error messages.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{param_name} must be a positive integer.")

    @staticmethod
    def validate_symbol(symbol: str, param_name: str) -> None:
        """
        Validates that the given symbol is a single printable character.

        Args:
            symbol (str): The symbol to validate.
            param_name (str): The name of the parameter being validated, used in error messages.

        Raises:
            ValueError: If the symbol is not a single printable character.
        """
        if len(symbol) != 1 or not symbol.isprintable():
            raise ValueError(f"{param_name} must be a single printable character.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.

        Args:
            width (int): The width and height of the square.
            symbol (str): The symbol to use for filling the square.

        Returns:
            str: A multi-line string representing the square.

        Raises:
            ValueError: If width is not a positive integer or if symbol is invalid.
        """
        self.validate_positive_integer(width, "width")
        self.validate_symbol(symbol, "symbol")
        return self.draw_rectangle(width, width, symbol)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for filling the rectangle.

        Returns:
            str: A multi-line string representing the rectangle.

        Raises:
            ValueError: If width or height are not positive integers or if symbol is invalid.
        """
        self.validate_positive_integer(width, "width")
        self.validate_positive_integer(height, "height")
        self.validate_symbol(symbol, "symbol")
        return '\n'.join(symbol * width for _ in range(height))

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for filling the circle.

        Returns:
            str: A multi-line string representing the circle.

        Raises:
            ValueError: If diameter is not a positive integer or if symbol is invalid.
        """
        self.validate_positive_integer(diameter, "diameter")
        self.validate_symbol(symbol, "symbol")
        radius = diameter // 2
        result = []
        for y in range(diameter):
            line = ''
            for x in range(diameter):
                if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2:
                    line += symbol
                else:
                    line += ' '
            result.append(line)
        return '\n'.join(result)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.

        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to use for filling the triangle.

        Returns:
            str: A multi-line string representing the triangle.

        Raises:
            ValueError: If width or height are not positive integers or if symbol is invalid.
        """
        self.validate_positive_integer(width, "width")
        self.validate_positive_integer(height, "height")
        self.validate_symbol(symbol, "symbol")
        result = []
        for i in range(height):
            line_width = min(width, i + 1)
            result.append(symbol * line_width)
        return '\n'.join(result)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for filling the pyramid.

        Returns:
            str: A multi-line string representing the pyramid.

        Raises:
            ValueError: If height is not a positive integer or if symbol is invalid.
        """
        self.validate_positive_integer(height, "height")
        self.validate_symbol(symbol, "symbol")
        result = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            line = spaces + symbol * (2 * i + 1) + spaces
            result.append(line)
        return '\n'.join(result)
