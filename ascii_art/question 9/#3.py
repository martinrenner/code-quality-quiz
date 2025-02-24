import math

class AsciiArt:
    """
    A class for generating ASCII art shapes.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.

        Args:
            width: The width (and height) of the square.
            symbol: The character to use for drawing the square.

        Returns:
            A multi-line string representing the ASCII art square.

        Raises:
            ValueError: If width is not positive or symbol is not a single character.
        """
        self._validate_inputs(width, symbol, width)  # Height is same as width
        return "\n".join([symbol * width for _ in range(width)])

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.

        Args:
            width: The width of the rectangle.
            height: The height of the rectangle.
            symbol: The character to use for drawing.

        Returns:
            A multi-line string representing the ASCII art rectangle.

        Raises:
            ValueError: If width or height are not positive, or symbol is invalid.
        """
        self._validate_inputs(width, symbol, height)
        return "\n".join([symbol * width for _ in range(height)])
    
    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.

        Args:
            diameter: The diameter of the circle.
            symbol: The character to use for drawing.

        Returns:
            A multi-line string representing the ASCII art circle.

        Raises:
            ValueError: If diameter is not positive or symbol is invalid.
        """
        self._validate_inputs(diameter, symbol, diameter) #Width and Height same as the diameter
        radius = diameter / 2
        result = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Calculate distance from the center of the circle
                dist_x = x - radius + 0.5  # +0.5 for better visual centering
                dist_y = y - radius + 0.5
                distance = math.sqrt(dist_x**2 + dist_y**2)

                # Check if the point is within the circle's radius
                if distance <= radius:
                    line += symbol
                else:
                    line += " "  # Use space for the background
            result.append(line)
        return "\n".join(result)
    
    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.

        Args:
            width: The width of the triangle's base.
            height: The height of the triangle.
            symbol: The character to use.

        Returns:
            A multi-line string representing the ASCII art triangle.

        Raises:
            ValueError: If width or height are not positive, or symbol is invalid.
        """
        self._validate_inputs(width, symbol, height)
        result = []
        for y in range(height):
            # Calculate the number of symbols to draw on this row
            num_symbols = int((y + 1) * (width / height))
            line = symbol * num_symbols
            # Pad the line with empty spaces
            line = line.ljust(width)
            result.append(line)
        return "\n".join(result)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.

        Args:
            height: The height of the pyramid.
            symbol: The character to use.

        Returns:
            A multi-line string representing the ASCII art pyramid.

        Raises:
            ValueError: If height is not positive or symbol is invalid.
        """

        self._validate_inputs(height, symbol, height)  # Width will be derived from height
        result = []
        for y in range(height):
            # Calculate the number of symbols to draw for this row
            num_symbols = 2 * y + 1
            # Calculate the number of spaces to pad on each side
            num_spaces = height - y - 1
            line = " " * num_spaces + symbol * num_symbols + " " * num_spaces
            result.append(line)
        return "\n".join(result)

    def _validate_inputs(self, width: int,  symbol: str, height: int):
        """
        Validates the inputs for the drawing functions.  A private helper method.

        Args:
            width: the width of the shape.
            symbol: The character to use.
            height: the height of the shape

        Raises:
            ValueError: If inputs are invalid.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")    
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")


# Example Usage (and informal testing):

art_generator = AsciiArt()

try:
    square = art_generator.draw_square(5, "#")
    print("Square:\n", square)

    rectangle = art_generator.draw_rectangle(10, 3, "*")
    print("\nRectangle:\n", rectangle)

    circle = art_generator.draw_circle(7, "O")
    print("\nCircle:\n", circle)

    triangle = art_generator.draw_triangle(7, 5, "+")
    print("\nTriangle:\n", triangle)
    
    pyramid = art_generator.draw_pyramid(6, "X")
    print("\nPyramid:\n", pyramid)

    # Example of invalid input:
    # invalid_square = art_generator.draw_square(-5, "#")  # This will raise a ValueError
    # invalid_symbol = art_generator.draw_square(5, "##")  # This will raise a ValueError

except ValueError as e:
    print(f"Error: {e}")

# --- Testing Strategy (Formal Unit Tests would be in a separate file) ---
# 1.  Test each function (`draw_square`, `draw_rectangle`, etc.) individually.
# 2.  Test with various valid inputs:
#     - Small and large widths/heights/diameters.
#     - Different symbols (e.g., '#', '*', '.', 'X').
# 3.  Test with invalid inputs:
#     - Negative widths/heights/diameters.
#     - Zero width/height/diameter.
#     - Empty symbol.
#     - Multi-character symbols.
#     - Non-printable symbols.
# 4.  Visually inspect the output for correctness for the valid input cases.
# 5.  Verify that ValueErrors are raised appropriately for invalid input cases.
# The use of a testing framework like `pytest` would make this process much easier 
# and more automated.
