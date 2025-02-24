class AsciiArt:
    """
    A class for generating console-based 2D ASCII art.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a filled square of the given width using the specified symbol.

        Args:
            width: The width (and height) of the square.
            symbol: The character to use for drawing.

        Returns:
            A multi-line string representing the square.

        Raises:
            ValueError: If width is not positive or symbol is not a single character.
        """
        self._validate_dimensions(width)
        self._validate_symbol(symbol)

        square_str = ""
        for _ in range(width):
            square_str += symbol * width + "\n"
        return square_str

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle of the given dimensions using the specified symbol.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            symbol: The character to use for drawing.

        Returns:
            A multi-line string representing the rectangle.

        Raises:
            ValueError: If width or height are not positive, or symbol is not a single character.
        """
        self._validate_dimensions(width, height)
        self._validate_symbol(symbol)

        rectangle_str = ""
        for _ in range(height):
            rectangle_str += symbol * width + "\n"
        return rectangle_str

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle (more accurately, a filled diamond)
        of the given diameter using the specified symbol.

        Args:
            diameter: The diameter of the circle.
            symbol: The character to use for drawing.

        Returns:
            A multi-line string representing the circle.

        Raises:
            ValueError: If diameter is not positive or symbol is not a single character.
        """
        self._validate_dimensions(diameter)
        self._validate_symbol(symbol)

        radius = diameter // 2
        circle_str = ""

        for row in range(-radius, radius + 1):
            for col in range(-radius, radius + 1):
                # Simple distance check for a diamond-like shape.
                if abs(row) + abs(col) <= radius:
                    circle_str += symbol
                else:
                    circle_str += " "  # Add spaces for the outside of the circle
            circle_str += "\n"
        return circle_str

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle with the given dimensions.

        Args:
            width: the base width of the triangle
            height: The height of the triangle.
            symbol: The character to use for drawing.

        Returns:
            A multi-line string representing the triangle.

        Raises:
            ValueError: If the base width or height are not positive or symbol is not a single character.
        """

        self._validate_dimensions(width, height)
        self._validate_symbol(symbol)

        triangle_str = ""
        for row in range(height):
            # Calculate the number of symbols needed for the current row
            num_symbols = int((row + 1) * (width / height))
            triangle_str += symbol * num_symbols + "\n"
        return triangle_str
    
    def draw_pyramid(self, height: int, symbol: str) -> str:
        """Draws a filled symmetrical pyramid with specified height

        Args:
            height (int): The height of the pyramid
            symbol (str): The symbol to draw with.

        Raises:
            ValueError: If the base width or height are not positive or symbol is not a single character.

        Returns:
            str: String represention of the pyramid.
        """
        self._validate_dimensions(height)
        self._validate_symbol(symbol)

        pyramid_str = ""
        for i in range(height):
            spaces = " " * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid_str += spaces + symbols + "\n"
        return pyramid_str

    def _validate_dimensions(self, *args):
        """Helper function to validate dimensions."""
        for dim in args:
            if not isinstance(dim, int) or dim <= 0:
                raise ValueError("Dimensions must be positive integers.")

    def _validate_symbol(self, symbol: str):
        """Helper function to validate the drawing symbol."""
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")



# Example Usage (and Basic Interactive Test)
if __name__ == "__main__":
    art = AsciiArt()

    try:
        symbol = input("Enter the symbol to use: ")
        print("\nSquare:")
        print(art.draw_square(5, symbol))

        print("\nRectangle:")
        print(art.draw_rectangle(10, 4, symbol))

        print("\nCircle:")
        print(art.draw_circle(9, symbol))

        print("\nTriangle:")
        print(art.draw_triangle(7,5, symbol))
        
        print("\nPyramid")
        print(art.draw_pyramid(5, symbol))


    except ValueError as e:
        print(f"Error: {e}")

