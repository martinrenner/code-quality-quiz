
class AsciiArt:
    def __init__(self, symbol: str = '*'):
        """
        Initializes the AsciiArt class with a specified symbol.

        :param symbol: The symbol to use for drawing shapes. Default is '*'.
        """
        if not symbol or len(symbol) != 1:
            raise ValueError("Symbol must be a single printable character.")
        self.symbol = symbol

    def draw_square(self, width: int) -> str:
        """
        Draws a square of the specified width.

        :param width: The width of the square.
        :return: A multi-line string representing the square.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        return '\n'.join([self.symbol * width] * width)

    def draw_rectangle(self, width: int, height: int) -> str:
        """
        Draws a rectangle of the specified width and height.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :return: A multi-line string representing the rectangle.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        return '\n'.join([self.symbol * width] * height)

    def draw_circle(self, diameter: int) -> str:
        """
        Draws an approximate circle of the specified diameter.

        :param diameter: The diameter of the circle.
        :return: A multi-line string representing the circle.
        """
        if diameter <= 0 or diameter % 2 == 0:
            raise ValueError("Diameter must be a positive odd integer.")
        radius = diameter // 2
        result = []
        for y in range(-radius, radius + 1):
            line = ''
            for x in range(-radius, radius + 1):
                if x*x + y*y <= radius*radius:
                    line += self.symbol
                else:
                    line += ' '
            result.append(line)
        return '\n'.join(result)

    def draw_triangle(self, width: int, height: int) -> str:
        """
        Draws a right-angled triangle of the specified width and height.

        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :return: A multi-line string representing the triangle.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        result = []
        for i in range(height):
            line = self.symbol * (i + 1)
            result.append(line.ljust(width))
        return '\n'.join(result)

    def draw_pyramid(self, height: int) -> str:
        """
        Draws a symmetrical pyramid of the specified height.

        :param height: The height of the pyramid.
        :return: A multi-line string representing the pyramid.
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
    art = AsciiArt(symbol='#')
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
