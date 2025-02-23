
class AsciiArt:
    def __init__(self):
        pass

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square using the specified symbol.

        :param width: The width of the square.
        :param symbol: The symbol to use for drawing the square.
        :return: The ASCII art representation of the square.
        :raises ValueError: If the width is less than 1 or the symbol is not a single character.
        """
        if width < 1:
            raise ValueError("Width must be greater than or equal to 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle using the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing the rectangle.
        :return: The ASCII art representation of the rectangle.
        :raises ValueError: If the width or height is less than 1 or the symbol is not a single character.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be greater than or equal to 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the specified symbol.

        :param diameter: The diameter of the circle.
        :param symbol: The symbol to use for drawing the circle.
        :return: The ASCII art representation of the circle.
        :raises ValueError: If the diameter is less than 1 or the symbol is not a single character.
        """
        if diameter < 1:
            raise ValueError("Diameter must be greater than or equal to 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        output = []
        radius = diameter // 2
        for y in range(-radius, radius + 1):
            row = []
            for x in range(-radius, radius + 1):
                if x * x + y * y <= radius * radius:
                    row.append(symbol)
                else:
                    row.append(' ')
            output.append(''.join(row))
        return '\n'.join(output)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the specified symbol.

        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing the triangle.
        :return: The ASCII art representation of the triangle.
        :raises ValueError: If the width or height is less than 1 or the symbol is not a single character.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be greater than or equal to 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        output = []
        for i in range(1, height + 1):
            output.append(symbol * min(i, width))
        return '\n'.join(output)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the specified symbol.

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing the pyramid.
        :return: The ASCII art representation of the pyramid.
        :raises ValueError: If the height is less than 1 or the symbol is not a single character.
        """
        if height < 1:
            raise ValueError("Height must be greater than or equal to 1.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        output = []
        for i in range(1, height + 1):
            spaces = ' ' * (height - i)
            row = spaces + symbol * (2 * i - 1) + spaces
            output.append(row)
        return '\n'.join(output)
