
import math


class AsciiArt:
    """
    A class for generating 2D ASCII art shapes.

    Methods:
        draw_square(width: int, symbol: str) -> str
        draw_rectangle(width: int, height: int, symbol: str) -> str
        draw_circle(diameter: int, symbol: str) -> str
        draw_triangle(width: int, height: int, symbol: str) -> str
        draw_pyramid(height: int, symbol: str) -> str
    """

    @staticmethod
    def _validate_positive_int(value: int, name: str) -> None:
        """Validate that the given value is a positive integer."""
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """Validate that the symbol is a single printable character."""
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a filled square.

        Parameters:
            width (int): The number of symbols per side.
            symbol (str): The printable symbol to fill the square.

        Returns:
            str: A multiline string representing the square.
        """
        self._validate_positive_int(width, "Width")
        self._validate_symbol(symbol)

        # Generate each line of the square
        lines = [symbol * width for _ in range(width)]
        return "\n".join(lines)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle.

        Parameters:
            width (int): The number of symbols in each row.
            height (int): The number of rows.
            symbol (str): The printable symbol to fill the rectangle.

        Returns:
            str: A multiline string representing the rectangle.
        """
        self._validate_positive_int(width, "Width")
        self._validate_positive_int(height, "Height")
        self._validate_symbol(symbol)

        lines = [symbol * width for _ in range(height)]
        return "\n".join(lines)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle using the midpoint circle algorithm.

        Parameters:
            diameter (int): The diameter of the circle.
            symbol (str): The printable symbol to fill the circle.

        Returns:
            str: A multiline string representing the circle.
        """
        self._validate_positive_int(diameter, "Diameter")
        self._validate_symbol(symbol)

        radius = diameter / 2.0
        center = (diameter - 1) / 2.0  # Center coordinate for both x and y
        lines = []

        # Iterate over each row and column of the bounding box
        for y in range(diameter):
            line_chars = []
            for x in range(diameter):
                # Compute Euclidean distance from the center
                if (x - center) ** 2 + (y - center) ** 2 <= radius ** 2:
                    line_chars.append(symbol)
                else:
                    line_chars.append(" ")
            lines.append("".join(line_chars))
        return "\n".join(lines)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled filled triangle.

        The triangle will have 'height' rows, and the last row will have 'width' symbols.
        Each row's symbol count is approximated proportionally to ensure a right angle at the bottom-left.

        Parameters:
            width (int): The number of symbols at the base of the triangle.
            height (int): The number of rows.
            symbol (str): The printable symbol to fill the triangle.

        Returns:
            str: A multiline string representing the triangle.
        """
        self._validate_positive_int(width, "Width")
        self._validate_positive_int(height, "Height")
        self._validate_symbol(symbol)

        lines = []
        for row in range(height):
            # Compute number of symbols for this row (ensuring the last row equals width)
            # Using math.ceil to guarantee at least one symbol per row.
            symbols_count = math.ceil((row + 1) * width / height)
            # Ensure that the final row has exactly 'width' symbols
            if row == height - 1:
                symbols_count = width
            lines.append(symbol * symbols_count)
        return "\n".join(lines)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetrical filled pyramid.

        Each row is centered by padding with spaces. The base of the pyramid has width (2*height - 1).

        Parameters:
            height (int): The number of rows in the pyramid.
            symbol (str): The printable symbol to fill the pyramid.

        Returns:
            str: A multiline string representing the pyramid.
        """
        self._validate_positive_int(height, "Height")
        self._validate_symbol(symbol)

        lines = []
        for row in range(height):
            # Compute the number of symbol characters in this row.
            symbol_count = 2 * row + 1
            # Compute left padding for centering
            padding = height - row - 1
            line = " " * padding + symbol * symbol_count
            lines.append(line)
        return "\n".join(lines)


def main():
    """
    Console-based interface to select and draw ASCII art shapes.
    """
    ascii_art = AsciiArt()

    menu = (
        "\nSelect shape to draw:\n"
        "1: Square\n"
        "2: Rectangle\n"
        "3: Circle\n"
        "4: Triangle (right-angled)\n"
        "5: Pyramid\n"
        "q: Quit\n"
    )

    while True:
        print(menu)
        choice = input("Enter your choice (1/2/3/4/5/q): ").strip().lower()

        if choice == "q":
            print("Goodbye!")
            break

        try:
            if choice == "1":
                width = int(input("Enter the width of the square: "))
                symbol = input("Enter the symbol to use: ")
                art = ascii_art.draw_square(width, symbol)
            elif choice == "2":
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter the symbol to use: ")
                art = ascii_art.draw_rectangle(width, height, symbol)
            elif choice == "3":
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter the symbol to use: ")
                art = ascii_art.draw_circle(diameter, symbol)
            elif choice == "4":
                base = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter the symbol to use: ")
                art = ascii_art.draw_triangle(base, height, symbol)
            elif choice == "5":
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter the symbol to use: ")
                art = ascii_art.draw_pyramid(height, symbol)
            else:
                print("Invalid choice. Please try again.")
                continue

            # Print the generated ASCII art.
            print("\n" + art + "\n")

        except ValueError as ve:
            print("Input error:", ve)
        except Exception as e:
            print("An unexpected error occurred:", e)


if __name__ == "__main__":
    main()
