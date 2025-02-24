import math

class AsciiArt:
    """
    A class for generating 2D ASCII Art shapes.
    
    This class provides methods to draw filled shapes:
      - Square
      - Rectangle
      - Circle (approximate)
      - Right-angled triangle
      - Symmetrical pyramid

    Each method returns the ASCII art as a multi-line string.
    """

    @staticmethod
    def _validate_positive_integer(value: int, name: str) -> None:
        """
        Validates that the provided value is a positive integer.
        
        :param value: The integer value to validate.
        :param name: The name of the parameter (for error messages).
        :raises ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates the symbol to ensure it is a non-empty, printable string.
        
        :param symbol: The symbol to validate.
        :raises ValueError: If the symbol is empty or contains unprintable characters.
        """
        if not isinstance(symbol, str) or len(symbol) == 0:
            raise ValueError("Symbol must be a non-empty string.")
        if not symbol.isprintable():
            raise ValueError("Symbol must be a printable character.")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a filled ASCII square.

        :param width: The width (and height) of the square.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the square.
        """
        cls._validate_positive_integer(width, "width")
        cls._validate_symbol(symbol)
        # Create a list where each element is a row of 'symbol' repeated 'width' times.
        square_lines = [symbol * width for _ in range(width)]
        return "\n".join(square_lines)

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled ASCII rectangle.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the rectangle.
        """
        cls._validate_positive_integer(width, "width")
        cls._validate_positive_integer(height, "height")
        cls._validate_symbol(symbol)
        rectangle_lines = [symbol * width for _ in range(height)]
        return "\n".join(rectangle_lines)

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled ASCII circle.

        The algorithm uses the equation of a circle in a discrete grid.
        
        :param diameter: The approximate diameter of the circle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the circle.
        """
        cls._validate_positive_integer(diameter, "diameter")
        cls._validate_symbol(symbol)
        circle_lines = []
        # Define the center. Using (diameter - 1)/2 centers the circle in the grid.
        center = (diameter - 1) / 2
        radius = diameter / 2
        for i in range(diameter):
            line_chars = []
            for j in range(diameter):
                # Calculate the Euclidean distance from the current point to the center.
                distance = math.sqrt((j - center) ** 2 + (i - center) ** 2)
                if distance <= radius:
                    line_chars.append(symbol)
                else:
                    line_chars.append(" ")
            circle_lines.append("".join(line_chars))
        return "\n".join(circle_lines)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle with the right angle at the bottom left.

        The triangle's base has the specified width and progresses
        linearly to form the given height.

        :param width: The base width of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the triangle.
        """
        cls._validate_positive_integer(width, "width")
        cls._validate_positive_integer(height, "height")
        cls._validate_symbol(symbol)
        triangle_lines = []
        # For each row, determine the number of symbols by linear interpolation,
        # ensuring that the bottom row has exactly 'width' symbols.
        for i in range(height):
            num_symbols = max(1, math.ceil((i + 1) * width / height))
            triangle_lines.append(symbol * num_symbols)
        return "\n".join(triangle_lines)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a filled symmetrical pyramid.

        The pyramid is centered horizontally with a base width of (2*height - 1).

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the pyramid.
        """
        cls._validate_positive_integer(height, "height")
        cls._validate_symbol(symbol)
        pyramid_lines = []
        for i in range(height):
            num_symbols = 2 * i + 1
            num_spaces = height - i - 1  # Leading spaces to center the pyramid row.
            line = " " * num_spaces + symbol * num_symbols
            pyramid_lines.append(line)
        return "\n".join(pyramid_lines)


def main():
    """
    Main function to run the console-based ASCII Art application.
    
    Displays a simple menu to choose the shape and enter parameters.
    """
    print("Welcome to the ASCII Art Console Application!")
    art_generator = AsciiArt()

    menu = """
Please select a shape to draw:
  1. Square
  2. Rectangle
  3. Circle (approximate)
  4. Right-Angled Triangle
  5. Pyramid (Symmetrical)
  6. Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == "6":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                width = int(input("Enter the width of the square: "))
                symbol = input("Enter a printable symbol (e.g., *): ")
                result = art_generator.draw_square(width, symbol)
            elif choice == "2":
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter a printable symbol (e.g., #): ")
                result = art_generator.draw_rectangle(width, height, symbol)
            elif choice == "3":
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter a printable symbol (e.g., @): ")
                result = art_generator.draw_circle(diameter, symbol)
            elif choice == "4":
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter a printable symbol (e.g., +): ")
                result = art_generator.draw_triangle(width, height, symbol)
            elif choice == "5":
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter a printable symbol (e.g., ^): ")
                result = art_generator.draw_pyramid(height, symbol)
            else:
                print("Invalid choice. Please try again.")
                continue

            # Display the generated ASCII art.
            print("\nGenerated ASCII Art:")
            print(result)
            print("\n" + "-" * 40 + "\n")

        except ValueError as err:
            print(f"Input error: {err}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")


if __name__ == '__main__':
    main()
