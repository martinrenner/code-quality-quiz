
class AsciiArt:
    """
    A class for generating various ASCII art shapes.

    This class provides methods to draw squares, rectangles,
    approximate circles, right-angled triangles, and pyramids
    using a specified symbol.  It emphasizes code quality,
    efficiency, and adherence to good coding practices.
    """

    def __init__(self):
        pass # currently no initialization required

    def _validate_input(self, dimensions, symbol):
        """
        Validates the input parameters for shape drawing functions.

        Args:
            dimensions (list of int): A list of integer dimensions (width, height, etc.).
            symbol (str): The character to use for drawing the shape.

        Raises:
            TypeError: If dimensions are not integers or symbol is not a string.
            ValueError: If dimensions are not positive or symbol is not a single character.
        """
        if not all(isinstance(dim, int) for dim in dimensions):
            raise TypeError("All dimensions must be integers.")
        if not all(dim > 0 for dim in dimensions):
            raise ValueError("All dimensions must be positive.")
        if not isinstance(symbol, str):
            raise TypeError("Symbol must be a string.")
        if len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")
        if not symbol.isprintable(): # Check it's printable.
            raise ValueError("Symbol must be a printable character.")


    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a filled square of the given width using the specified symbol.

        Args:
            width (int): The width (and height) of the square.
            symbol (str): The character to use for drawing the square.

        Returns:
            str: A multi-line string representing the ASCII art square.

        Raises:
            TypeError: If input types are invalid.
            ValueError: If input values are invalid.
        """
        self._validate_input([width], symbol)  # Validate inputs
        return "\n".join([symbol * width] * width)


    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle of the given dimensions using the specified symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to use.

        Returns:
            str: A multi-line string representing the ASCII art rectangle.

        Raises:
            TypeError: If input types are invalid.
            ValueError: If input values are invalid.
        """
        self._validate_input([width, height], symbol)
        return "\n".join([symbol * width] * height)


    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle using the specified symbol.

        The circle is approximated by checking the distance of each point
        from the center and drawing the symbol if the distance is within
        the radius.  This creates a filled circle.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use.

        Returns:
            str: A multi-line string representing the approximate ASCII art circle.

        Raises:
            TypeError: If input types are invalid.
            ValueError: If input values are invalid.
        """
        self._validate_input([diameter], symbol)
        radius = diameter / 2
        lines = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Calculate distance from center
                dist_x = x - (radius - 0.5)  # Offset by 0.5 for visual centering
                dist_y = y - (radius - 0.5)
                distance_from_center = (dist_x**2 + dist_y**2)**0.5

                # Draw symbol if within the radius (with tolerance for rounding)
                if distance_from_center <= radius + 0.5 : # Additional tolerance
                   line += symbol
                else:
                    line += " " # Space for outside the circle.
            lines.append(line)
        return "\n".join(lines)


    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle.

        Args:
            width (int):  The width of the base of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to use.

        Returns:
            str: Multi-line string: ASCII art triangle.

        Raises:
            TypeError: If input types are invalid.
            ValueError: If input values are invalid.
        """
        self._validate_input([width, height], symbol)
        lines = []
        for row in range(height):
            # Calculate the number of symbols to draw in this row,
            # scaled by the row number and height.
            num_symbols = int((row + 1) / height * width)
            num_symbols = max(1, num_symbols)   # Ensure at least one symbol per row
            lines.append(symbol * num_symbols)
        return "\n".join(lines)


    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a filled symmetrical pyramid using specified symbol.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use.

        Returns:
            str: A multi-line string representing the ASCII art pyramid.

        Raises:
            TypeError: If input types are invalid.
            ValueError: If input values are invalid.
        """
        self._validate_input([height], symbol)
        lines = []
        for row in range(height):
            # Calculate leading spaces and number of symbols for each row
            spaces = " " * (height - row - 1)
            symbols = symbol * (2 * row + 1)
            lines.append(spaces + symbols)
        return "\n".join(lines)



def main():
    """
    Main function to demonstrate the AsciiArt class.
    """
    art_generator = AsciiArt()

    try:
        # Get user input for shape and symbol
        shape_choice = input("Enter shape (square, rectangle, circle, triangle, pyramid): ").lower()
        symbol = input("Enter the symbol to use: ")

        # Draw the chosen shape based on user input
        if shape_choice == "square":
            width = int(input("Enter width: "))
            print(art_generator.draw_square(width, symbol))
        elif shape_choice == "rectangle":
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            print(art_generator.draw_rectangle(width, height, symbol))
        elif shape_choice == "circle":
            diameter = int(input("Enter diameter: "))
            print(art_generator.draw_circle(diameter, symbol))
        elif shape_choice == "triangle":
            width = int(input("Enter width: "))
            height = int(input("Enter height: "))
            print(art_generator.draw_triangle(width, height, symbol))
        elif shape_choice == "pyramid":
            height = int(input("Enter height: "))
            print(art_generator.draw_pyramid(height, symbol))
        else:
            print("Invalid shape choice.")

    except (ValueError, TypeError) as e:
        print(f"Error: {e}")  # Handle input errors gracefully
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

