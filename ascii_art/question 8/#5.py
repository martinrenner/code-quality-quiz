
class AsciiArt:
    """
    A class for generating ASCII art shapes.
    """

    def __init__(self):
        pass  # No initialization needed at this point

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width, filled with the specified symbol.

        Args:
            width: The width (and height) of the square.
            symbol: The character to use for drawing the square.

        Returns:
            A string representing the ASCII art square.

        Raises:
            ValueError: If width is not positive or symbol is not a single character.
        """
        if width <= 0:
            raise ValueError("Width must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the given dimensions, filled with the specified symbol.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            symbol: The character to use for drawing the rectangle.

        Returns:
            A string representing the ASCII art rectangle.

        Raises:
            ValueError: If width or height are not positive, or if symbol is invalid.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle using ASCII characters.

        Args:
            diameter: The diameter of the circle.
            symbol:  The character to use for filling the circle.

        Returns:
            A multi-line string representing the ASCII art circle.

        Raises:
            ValueError: If diameter is not positive or symbol is not a single character
        """

        if diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

        radius = diameter // 2
        circle_str = ""

        for y in range(-radius, radius + 1):
            line = ""
            for x in range(-radius, radius + 1):
                distance_squared = x * x + y * y
                if distance_squared <= radius * radius:
                    line += symbol
                else:
                    line += " "  # Use space for outside the circle
            circle_str += line + "\n"
        return circle_str
    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle.

        Args:
            width: The width of the triangle's base.
            height: The height of the triangle.
            symbol: The character to use for drawing.

        Returns:
            A string representing the ASCII art triangle.

        Raises:
            ValueError: If width or height are not positive, or if symbol is invalid.
        """
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive integers.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

        triangle = ""
        for row in range(height):
            # Calculate the number of symbols to print in this row.
            # Scale the width based on the current row and height.
            num_symbols = int((row + 1) / height * width)
            triangle += symbol * num_symbols + "\n"
        return triangle

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid.

        Args:
            height: The height of the pyramid.
            symbol: The character to use.

        Returns:
            A string representing the ASCII art pyramid.

        Raises:
            ValueError: If height is not positive or symbol is invalid.
        """
        if height <= 0:
            raise ValueError("Height must be a positive integer.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        
        pyramid = ""
        for row in range(1, height + 1):
            spaces = " " * (height - row)
            symbols = symbol * (2 * row - 1)
            pyramid += spaces + symbols + spaces + "\n"
        return pyramid


def main():
    """
    Main function to demonstrate the AsciiArt class.
    """
    art = AsciiArt()

    try:
        symbol = input("Enter the symbol to use for drawing: ")

        print("\nSquare:")
        print(art.draw_square(5, symbol))

        print("Rectangle:")
        print(art.draw_rectangle(7, 3, symbol))

        print("Circle:")
        print(art.draw_circle(7, symbol))  # Odd diameter for better symmetry

        print("Triangle:")
        print(art.draw_triangle(5, 8, symbol))
        
        print("Pyramid")
        print(art.draw_pyramid(5, symbol))

    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
