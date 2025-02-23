
class AsciiArt:
    """
    A class for creating ASCII art shapes.

    This class provides methods to draw various filled shapes using ASCII characters.
    """

    @staticmethod
    def validate_input(width: int, height: int = None, diameter: int = None) -> None:
        """
        Validates input parameters to ensure they are positive integers.

        :param width: The width of the shape.
        :param height: The height of the shape, if applicable.
        :param diameter: The diameter of the circle, if applicable.
        :raises ValueError: If any of the inputs are not positive integers.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if height is not None and (not isinstance(height, int) or height <= 0):
            raise ValueError("Height must be a positive integer.")
        if diameter is not None and (not isinstance(diameter, int) or diameter <= 0):
            raise ValueError("Diameter must be a positive integer.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a filled square of given width using the specified symbol.

        :param width: The width (and height) of the square.
        :param symbol: The character to use for drawing.
        :return: A string representation of the square.
        """
        AsciiArt.validate_input(width)
        return '\n'.join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle of given width and height using the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The character to use for drawing.
        :return: A string representation of the rectangle.
        """
        AsciiArt.validate_input(width, height)
        return '\n'.join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle of given diameter using the specified symbol.

        :param diameter: The diameter of the circle.
        :param symbol: The character to use for drawing.
        :return: A string representation of the circle.
        """
        AsciiArt.validate_input(diameter=diameter)
        radius = diameter // 2
        result = []
        for y in range(diameter):
            line = ''.join([symbol if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2 else ' ' 
                            for x in range(diameter)])
            result.append(line)
        return '\n'.join(result)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle of given width and height using the specified symbol.

        :param width: The width of the triangle's base.
        :param height: The height of the triangle.
        :param symbol: The character to use for drawing.
        :return: A string representation of the triangle.
        """
        AsciiArt.validate_input(width, height)
        result = []
        for h in range(1, height + 1):
            w = int(width * h / height)
            result.append(symbol * w)
        return '\n'.join(result)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a filled symmetrical pyramid of given height using the specified symbol.

        :param height: The height of the pyramid.
        :param symbol: The character to use for drawing.
        :return: A string representation of the pyramid.
        """
        AsciiArt.validate_input(height)
        result = []
        for h in range(1, height + 1):
            spaces = ' ' * (height - h)
            symbols = symbol * (2 * h - 1)
            result.append(spaces + symbols)
        return '\n'.join(result)


ascii_art = AsciiArt()
print(ascii_art.draw_square(5, '*'))
print(ascii_art.draw_circle(10, 'O'))
