
class AsciiArt:
    def __init__(self):
        pass

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square using the given symbol.

        :param width: The width of the square.
        :param symbol: The symbol to use for drawing the square.
        :return: A multi-line string representing the ASCII art of the square.
        :raises ValueError: If the width is less than 1 or the symbol is not a single character.
        """
        self._validate_input(width, symbol)
        return "\n".join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle using the given symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing the rectangle.
        :return: A multi-line string representing the ASCII art of the rectangle.
        :raises ValueError: If the width or height is less than 1 or the symbol is not a single character.
        """
        self._validate_input(width, symbol)
        self._validate_input(height, symbol)
        return "\n".join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the given symbol.

        :param diameter: The diameter of the circle.
        :param symbol: The symbol to use for drawing the circle.
        :return: A multi-line string representing the ASCII art of the circle.
        :raises ValueError: If the diameter is less than 1 or the symbol is not a single character.
        """
        self._validate_input(diameter, symbol)
        radius = diameter // 2
        art = []
        for y in range(-radius, radius + 1):
            row = []
            for x in range(-radius, radius + 1):
                if x * x + y * y <= radius * radius:
                    row.append(symbol)
                else:
                    row.append(" ")
            art.append("".join(row))
        return "\n".join(art)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the given symbol.

        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing the triangle.
        :return: A multi-line string representing the ASCII art of the triangle.
        :raises ValueError: If the width or height is less than 1 or the symbol is not a single character.
        """
        self._validate_input(width, symbol)
        self._validate_input(height, symbol)
        art = []
        for i in range(1, height + 1):
            row = symbol * (i * width // height)
            art.append(row)
        return "\n".join(art)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the given symbol.

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing the pyramid.
        :return: A multi-line string representing the ASCII art of the pyramid.
        :raises ValueError: If the height is less than 1 or the symbol is not a single character.
        """
        self._validate_input(height, symbol)
        art = []
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            row = spaces + symbol * (2 * i - 1) + spaces
            art.append(row)
        return "\n".join(art)

    def _validate_input(self, value: int, symbol: str):
        """
        Validates the input values for width, height, and symbol.

        :param value: The value to validate (width or height).
        :param symbol: The symbol to validate.
        :raises ValueError: If the value is less than 1 or the symbol is not a single character.
        """
        if value < 1:
            raise ValueError("Width and height must be greater than or equal to 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
