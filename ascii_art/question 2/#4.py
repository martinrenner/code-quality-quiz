
class AsciiArt:
    """
    A class for generating ASCII art shapes.

    This class provides methods to draw various shapes using a specified symbol.
    Each method returns a multi-line string representing the ASCII art.
    """

    @staticmethod
    def _validate_input(value: int, min_value: int = 1) -> None:
        """
        Validates that the input is a positive integer.

        :param value: The value to validate.
        :param min_value: The minimum allowed value (default is 1).
        :raises ValueError: If the input is not a positive integer.
        """
        if not isinstance(value, int) or value < min_value:
            raise ValueError(f"Input must be an integer greater than or equal to {min_value}.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a single character.

        :param symbol: The symbol to validate.
        :raises ValueError: If the symbol is not a single character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a square of the specified width using the given symbol.

        :param width: The width (and height) of the square.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the square.
        :raises ValueError: If input values are invalid.
        """
        cls._validate_input(width)
        cls._validate_symbol(symbol)
        return cls._draw_filled_rectangle(width, width, symbol)

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the specified width and height using the given symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the rectangle.
        :raises ValueError: If input values are invalid.
        """
        cls._validate_input(width)
        cls._validate_input(height)
        cls._validate_symbol(symbol)
        return cls._draw_filled_rectangle(width, height, symbol)

    @staticmethod
    def _draw_filled_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Helper method to draw a filled rectangle.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the filled rectangle.
        """
        return '\n'.join([symbol * width for _ in range(height)])

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of the specified diameter using the given symbol.

        :param diameter: The diameter of the circle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the circle.
        :raises ValueError: If input values are invalid.
        """
        cls._validate_input(diameter)
        cls._validate_symbol(symbol)
        radius = diameter // 2
        return cls._draw_filled_circle(radius, symbol)

    @staticmethod
    def _draw_filled_circle(radius: int, symbol: str) -> str:
        """
        Helper method to draw a filled circle.

        :param radius: The radius of the circle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the filled circle.
        """
        def circle_line(y):
            x = int((radius**2 - y**2)**0.5 + 0.5)
            return symbol * x + ' ' * (2 * (radius - x)) + symbol * x if x > 0 else ' ' * (2 * radius)

        return '\n'.join(circle_line(y) for y in range(radius + 1)) + \
               '\n'.join(circle_line(y) for y in range(radius - 1, -1, -1))

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle of the specified width and height using the given symbol.

        :param width: The width of the triangle base.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the triangle.
        :raises ValueError: If input values are invalid.
        """
        cls._validate_input(width)
        cls._validate_input(height)
        cls._validate_symbol(symbol)
        return cls._draw_filled_triangle(width, height, symbol)

    @staticmethod
    def _draw_filled_triangle(width: int, height: int, symbol: str) -> str:
        """
        Helper method to draw a filled right-angled triangle.

        :param width: The width of the triangle base.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the filled triangle.
        """
        return '\n'.join([symbol * min((i + 1) * width // height, width) for i in range(height)])

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid of the specified height using the given symbol.

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the pyramid.
        :raises ValueError: If input values are invalid.
        """
        cls._validate_input(height)
        cls._validate_symbol(symbol)
        return cls._draw_filled_pyramid(height, symbol)

    @staticmethod
    def _draw_filled_pyramid(height: int, symbol: str) -> str:
        """
        Helper method to draw a filled symmetrical pyramid.

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the filled pyramid.
        """
        width = 2 * height - 1
        return '\n'.join([' ' * (width - 2 * i - 1) // 2 + symbol * (2 * i + 1) for i in range(height)])


ascii_art = AsciiArt()

# Draw a square
print(ascii_art.draw_square(5, '#'))

# Draw a rectangle
print(ascii_art.draw_rectangle(10, 3, '*'))

# Draw a circle
print(ascii_art.draw_circle(15, 'O'))

# Draw a right-angled triangle
print(ascii_art.draw_triangle(7, 4, 'X'))

# Draw a pyramid
print(ascii_art.draw_pyramid(6, '+'))
