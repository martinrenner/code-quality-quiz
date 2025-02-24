class AsciiArt:
    """
    A class for creating ASCII art shapes.

    This class provides methods to draw various 2D shapes using ASCII characters.
    Each shape is completely filled with a user-specified symbol.
    """

    @staticmethod
    def _validate_positive_int(value: int, name: str) -> None:
        """
        Validates that the given value is a positive integer.

        Args:
            value (int): The value to validate.
            name (str): The name of the parameter for error messaging.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates that the given symbol is a single printable character.

        Args:
            symbol (str): The symbol to validate.

        Raises:
            ValueError: If the symbol is not a single printable character.
        """
        if len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a square of the specified width using the given symbol.

        Args:
            width (int): The width (and height) of the square.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn square.

        Raises:
            ValueError: If width is not a positive integer or symbol is invalid.
        """
        cls._validate_positive_int(width, "width")
        cls._validate_symbol(symbol)
        return '\n'.join([symbol * width] * width)

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the specified width and height using the given symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn rectangle.

        Raises:
            ValueError: If width or height are not positive integers or symbol is invalid.
        """
        cls._validate_positive_int(width, "width")
        cls._validate_positive_int(height, "height")
        cls._validate_symbol(symbol)
        return '\n'.join([symbol * width] * height)

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of the specified diameter using the given symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn circle.

        Raises:
            ValueError: If diameter is not a positive integer or symbol is invalid.
        """
        cls._validate_positive_int(diameter, "diameter")
        cls._validate_symbol(symbol)
        radius = diameter // 2
        circle = []
        for y in range(diameter):
            line = []
            for x in range(diameter):
                dx = x - radius
                dy = y - radius
                if dx*dx + dy*dy <= radius*radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle.append(''.join(line))
        return '\n'.join(circle)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle of the specified width and height using the given symbol.

        Args:
            width (int): The width of the triangle's base.
            height (int): The height of the triangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn triangle.

        Raises:
            ValueError: If width or height are not positive integers or symbol is invalid.
        """
        cls._validate_positive_int(width, "width")
        cls._validate_positive_int(height, "height")
        cls._validate_symbol(symbol)
        triangle = []
        for i in range(height):
            line_width = min(width, i + 1)
            triangle.append(symbol * line_width)
        return '\n'.join(triangle)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid of the specified height using the given symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn pyramid.

        Raises:
            ValueError: If height is not a positive integer or symbol is invalid.
        """
        cls._validate_positive_int(height, "height")
        cls._validate_symbol(symbol)
        pyramid = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            line = spaces + symbol * (2 * i + 1)
            pyramid.append(line)
        return '\n'.join(pyramid)


ascii_art = AsciiArt()

print(ascii_art.draw_square(5, '#'))
print(ascii_art.draw_rectangle(4, 3, '*'))
print(ascii_art.draw_circle(7, 'O'))
print(ascii_art.draw_triangle(5, 3, '$'))
print(ascii_art.draw_pyramid(4, '^'))
