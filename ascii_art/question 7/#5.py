"""
ASCII Art Application
---------------------
This console-based application enables users to generate various 2D ASCII art shapes.
It implements functions to draw a square, rectangle, circle (approximate),
right-angled triangle, and symmetrical pyramid using a user-defined filling symbol.

Each function performs input validation to ensure dimensions are positive integers
and that the provided symbol is a single character.

The application uses clean architecture principles with modular, testable, and
well-documented code. The design adheres to best practices for maintainability and
efficiency.
"""

class AsciiArt:
    @staticmethod
    def _validate_dimension(value: int, name: str = "Dimension") -> None:
        """
        Validates that a dimension value is a positive integer.

        Args:
            value (int): The dimension value.
            name (str): A descriptive name for the value (e.g., "Width", "Height").

        Raises:
            ValueError: If value is not a positive integer.
        """
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a non-empty string of length 1.

        Args:
            symbol (str): The symbol to validate.

        Raises:
            ValueError: If the symbol is not exactly one character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character.")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a filled square of the specified width using the given symbol.

        Args:
            width (int): The width (and height) of the square in characters.
            symbol (str): The filling symbol (must be a single character).

        Returns:
            str: A multi-line string representing the square.
        """
        cls._validate_dimension(width, "Width")
        cls._validate_symbol(symbol)

        lines = [symbol * width for _ in range(width)]
        return "\n".join(lines)

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle using the specified dimensions and symbol.

        Args:
            width (int): The width of the rectangle in characters.
            height (int): The height of the rectangle in characters.
            symbol (str): The filling symbol (must be a single character).

        Returns:
            str: A multi-line string representing the rectangle.
        """
        cls._validate_dimension(width, "Width")
        cls._validate_dimension(height, "Height")
        cls._validate_symbol(symbol)

        lines = [symbol * width for _ in range(height)]
        return "\n".join(lines)

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle using the specified diameter and symbol.

        The algorithm uses the circle equation to decide if a coordinate lies
        inside the circle area. The circle is centered in a square of side 'diameter'.

        Args:
            diameter (int): The diameter of the circle (also the output grid size).
            symbol (str): The filling symbol (must be a single character).

        Returns:
            str: A multi-line string representing the filled circle.
        """
        cls._validate_dimension(diameter, "Diameter")
        cls._validate_symbol(symbol)

        lines = []
        center = (diameter - 1) / 2
        radius = diameter / 2

        for i in range(diameter):
            line = ""
            for j in range(diameter):
                # Use the circle equation: (x - center_x)^2 + (y - center_y)^2 <= radius^2
                if (i - center) ** 2 + (j - center) ** 2 <= radius ** 2:
                    line += symbol
                else:
                    line += " "
            lines.append(line)
        return "\n".join(lines)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle with the right angle at the bottom-left.

        The triangle is scaled so that the bottom row has exactly 'width' symbols,
        and the triangle spans 'height' rows. The number of symbols in each row is 
        calculated by scaling the row number relative to the total height.

        Args:
            width (int): The target width of the triangle's base.
            height (int): The height of the triangle in rows.
            symbol (str): The filling symbol (must be a single character).

        Returns:
            str: A multi-line string representing the triangle.
        """
        cls._validate_dimension(width, "Width")
        cls._validate_dimension(height, "Height")
        cls._validate_symbol(symbol)

        lines = []
        for i in range(1, height + 1):
            # Scale the number of symbols relative to the current row.
            num_symbols = max(1, round((i / height) * width))
            lines.append(symbol * num_symbols)
        return "\n".join(lines)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a filled, symmetrical pyramid with the specified height.

        The pyramid's base width is (2 * height - 1) and it is centered using spaces.

        Args:
            height (int): The number of rows (height) of the pyramid.
            symbol (str): The filling symbol (must be a single character).

        Returns:
            str: A multi-line string representing the pyramid.
        """
        cls._validate_dimension(height, "Height")
        cls._validate_symbol(symbol)

        lines = []
        for i in range(height):
            num_symbols = 2 * i + 1
            num_spaces = height - i - 1
            # Center the symbols by padding with spaces on both sides.
            line = " " * num_spaces + symbol * num_symbols + " " * num_spaces
            lines.append(line)
        return "\n".join(lines)


def main():
    """
    Main function for the ASCII Art console application.
    
    Provides a menu-based interface for the user to select a shape, enter its
    dimensions and the filling symbol, and then displays the generated ASCII art.
    """
    art = AsciiArt()
    menu = """
Select a shape to draw:
1. Square
2. Rectangle
3. Circle
4. Triangle (right-angled)
5. Pyramid
0. Exit
Enter your choice: """

    while True:
        try:
            choice_input = input(menu)
            if not choice_input.strip():
                print("Please enter a valid option.")
                continue
            choice = int(choice_input)
        except ValueError:
            print("Invalid input. Please enter a number corresponding to the options.")
            continue

        if choice == 0:
            print("Exiting the application.")
            break

        try:
            if choice == 1:
                # Square: width and symbol
                width = int(input("Enter the width of the square: "))
                symbol = input("Enter a single character as the filling symbol: ")
                result = art.draw_square(width, symbol)
            elif choice == 2:
                # Rectangle: width, height and symbol
                width = int(input("Enter the width of the rectangle: "))
                height = int(input("Enter the height of the rectangle: "))
                symbol = input("Enter a single character as the filling symbol: ")
                result = art.draw_rectangle(width, height, symbol)
            elif choice == 3:
                # Circle: diameter and symbol
                diameter = int(input("Enter the diameter of the circle: "))
                symbol = input("Enter a single character as the filling symbol: ")
                result = art.draw_circle(diameter, symbol)
            elif choice == 4:
                # Triangle: width, height and symbol
                width = int(input("Enter the base width of the triangle: "))
                height = int(input("Enter the height of the triangle: "))
                symbol = input("Enter a single character as the filling symbol: ")
                result = art.draw_triangle(width, height, symbol)
            elif choice == 5:
                # Pyramid: height and symbol
                height = int(input("Enter the height of the pyramid: "))
                symbol = input("Enter a single character as the filling symbol: ")
                result = art.draw_pyramid(height, symbol)
            else:
                print("Invalid choice. Please select a valid option.")
                continue

            print("\n" + result + "\n")
        except ValueError as error:
            print(f"Error: {error}")
        except Exception as exc:
            print(f"An unexpected error occurred: {exc}")


if __name__ == "__main__":
    main()
