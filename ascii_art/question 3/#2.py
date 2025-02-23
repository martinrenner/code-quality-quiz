
class AsciiArt:
    def __init__(self):
        pass

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square using the given symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The symbol to use for drawing the square.

        Returns:
            str: A multi-line string representing the ASCII art of the square.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square.rstrip()

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle using the given symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for drawing the rectangle.

        Returns:
            str: A multi-line string representing the ASCII art of the rectangle.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle.rstrip()

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the given symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for drawing the circle.

        Returns:
            str: A multi-line string representing the ASCII art of the circle.
        """
        if not isinstance(diameter, int) or diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

        radius = diameter // 2
        circle = ""
        for y in range(-radius, radius + 1):
            for x in range(-radius, radius + 1):
                if x * x + y * y <= radius * radius:
                    circle += symbol
                else:
                    circle += " "
            circle += "\n"
        return circle.rstrip()

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the given symbol.

        Args:
            width (int): The width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to use for drawing the triangle.

        Returns:
            str: A multi-line string representing the ASCII art of the triangle.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

        triangle = ""
        for i in range(1, height + 1):
            triangle += symbol * min(i, width) + "\n"
        return triangle.rstrip()

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the given symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for drawing the pyramid.

        Returns:
            str: A multi-line string representing the ASCII art of the pyramid.
        """
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

        pyramid = ""
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            pyramid += spaces + symbol * (2 * i - 1) + spaces + "\n"
        return pyramid.rstrip()
