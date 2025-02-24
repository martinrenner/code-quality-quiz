class AsciiArt:
    """A class for creating various ASCII art shapes.

    This class provides methods to draw different geometric shapes using ASCII characters.
    All methods validate inputs and return formatted multi-line strings.
    """

    @staticmethod
    def _validate_inputs(width: int, height: int, symbol: str) -> None:
        """
        Validates the input parameters for all drawing methods.

        Args:
            width (int): The width of the shape.
            height (int): The height of the shape.
            symbol (str): The symbol to use for drawing.

        Raises:
            ValueError: If inputs are invalid.
        """
        if not isinstance(width, int) or not isinstance(height, int):
            raise ValueError("Dimensions must be integers")
        if width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square with the specified width using the given symbol.

        Args:
            width (int): The width and height of the square.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the square.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(width, width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle with the specified dimensions using the given symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the rectangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(width, height, symbol)
        return '\n'.join([symbol * width] * height)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle with the specified dimensions.

        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the triangle.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(width, height, symbol)
        lines = []
        for i in range(height):
            symbols = int((i + 1) * (width / height))
            lines.append(symbol * symbols)
        return '\n'.join(lines)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid with the specified height.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the pyramid.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(height, height, symbol)
        lines = []
        for i in range(height):
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            lines.append(f"{spaces}{symbols}")
        return '\n'.join(lines)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle with the specified diameter.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for drawing.

        Returns:
            str: A multi-line string representing the circle.

        Raises:
            ValueError: If inputs are invalid.
        """
        self._validate_inputs(diameter, diameter, symbol)
        
        lines = []
        radius = diameter // 2
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Using the circle equation (x²/a² + y²/b² ≤ 1)
                if x*x + y*y <= radius*radius:
                    line.append(symbol)
                else:
                    line.append(" ")
            lines.append("".join(line))
        return '\n'.join(lines)


def main():
    """
    Main function to demonstrate the ASCII art functionality.
    """
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (5x5):")
        print(ascii_art.draw_square(5, "*"))
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, "#"))
        print("\nTriangle (5x3):")
        print(ascii_art.draw_triangle(5, 3, "@"))
        print("\nPyramid (4 high):")
        print(ascii_art.draw_pyramid(4, "+"))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, "O"))

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
