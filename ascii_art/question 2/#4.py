class AsciiArt:
    """
    A class to generate various ASCII shapes.
    Each method returns a string representation of the specified shape.
    """

    @staticmethod
    def validate_input(positive_ints: list, symbol: str) -> None:
        """
        Validates the input parameters for the shape drawing functions.

        Args:
            positive_ints (list): List of integers that should be positive.
            symbol (str): The symbol to use for drawing.

        Raises:
            ValueError: If inputs are invalid.
        """
        for num in positive_ints:
            if not isinstance(num, int) or num <= 0:
                raise ValueError("All dimensions must be positive integers.")
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character string.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a square with the given width using the specified symbol.

        Args:
            width (int): The width (and height) of the square.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the square.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input([width], symbol)
        return '\n'.join([symbol * width for _ in range(width)])

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the given dimensions using the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the rectangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input([width, height], symbol)
        return '\n'.join([symbol * width for _ in range(height)])

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using the specified symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the circle.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input([diameter], symbol)
        radius = diameter // 2
        circle = []
        for y in range(diameter):
            line = ''
            for x in range(diameter):
                if (x - radius) ** 2 + (y - radius) ** 2 <= radius ** 2:
                    line += symbol
                else:
                    line += ' '
            circle.append(line)
        return '\n'.join(circle)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle using the specified symbol.

        Args:
            width (int): The width of the base of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the triangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input([width, height], symbol)
        triangle = []
        for i in range(height):
            line = symbol * (i + 1 if i < width else width)
            triangle.append(line)
        return '\n'.join(triangle)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid using the specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the pyramid.

        Raises:
            ValueError: If inputs are invalid.
        """
        AsciiArt.validate_input([height], symbol)
        pyramid = []
        for i in range(height):
            spaces = ' ' * (height - i - 1)
            line = spaces + symbol * (2 * i + 1)
            pyramid.append(line)
        return '\n'.join(pyramid)


# Example usage
if __name__ == "__main__":
    ascii_art = AsciiArt()
    print("Square:")
    print(ascii_art.draw_square(5, '*'))
    print("\nRectangle:")
    print(ascii_art.draw_rectangle(4, 3, '#'))
    print("\nCircle:")
    print(ascii_art.draw_circle(10, 'O'))
    print("\nTriangle:")
    print(ascii_art.draw_triangle(5, 4, '+'))
    print("\nPyramid:")
    print(ascii_art.draw_pyramid(5, '^'))
