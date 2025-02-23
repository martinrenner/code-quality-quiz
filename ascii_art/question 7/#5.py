
class AsciiArt:
    def __init__(self):
        pass

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square using the specified symbol.
        
        :param width: The width of the square.
        :param symbol: The symbol to use for drawing the square.
        :return: A multi-line string representing the ASCII art of the square.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        
        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square.rstrip()

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle using the specified symbol.
        
        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing the rectangle.
        :return: A multi-line string representing the ASCII art of the rectangle.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        
        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle.rstrip()

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the specified symbol.
        
        :param diameter: The diameter of the circle.
        :param symbol: The symbol to use for drawing the circle.
        :return: A multi-line string representing the ASCII art of the circle.
        """
        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        
        circle = ""
        radius = diameter // 2
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                if i * i + j * j <= radius * radius:
                    circle += symbol
                else:
                    circle += " "
            circle += "\n"
        return circle.rstrip()

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the specified symbol.
        
        :param width: The width of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing the triangle.
        :return: A multi-line string representing the ASCII art of the triangle.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        
        triangle = ""
        for i in range(1, height + 1):
            triangle += symbol * min(i, width) + "\n"
        return triangle.rstrip()

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the specified symbol.
        
        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing the pyramid.
        :return: A multi-line string representing the ASCII art of the pyramid.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        
        pyramid = ""
        width = 2 * height - 1
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            symbols = symbol * (2 * i - 1)
            pyramid += spaces + symbols + spaces + "\n"
        return pyramid.rstrip()
