import math

class AsciiArt:
    """
    A class that provides methods to generate 2D ASCII art shapes.
    """

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a completely filled square of given width using the specified symbol.

        Args:
            width (int): The number of characters per side of the square.
            symbol (str): A single printable character used to draw the square.

        Returns:
            str: A multi-line string representing the square.

        Raises:
            ValueError: If width is not a positive integer or symbol is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single, printable character.")

        # Build each row of the square
        rows = [symbol * width for _ in range(width)]
        return "\n".join(rows)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a completely filled rectangle using the specified dimensions and symbol.

        Args:
            width (int): The number of characters in each row.
            height (int): The number of rows.
            symbol (str): A single printable character used to draw the rectangle.

        Returns:
            str: A multi-line string representing the rectangle.

        Raises:
            ValueError: If width or height is not a positive integer or symbol is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single, printable character.")

        # Build each row of the rectangle
        rows = [symbol * width for _ in range(height)]
        return "\n".join(rows)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate completely filled circle of the given diameter using the specified symbol.

        The drawing is based on the circle equation and may not be perfect due to the limitations of ASCII art.

        Args:
            diameter (int): The approximate diameter of the circle in characters.
            symbol (str): A single printable character used to draw the circle.

        Returns:
            str: A multi-line string representing the approximate circle.

        Raises:
            ValueError: If diameter is not a positive integer or symbol is invalid.
        """
        if not isinstance(diameter, int) or diameter <= 0:
            raise ValueError("Diameter must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single, printable character.")

        radius = diameter / 2.0
        result = []

        # Iterate over rows and columns, using circle equation for approximation.
        for y in range(diameter):
            row = ""
            for x in range(diameter):
                # Adjust x and y relative to the center. Using 0.5 offset for better centering.
                if ((x - radius + 0.5) ** 2 + (y - radius + 0.5) ** 2) <= (radius ** 2):
                    row += symbol
                else:
                    row += " "
            result.append(row.rstrip())
        return "\n".join(result)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a completely filled right-angled triangle with the right angle at the bottom left.
        The triangle scales the number of symbols in each row such that the base has 'width' symbols
        and there are 'height' rows.

        Args:
            width (int): The number of symbols in the base row.
            height (int): The number of rows (height of the triangle).
            symbol (str): A single printable character used to draw the triangle.

        Returns:
            str: A multi-line string representing the triangle.

        Raises:
            ValueError: If width or height is not a positive integer or symbol is invalid.
        """
        if not isinstance(width, int) or width <= 0:
            raise ValueError("Width must be a positive integer.")
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single, printable character.")

        rows = []
        # Generate each row with a proportional number of symbols.
        for row in range(1, height + 1):
            # Calculate the number of symbols for the current row.
            # Use math.ceil to ensure at least one symbol is printed.
            count = math.ceil(row * width / height)
            rows.append(symbol * count)
        return "\n".join(rows)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a completely filled symmetrical pyramid centered horizontally.
        The pyramid has 'height' rows and the base width is (2 * height - 1).

        Args:
            height (int): The number of rows in the pyramid.
            symbol (str): A single printable character used to draw the pyramid.

        Returns:
            str: A multi-line string representing the pyramid.

        Raises:
            ValueError: If height is not a positive integer or symbol is invalid.
        """
        if not isinstance(height, int) or height <= 0:
            raise ValueError("Height must be a positive integer.")
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single, printable character.")

        rows = []
        base_width = 2 * height - 1
        for i in range(height):
            symbol_count = 2 * i + 1
            spaces = (base_width - symbol_count) // 2
            row = " " * spaces + symbol * symbol_count + " " * spaces
            rows.append(row.rstrip())
        return "\n".join(rows)


def main():
    """
    Main function to run the console-based 2D ASCII ART application.
    Provides an interactive menu for the user to choose a shape and input parameters.
    """
    art = AsciiArt()

    menu = """
Choose a shape to draw:
1. Square
2. Rectangle
3. Circle
4. Right-Angled Triangle
5. Pyramid
q. Quit
Enter your choice: """

    while True:
        choice = input(menu).strip().lower()
        if choice == 'q':
            print("Goodbye!")
            break

        try:
            if choice == '1':
                width = int(input("Enter the side length of the square: "))
                symbol = input("Enter the drawing symbol (single character): ")
                result = art.draw_square(width, symbol)
            elif choice == '2':
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter the drawing symbol (single character): ")
                result = art.draw_rectangle(width, height, symbol)
            elif choice == '3':
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter the drawing symbol (single character): ")
                result = art.draw_circle(diameter, symbol)
            elif choice == '4':
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter the drawing symbol (single character): ")
                result = art.draw_triangle(width, height, symbol)
            elif choice == '5':
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter the drawing symbol (single character): ")
                result = art.draw_pyramid(height, symbol)
            else:
                print("Invalid selection. Please choose a valid option.")
                continue

            print("\nHere is your ASCII art:\n")
            print(result)
            print("\n" + "=" * 40 + "\n")
        except ValueError as ve:
            print(f"Input error: {ve}\nPlease try again.\n")
        except Exception as e:
            print(f"An unexpected error occurred: {e}\nPlease try again.\n")


if __name__ == "__main__":
    main()
