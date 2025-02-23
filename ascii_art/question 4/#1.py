
import math

class AsciiArt:
    """
    A class that provides methods for generating 2D ASCII art shapes.
    Each method returns a multi-line string representing the shape.
    """

    @staticmethod
    def _validate_dimension(value: int, name: str) -> None:
        """
        Validates that a given dimension is a positive integer.

        :param value: The value to validate.
        :param name: Name of the dimension (for error messages).
        :raises ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a single printable character.

        :param symbol: The symbol provided by the user.
        :raises ValueError: If the symbol is not exactly one printable character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a filled square with a given side length and symbol.

        :param width: The length of each side of the square (positive integer).
        :param symbol: The symbol used to draw the square (single printable character).
        :return: A multi-line string representing the square.
        :raises ValueError: If any parameter is invalid.
        """
        cls._validate_dimension(width, "Width")
        cls._validate_symbol(symbol)
        
        # Build the square row by row.
        return "\n".join([symbol * width for _ in range(width)])

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle given its width, height, and drawing symbol.

        :param width: Width of the rectangle (positive integer).
        :param height: Height of the rectangle (positive integer).
        :param symbol: The symbol used to draw the rectangle (single printable character).
        :return: A multi-line string representing the rectangle.
        :raises ValueError: If any parameter is invalid.
        """
        cls._validate_dimension(width, "Width")
        cls._validate_dimension(height, "Height")
        cls._validate_symbol(symbol)
        
        return "\n".join([symbol * width for _ in range(height)])

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle of a given diameter using the specified symbol.
        The algorithm checks each point against the circle equation.

        :param diameter: The diameter of the circle (positive integer).
        :param symbol: The symbol used to draw the circle (single printable character).
        :return: A multi-line string representing the filled circle.
        :raises ValueError: If any parameter is invalid.
        """
        cls._validate_dimension(diameter, "Diameter")
        cls._validate_symbol(symbol)

        radius = diameter / 2
        center = (diameter - 1) / 2
        rows = []
        for i in range(diameter):
            row_chars = []
            for j in range(diameter):
                # Check if the point is inside the circle equation.
                if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
                    row_chars.append(symbol)
                else:
                    row_chars.append(" ")
            rows.append("".join(row_chars))
        return "\n".join(rows)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle whose right angle is at the bottom-left.
        The number of symbols in each row is determined via linear interpolation
        so that the bottom row contains 'width' symbols and the top row contains 1 symbol.

        :param width: The base width of the triangle (positive integer).
        :param height: The height (number of rows) of the triangle (positive integer).
        :param symbol: The symbol used to draw the triangle (single printable character).
        :return: A multi-line string representing the triangle.
        :raises ValueError: If any parameter is invalid.
        """
        cls._validate_dimension(width, "Width")
        cls._validate_dimension(height, "Height")
        cls._validate_symbol(symbol)

        # Handle the special case when there is only one row.
        if height == 1:
            return symbol * width

        rows = []
        # Use linear interpolation so that:
        #   when i == 1, count = 1 and when i == height, count = width.
        for i in range(1, height + 1):
            count = int((i - 1) * (width - 1) / (height - 1)) + 1
            rows.append(symbol * count)
        return "\n".join(rows)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a filled, symmetrical pyramid with a given height.
        The pyramid's base width is computed as (2 * height - 1) to ensure symmetry.

        :param height: The height of the pyramid (positive integer).
        :param symbol: The symbol used to draw the pyramid (single printable character).
        :return: A multi-line string representing the pyramid.
        :raises ValueError: If any parameter is invalid.
        """
        cls._validate_dimension(height, "Height")
        cls._validate_symbol(symbol)

        rows = []
        base_width = 2 * height - 1
        for i in range(height):
            num_symbols = 2 * i + 1
            left_padding = (base_width - num_symbols) // 2
            row = (" " * left_padding) + (symbol * num_symbols)
            rows.append(row)
        return "\n".join(rows)


def main():
    """
    Main function to run the console-based 2D ASCII Art App.
    Allows the user to select a shape, input dimensions and symbol, and then displays the ASCII art.
    """
    print("Welcome to the 2D ASCII Art App!")
    while True:
        print("\nPlease choose an option:")
        print("1. Draw Square")
        print("2. Draw Rectangle")
        print("3. Draw Circle")
        print("4. Draw Triangle (Right-angled)")
        print("5. Draw Pyramid")
        print("0. Exit")

        choice = input("Enter your choice (0-5): ").strip()
        if choice == "0":
            print("Thank you for using the 2D ASCII Art App. Goodbye!")
            break

        try:
            if choice == "1":
                width = int(input("Enter the side length of the square: ").strip())
                symbol = input("Enter the drawing symbol (single character): ").strip()
                result = AsciiArt.draw_square(width, symbol)
            elif choice == "2":
                width = int(input("Enter the width of the rectangle: ").strip())
                height = int(input("Enter the height of the rectangle: ").strip())
                symbol = input("Enter the drawing symbol (single character): ").strip()
                result = AsciiArt.draw_rectangle(width, height, symbol)
            elif choice == "3":
                diameter = int(input("Enter the diameter of the circle: ").strip())
                symbol = input("Enter the drawing symbol (single character): ").strip()
                result = AsciiArt.draw_circle(diameter, symbol)
            elif choice == "4":
                width = int(input("Enter the base width of the triangle: ").strip())
                height = int(input("Enter the height of the triangle: ").strip())
                symbol = input("Enter the drawing symbol (single character): ").strip()
                result = AsciiArt.draw_triangle(width, height, symbol)
            elif choice == "5":
                height = int(input("Enter the height of the pyramid: ").strip())
                symbol = input("Enter the drawing symbol (single character): ").strip()
                result = AsciiArt.draw_pyramid(height, symbol)
            else:
                print("Invalid choice. Please try again.")
                continue

            print("\n" + result)
        except ValueError as ve:
            print(f"Error: {ve}")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")


if __name__ == "__main__":
    main()
