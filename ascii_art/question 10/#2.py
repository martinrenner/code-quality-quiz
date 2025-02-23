
class AsciiArt:
    def __init__(self, symbol: str):
        """
        Initializes the AsciiArt class with a printable symbol.

        :param symbol: The symbol used to draw the ASCII art.
        :raises ValueError: If the symbol is not a single printable character.
        """
        if len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")
        self.symbol = symbol

    def draw_square(self, width: int) -> str:
        """
        Draws a square using the specified symbol.

        :param width: The width of the square.
        :return: A multi-line string representing the ASCII square.
        :raises ValueError: If width is not a positive integer.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        return '\n'.join([self.symbol * width for _ in range(width)])

    def draw_rectangle(self, width: int, height: int) -> str:
        """
        Draws a rectangle using the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: A multi-line string representing the ASCII rectangle.
        :raises ValueError: If width or height is not a positive integer.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return '\n'.join([self.symbol * width for _ in range(height)])

    def draw_circle(self, diameter: int) -> str:
        """
        Draws an approximate circle using the specified symbol.

        :param diameter: The diameter of the circle.
        :return: A multi-line string representing the ASCII circle.
        :raises ValueError: If diameter is not a positive integer.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        radius = diameter // 2
        result = []
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                if x * x + y * y <= radius * radius:
                    line.append(self.symbol)
                else:
                    line.append(' ')
            result.append(''.join(line))
        return '\n'.join(result)

    def draw_triangle(self, width: int, height: int) -> str:
        """
        Draws a right-angled triangle using the specified symbol.

        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :return: A multi-line string representing the ASCII right-angled triangle.
        :raises ValueError: If width or height is not a positive integer.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return '\n'.join([self.symbol * (i + 1) for i in range(min(width, height))])

    def draw_pyramid(self, height: int) -> str:
        """
        Draws a symmetrical pyramid using the specified symbol.

        :param height: The height of the pyramid.
        :return: A multi-line string representing the ASCII pyramid.
        :raises ValueError: If height is not a positive integer.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        result = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            symbols = self.symbol * (2 * i + 1)
            result.append(spaces + symbols + spaces)
        return '\n'.join(result)

# Example usage:
if __name__ == "__main__":
    art = AsciiArt('*')
    print("Square:")
    print(art.draw_square(5))
    print("\nRectangle:")
    print(art.draw_rectangle(5, 3))
    print("\nCircle:")
    print(art.draw_circle(9))
    print("\nTriangle:")
    print(art.draw_triangle(5, 5))
    print("\nPyramid:")
    print(art.draw_pyramid(5))
