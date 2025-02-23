
import math

class AsciiArt:
    """
    A class used to generate ASCII art shapes.

    This class includes methods to draw various geometric shapes using specified symbols.
    """

    @staticmethod
    def validate_inputs(*args):
        """
        Validate input parameters to ensure they are positive integers.

        :param args: Variable length argument list of integers to validate
        :raises ValueError: If any argument is not a positive integer
        """
        for arg in args:
            if not isinstance(arg, int) or arg <= 0:
                raise ValueError("All dimensions must be positive integers.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draw a square with the specified width and symbol.

        :param width: The width (and height) of the square
        :param symbol: The symbol to use for drawing
        :return: A multi-line string representing the square
        :raises ValueError: If inputs are invalid
        """
        AsciiArt.validate_inputs(width)
        return '\n'.join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draw a rectangle with the specified width, height, and symbol.

        :param width: The width of the rectangle
        :param height: The height of the rectangle
        :param symbol: The symbol to use for drawing
        :return: A multi-line string representing the rectangle
        :raises ValueError: If inputs are invalid
        """
        AsciiArt.validate_inputs(width, height)
        return '\n'.join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draw an approximate circle with the specified diameter and symbol.

        :param diameter: The diameter of the circle
        :param symbol: The symbol to use for drawing
        :return: A multi-line string representing the circle
        :raises ValueError: If inputs are invalid
        """
        AsciiArt.validate_inputs(diameter)
        radius = diameter // 2
        circle = []
        for y in range(diameter):
            row = ''
            for x in range(diameter):
                if int(math.sqrt((x - radius) ** 2 + (y - radius) ** 2)) <= radius:
                    row += symbol
                else:
                    row += ' '
            circle.append(row)
        return '\n'.join(circle)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draw a right-angled triangle with the specified width, height, and symbol.

        :param width: The width of the triangle's base
        :param height: The height of the triangle
        :param symbol: The symbol to use for drawing
        :return: A multi-line string representing the triangle
        :raises ValueError: If inputs are invalid
        """
        AsciiArt.validate_inputs(width, height)
        triangle = []
        for h in range(height):
            row = symbol * min(width, h + 1)
            triangle.append(row)
        return '\n'.join(triangle)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draw a symmetrical pyramid with the specified height and symbol.

        :param height: The height of the pyramid
        :param symbol: The symbol to use for drawing
        :return: A multi-line string representing the pyramid
        :raises ValueError: If inputs are invalid
        """
        AsciiArt.validate_inputs(height)
        pyramid = []
        for h in range(height):
            spaces = ' ' * (height - h - 1)
            symbols = symbol * (2 * h + 1)
            pyramid.append(spaces + symbols)
        return '\n'.join(pyramid)
