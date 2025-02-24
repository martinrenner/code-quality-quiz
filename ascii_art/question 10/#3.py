class AsciiArt:
    """
    A class for creating 2D ASCII art shapes.

    This class provides methods to draw various shapes like square, rectangle,
    circle, triangle, and pyramid using a specified symbol.
    """

    @staticmethod
    def _validate_positive_integer(value: int, name: str) -> None:
        """
        Validate that the given value is a positive integer.

        Args:
            value (int): The value to validate.
            name (str): The name of the parameter being validated.

        Raises:
            ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validate that the given symbol is a single printable character.

        Args:
            symbol (str): The symbol to validate.

        Raises:
            ValueError: If the symbol is not a single printable character.
        """
        if len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draw a square of the specified width using the given symbol.

        Args:
            width (int): The width (and height) of the square.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the square.

        Raises:
            ValueError: If input parameters are invalid.
        """
        self._validate_positive_integer(width, "width")
        self._validate_symbol(symbol)

        return (symbol * width + '\n') * width

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draw a rectangle of the specified width and height using the given symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the rectangle.

        Raises:
            ValueError: If input parameters are invalid.
        """
        self._validate_positive_integer(width, "width")
        self._validate_positive_integer(height, "height")
        self._validate_symbol(symbol)

        return (symbol * width + '\n') * height

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draw an approximate circle of the specified diameter using the given symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the circle.

        Raises:
            ValueError: If input parameters are invalid.
        """
        self._validate_positive_integer(diameter, "diameter")
        self._validate_symbol(symbol)

        radius = diameter // 2
        result = []

        for y in range(diameter):
            line = ''
            for x in range(diameter):
                dx = x - radius
                dy = y - radius
                if dx*dx + dy*dy <= radius*radius:
                    line += symbol
                else:
                    line += ' '
            result.append(line)

        return '\n'.join(result) + '\n'

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draw a right-angled triangle of the specified width and height using the given symbol.

        Args:
            width (int): The width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the triangle.

        Raises:
            ValueError: If input parameters are invalid.
        """
        self._validate_positive_integer(width, "width")
        self._validate_positive_integer(height, "height")
        self._validate_symbol(symbol)

        result = []
        for i in range(height):
            line_width = min(width, i + 1)
            result.append(symbol * line_width)

        return '\n'.join(result) + '\n'

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draw a symmetrical pyramid of the specified height using the given symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use for drawing.

        Returns:
            str: A multi-line string representing the pyramid.

        Raises:
            ValueError: If input parameters are invalid.
        """
        self._validate_positive_integer(height, "height")
        self._validate_symbol(symbol)

        result = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            line = spaces + symbol * (2 * i + 1)
            result.append(line)

        return '\n'.join(result) + '\n'
