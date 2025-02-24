class AsciiArt:
    """
    A class for generating various ASCII art shapes.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.

        Args:
            width: The width (and height) of the square.
            symbol: The character to use for drawing the square.

        Returns:
            A string representing the ASCII art square.  Returns an empty
            string if input is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            print("Error: Width must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            print("Error: Symbol must be a single printable character.")
            return ""

        square = ""
        for _ in range(width):
            square += symbol * width + "\n"
        return square

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            symbol: The character to use for drawing.

        Returns:
            A string representing the ASCII art rectangle. Returns an empty
            string if input is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            print("Error: Width must be a positive integer.")
            return ""
        if not isinstance(height, int) or height <= 0:
            print("Error: Height must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            print("Error: Symbol must be a single printable character.")
            return ""

        rectangle = ""
        for _ in range(height):
            rectangle += symbol * width + "\n"
        return rectangle

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.

        Args:
            diameter: The diameter of the circle.
            symbol: The character to use for drawing.

        Returns:
            A string representing the ASCII art circle. Returns an empty
            string if input is invalid.
        """
        if not isinstance(diameter, int) or diameter <= 0:
            print("Error: Diameter must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            print("Error: Symbol must be a single printable character.")
            return ""

        radius = diameter // 2
        circle = ""
        for y in range(-radius, radius + 1):
            line = ""
            for x in range(-radius, radius + 1):
                distance = (x * x + y * y) ** 0.5
                if distance <= radius + 0.5:  # Add a small tolerance
                    line += symbol
                else:
                    line += " "  # Use space for outside the circle
            circle += line + "\n"
        return circle

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle.

        Args:
            width: The width of the triangle's base.
            height: The height of the triangle.
            symbol: The character to use.

        Returns:
            A string representing the ASCII art triangle. Returns an empty
            string if input is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            print("Error: Width must be a positive integer.")
            return ""
        if not isinstance(height, int) or height <= 0:
            print("Error: Height must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            print("Error: Symbol must be a single printable character.")
            return ""
        
        triangle = ""
        for row in range(1, height+1):
            num_symbols = int(row * (width / height))
            if num_symbols > 0:
                triangle += symbol * num_symbols + "\n"
            else:
                triangle += "\n" # Necessary to keep the correct form of triangle in case of float numbers rounding

        return triangle

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid.

        Args:
            height: The height of the pyramid.
            symbol: The character to use.

        Returns:
            A string representing the ASCII art pyramid.  Returns an empty
            string if input is invalid.
        """
        if not isinstance(height, int) or height <= 0:
            print("Error: Height must be a positive integer.")
            return ""
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            print("Error: Symbol must be a single printable character.")
            return ""

        pyramid = ""
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            symbols = symbol * (2 * i - 1)
            pyramid += spaces + symbols + spaces + "\n"
        return pyramid
def main():
    """
    Main function to demonstrate the AsciiArt class.
    """
    art = AsciiArt()

    # Get user input with validation
    while True:
        try:
            width = int(input("Enter width for square/rectangle/triangle: "))
            height = int(input("Enter height for rectangle/triangle: "))
            diameter = int(input("Enter diameter for circle: "))
            pyramid_height = int(input("Enter height for pyramid: "))
            symbol = input("Enter a symbol to use: ")

            if len(symbol) != 1 or not symbol.isprintable():
              print("Invalid symbol. Please use a single, printable character")
              continue

            break # All input valid
        except ValueError:
            print("Invalid input. Please enter integers for dimensions.")


    # Draw and print the shapes
    print("\nSquare:")
    print(art.draw_square(width, symbol))

    print("\nRectangle:")
    print(art.draw_rectangle(width, height, symbol))

    print("\nCircle:")
    print(art.draw_circle(diameter, symbol))

    print("\nTriangle:")
    print(art.draw_triangle(width, height, symbol))

    print("\nPyramid:")
    print(art.draw_pyramid(pyramid_height, symbol))


if __name__ == "__main__":
    main()

