class AsciiArt:
    def __init__(self, symbol: str):
        """
        Initialize the AsciiArt class with a specified symbol.

        :param symbol: The symbol to be used for drawing shapes.
        """
        if not symbol or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")
        self.symbol = symbol

    def draw_square(self, width: int) -> str:
        """
        Draw a square with the specified width.

        :param width: The width of the square.
        :return: A multi-line string representing the square.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        return '\n'.join([self.symbol * width for _ in range(width)])

    def draw_rectangle(self, width: int, height: int) -> str:
        """
        Draw a rectangle with the specified width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: A multi-line string representing the rectangle.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return '\n'.join([self.symbol * width for _ in range(height)])

    def draw_circle(self, diameter: int) -> str:
        """
        Draw an approximate circle with the specified diameter.

        :param diameter: The diameter of the circle.
        :return: A multi-line string representing the circle.
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
        Draw a right-angled triangle with the specified width and height.

        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :return: A multi-line string representing the triangle.
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
        Draw a symmetrical pyramid with the specified height.

        :param height: The height of the pyramid.
        :return: A multi-line string representing the pyramid.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        pyramid = []
        for i in range(height):
            line = ' ' * (height - i - 1) + self.symbol * (2 * i + 1)
            pyramid.append(line)
        return '\n'.join(pyramid)

# Example usage:
if __name__ == "__main__":
    symbol = input("Enter the symbol to use for drawing: ")
    ascii_art = AsciiArt(symbol)

    print("Square:")
    print(ascii_art.draw_square(5))

    print("\nRectangle:")
    print(ascii_art.draw_rectangle(5, 3))

    print("\nCircle:")
    print(ascii_art.draw_circle(9))

    print("\nTriangle:")
    print(ascii_art.draw_triangle(5, 5))

    print("\nPyramid:")
    print(ascii_art.draw_pyramid(5))
