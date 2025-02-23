
class AsciiArt:
    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square using the specified symbol.
        :param width: The width of the square.
        :param symbol: The symbol to use for drawing the square.
        :return: A multi-line string representing the ASCII square.
        """
        if not (1 <= width <= 100):
            raise ValueError("Width must be between 1 and 100.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle using the specified symbol.
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing the rectangle.
        :return: A multi-line string representing the ASCII rectangle.
        """
        if not (1 <= width <= 100 and 1 <= height <= 100):
            raise ValueError("Width and height must be between 1 and 100.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the specified symbol.
        :param diameter: The diameter of the circle.
        :param symbol: The symbol to use for drawing the circle.
        :return: A multi-line string representing the ASCII circle.
        """
        if not (1 <= diameter <= 100):
            raise ValueError("Diameter must be between 1 and 100.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        lines = []
        radius = diameter // 2
        for y in range(-radius, radius + 1):
            line = ''
            for x in range(-radius, radius + 1):
                if x * x + y * y <= radius * radius:
                    line += symbol
                else:
                    line += ' '
            lines.append(line)
        return '\n'.join(lines)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the specified symbol.
        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing the triangle.
        :return: A multi-line string representing the ASCII triangle.
        """
        if not (1 <= width <= 100 and 1 <= height <= 100):
            raise ValueError("Width and height must be between 1 and 100.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        lines = []
        for i in range(1, height + 1):
            line = symbol * (i * width // height)
            lines.append(line)
        return '\n'.join(lines)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the specified symbol.
        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing the pyramid.
        :return: A multi-line string representing the ASCII pyramid.
        """
        if not (1 <= height <= 100):
            raise ValueError("Height must be between 1 and 100.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        lines = []
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            line = spaces + symbol * (2 * i - 1) + spaces
            lines.append(line)
        return '\n'.join(lines)
