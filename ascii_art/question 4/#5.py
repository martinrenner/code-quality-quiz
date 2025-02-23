
class AsciiArt:
    """
    A class to generate ASCII art shapes.
    """

    def __init__(self, symbol: str):
        """
        Initializes the AsciiArt class with a printable symbol.

        :param symbol: The symbol to use for drawing shapes.
        :raises ValueError: If the symbol is not a single printable character.
        """
        if not symbol or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")
        self.symbol = symbol

    def draw_square(self, width: int) -> str:
        """
        Draws a square filled with the specified symbol.

        :param width: The width of the square.
        :return: A multi-line string representing the ASCII art square.
        :raises ValueError: If the width is not a positive integer.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        return self._draw_rectangle(width, width)

    def draw_rectangle(self, width: int, height: int) -> str:
        """
        Draws a rectangle filled with the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: A multi-line string representing the ASCII art rectangle.
        :raises ValueError: If the width or height is not a positive integer.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return self._draw_rectangle(width, height)

    def _draw_rectangle(self, width: int, height: int) -> str:
        """
        Helper method to draw a rectangle.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: A multi-line string representing the ASCII art rectangle.
        """
        return '\n'.join([self.symbol * width for _ in range(height)])

    def draw_circle(self, diameter: int) -> str:
        """
        Draws an approximate circle filled with the specified symbol.

        :param diameter: The diameter of the circle.
        :return: A multi-line string representing the ASCII art circle.
        :raises ValueError: If the diameter is not a positive integer.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        radius = diameter // 2
        circle = []
        for y in range(-radius, radius + 1):
            line = ''
            for x in range(-radius, radius + 1):
                if x*x + y*y <= radius*radius:
                    line += self.symbol
                else:
                    line += ' '
            circle.append(line)
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.

        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :return: A multi-line string representing the ASCII art triangle.
        :raises ValueError: If the width or height is not a positive integer.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        triangle = []
        for i in range(height):
            line = self.symbol * (i + 1)
            triangle.append(line.ljust(width))
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.

        :param height: The height of the pyramid.
        :return: A multi-line string representing the ASCII art pyramid.
        :raises ValueError: If the height is not a positive integer.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        pyramid = []
        for i in range(height):
            line = self.symbol * (2 * i + 1)
            pyramid.append(line.center(2 * height - 1))
        return '\n'.join(pyramid)
