
import math
import string

class AsciiArt:
    """
    A class for generating ASCII art shapes. Provides methods to draw a square, rectangle,
    circle, right-angled triangle, and a symmetrical pyramid. Each shape is completely filled
    with a user-provided single printable symbol.
    """

    @staticmethod
    def _validate_positive_int(value: int, name: str):
        """
        Validates that a value is a positive integer.

        :param value: The value to check.
        :param name: The parameter name (for error messages).
        :raises ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int) or value <= 0:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str):
        """
        Validates that the symbol is a single printable character.

        :param symbol: The symbol to check.
        :raises ValueError: If symbol is not a single printable character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a square completely filled with the specified symbol.

        :param width: The side length of the square.
        :param symbol: The character used to fill the square.
        :return: A multi-line string representing the square.
        :raises ValueError: If width is not a positive integer or symbol is invalid.
        """
        AsciiArt._validate_positive_int(width, "width")
        AsciiArt._validate_symbol(symbol)

        lines = [symbol * width for _ in range(width)]
        return "\n".join(lines)

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle completely filled with the specified symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The character used to fill the rectangle.
        :return: A multi-line string representing the rectangle.
        :raises ValueError: If width or height is not a positive integer or symbol is invalid.
        """
        AsciiArt._validate_positive_int(width, "width")
        AsciiArt._validate_positive_int(height, "height")
        AsciiArt._validate_symbol(symbol)

        lines = [symbol * width for _ in range(height)]
        return "\n".join(lines)

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle using ASCII characters.

        :param diameter: The diameter of the circle.
        :param symbol: The character used to fill the circle.
        :return: A multi-line string representing the circle.
        :raises ValueError: If diameter is not a positive integer or symbol is invalid.
        """
        AsciiArt._validate_positive_int(diameter, "diameter")
        AsciiArt._validate_symbol(symbol)

        # Center the circle in a grid of size 'diameter x diameter'
        center = (diameter - 1) / 2
        radius = diameter / 2

        lines = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Calculate the Euclidean distance from (x, y) to the center.
                distance = math.sqrt((x - center) ** 2 + (y - center) ** 2)
                # Fill the point if it lies within the circle's radius.
                if distance <= radius:
                    line += symbol
                else:
                    line += " "
            lines.append(line)
        return "\n".join(lines)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle completely filled with the specified symbol.
        The right angle is positioned at the bottom left, with the base having 'width' characters.

        :param width: The desired base width of the triangle.
        :param height: The height (number of rows) of the triangle.
        :param symbol: The character used to fill the triangle.
        :return: A multi-line string representing the triangle.
        :raises ValueError: If width or height is not a positive integer or symbol is invalid.
        """
        AsciiArt._validate_positive_int(width, "width")
        AsciiArt._validate_positive_int(height, "height")
        AsciiArt._validate_symbol(symbol)

        lines = []
        for i in range(1, height + 1):
            # Scale the number of symbols proportionally from 1 up to 'width'.
            count = math.ceil((i / height) * width)
            count = max(1, count)
            lines.append(symbol * count)
        return "\n".join(lines)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid completely filled with the specified symbol.

        :param height: The number of rows the pyramid consists of.
        :param symbol: The character used to fill the pyramid.
        :return: A multi-line string representing the pyramid.
        :raises ValueError: If height is not a positive integer or symbol is invalid.
        """
        AsciiArt._validate_positive_int(height, "height")
        AsciiArt._validate_symbol(symbol)

        lines = []
        # The base of the pyramid will have (2 * height - 1) symbols.
        base_width = 2 * height - 1
        for i in range(height):
            num_symbols = 2 * i + 1
            spaces = (base_width - num_symbols) // 2
            line = " " * spaces + symbol * num_symbols
            lines.append(line)
        return "\n".join(lines)


def main():
    """
    Runs the console-based ASCII Art application.
    Provides an interactive menu for choosing a shape and supplying input parameters.
    """
    art = AsciiArt()

    menu = (
        "\nASCII Art Generator Menu:\n"
        "1. Draw Square\n"
        "2. Draw Rectangle\n"
        "3. Draw Circle\n"
        "4. Draw Right-Angled Triangle\n"
        "5. Draw Pyramid\n"
        "6. Exit\n"
        "Enter your choice (1-6): "
    )

    while True:
        try:
            choice = input(menu).strip()
            if choice == '1':
                width = int(input("Enter the side length of the square: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = art.draw_square(width, symbol)
            elif choice == '2':
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = art.draw_rectangle(width, height, symbol)
            elif choice == '3':
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = art.draw_circle(diameter, symbol)
            elif choice == '4':
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = art.draw_triangle(width, height, symbol)
            elif choice == '5':
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter a single printable symbol: ").strip()
                result = art.draw_pyramid(height, symbol)
            elif choice == '6':
                print("Exiting the ASCII Art Generator. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                continue

            print("\nGenerated ASCII Art:\n")
            print(result)

        except ValueError as ve:
            print(f"Input error: {ve}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
