import math

class AsciiArt:
    """A class for generating 2D ASCII art shapes."""

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of given width filled with the specified symbol.

        Args:
            width (int): The width of the square.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn square.

        Raises:
            ValueError: If width is less than 1 or symbol is empty.
        """
        if width < 1:
            raise ValueError("Width must be at least 1.")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        return self._create_filled_shape(width, width, symbol)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of given dimensions filled with the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn rectangle.

        Raises:
            ValueError: If width or height is less than 1, or if symbol is empty.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        return self._create_filled_shape(width, height, symbol)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle of given diameter filled with the specified symbol.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn circle.

        Raises:
            ValueError: If diameter is less than 1 or symbol is empty.
        """
        if diameter < 1:
            raise ValueError("Diameter must be at least 1.")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        radius = diameter // 2
        result = []
        for y in range(diameter):
            row = []
            for x in range(diameter):
                dx = x - radius
                dy = y - radius
                if dx*dx + dy*dy <= radius*radius:
                    row.append(symbol)
                else:
                    row.append(' ')
            result.append(''.join(row))
        return '\n'.join(result)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle of given dimensions filled with the specified symbol.

        Args:
            width (int): The width of the triangle (base).
            height (int): The height of the triangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn triangle.

        Raises:
            ValueError: If width or height is less than 1, or if symbol is empty.
        """
        if width < 1 or height < 1:
            raise ValueError("Width and height must be at least 1.")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        result = []
        for i in range(height):
            row = symbol * (1 + i * width // height)
            result.append(row.ljust(width))
        return '\n'.join(result)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid of given height filled with the specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the drawn pyramid.

        Raises:
            ValueError: If height is less than 1 or symbol is empty.
        """
        if height < 1:
            raise ValueError("Height must be at least 1.")
        if not symbol:
            raise ValueError("Symbol cannot be empty.")

        result = []
        for i in range(height):
            width = 2 * i + 1
            row = symbol * width
            result.append(row.center(2 * height - 1))
        return '\n'.join(result)

    def _create_filled_shape(self, width: int, height: int, symbol: str) -> str:
        """Helper method to create a filled rectangular shape."""
        return '\n'.join([symbol * width for _ in range(height)])

# Example usage
if __name__ == "__main__":
    ascii_art = AsciiArt()

    print("Square:")
    print(ascii_art.draw_square(5, '#'))
    print("\nRectangle:")
    print(ascii_art.draw_rectangle(7, 3, '*'))
    print("\nCircle:")
    print(ascii_art.draw_circle(10, 'O'))
    print("\nTriangle:")
    print(ascii_art.draw_triangle(5, 3, 'T'))
    print("\nPyramid:")
    print(ascii_art.draw_pyramid(5, 'P'))
