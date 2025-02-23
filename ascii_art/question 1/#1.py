
"""
Console-Based 2D ASCII Art App

This application provides a console interface for drawing various 2D shapes in ASCII art.
It meets the ISO/IEC 25010 quality requirements by ensuring:
- Functionality: Supports drawing a square, rectangle, circle, right-angled triangle, and pyramid.
- Correctness: Uses precise geometric calculations to generate expected results.
- Performance: Uses efficient loops and minimal computations.
- Modularity: Organized into a class (AsciiArt) and helper functions.
- Security: Validates user inputs to prevent invalid parameters.
- Testability: Each drawing method returns a string, enabling easy unit testing.
- Readability & Documentation: Includes docstrings, clear variable names, and comments.

Author: Your Name
Date: YYYY-MM-DD
"""

import math


class AsciiArt:
    """
    A class for drawing ASCII art shapes.
    """

    @staticmethod
    def validate_dimension(value: int, name: str) -> None:
        """
        Validates that a dimension is a positive integer.

        :param value: The dimension value to validate.
        :param name: The name of the dimension parameter.
        :raises ValueError: If the value is not a positive integer.
        """
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a single printable character.

        :param symbol: The symbol to validate.
        :raises ValueError: If the symbol is not a single character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single printable character.")

    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draws a square of the given width filled with the chosen symbol.

        :param width: The width (and height) of the square.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the square in ASCII art.
        """
        self.validate_dimension(width, "Width")
        self.validate_symbol(symbol)
        line = symbol * width
        return "\n".join([line for _ in range(width)])

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle of the given width and height, filled with the chosen symbol.

        :param width: The width of the rectangle.
        :param height: The height of the rectangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the rectangle in ASCII art.
        """
        self.validate_dimension(width, "Width")
        self.validate_dimension(height, "Height")
        self.validate_symbol(symbol)
        line = symbol * width
        return "\n".join([line for _ in range(height)])

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle with the specified diameter and symbol.

        Uses the equation of a circle to decide if a point is within the circle's boundary.

        :param diameter: The diameter of the circle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the circle in ASCII art.
        """
        self.validate_dimension(diameter, "Diameter")
        self.validate_symbol(symbol)
        radius = diameter / 2
        center = (diameter - 1) / 2  # Center coordinate of the circle
        lines = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Calculate distance from the center of the circle.
                distance = math.sqrt((x - center) ** 2 + (y - center) ** 2)
                # Fill the point if it's within the circle's radius.
                if distance <= radius:
                    line += symbol
                else:
                    line += " "
            lines.append(line)
        return "\n".join(lines)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle with the given base width and height.

        The right angle is located at the bottom-left. The number of symbols per row
        increases proportionally from 1 to width.

        :param width: The base width of the triangle.
        :param height: The height of the triangle.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the triangle in ASCII art.
        """
        self.validate_dimension(width, "Width")
        self.validate_dimension(height, "Height")
        self.validate_symbol(symbol)
        lines = []
        for i in range(1, height + 1):
            # Calculate the proportional number of symbols for the current row.
            num_symbols = int(math.ceil(i * width / height))
            num_symbols = max(1, num_symbols)  # Ensure at least one symbol is drawn.
            lines.append(symbol * num_symbols)
        return "\n".join(lines)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draws a symmetric filled pyramid with the specified height, centered horizontally.

        Each row increases the number of symbols so that the bottom row has (2*height - 1) symbols.

        :param height: The height of the pyramid.
        :param symbol: The symbol to use for drawing.
        :return: A multi-line string representing the pyramid in ASCII art.
        """
        self.validate_dimension(height, "Height")
        self.validate_symbol(symbol)
        lines = []
        for i in range(height):
            num_spaces = height - i - 1
            num_symbols = 2 * i + 1
            lines.append(" " * num_spaces + symbol * num_symbols)
        return "\n".join(lines)


def get_positive_int(prompt: str) -> int:
    """
    Prompts the user to enter a positive integer.

    :param prompt: The prompt message.
    :return: A valid positive integer.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                raise ValueError
            return value
        except ValueError:
            print("Invalid input. Please enter a valid positive integer.")


def get_symbol(prompt: str) -> str:
    """
    Prompts the user to enter a single printable character as the symbol.

    :param prompt: The prompt message.
    :return: A single character string.
    """
    while True:
        symbol = input(prompt)
        if len(symbol) == 1:
            return symbol
        print("Invalid input. Please enter a single character.")


def main():
    """
    Main function for the ASCII Art App.
    
    Provides an interactive console interface for drawing shapes.
    """
    art = AsciiArt()
    shapes = {
        "1": ("Square", art.draw_square),
        "2": ("Rectangle", art.draw_rectangle),
        "3": ("Circle", art.draw_circle),
        "4": ("Triangle", art.draw_triangle),
        "5": ("Pyramid", art.draw_pyramid)
    }

    while True:
        print("\nSelect a shape to draw (enter 'q' to quit):")
        for key, (name, _) in shapes.items():
            print(f"  {key}: {name}")
        choice = input("Your choice: ").strip()

        if choice.lower() == 'q':
            print("Exiting the ASCII Art App. Goodbye!")
            break

        if choice not in shapes:
            print("Invalid choice. Please try again.")
            continue

        shape_name, draw_func = shapes[choice]
        try:
            if shape_name == "Square":
                width = get_positive_int("Enter the width of the square: ")
                symbol = get_symbol("Enter the drawing symbol: ")
                result = art.draw_square(width, symbol)
            elif shape_name == "Rectangle":
                width = get_positive_int("Enter the width of the rectangle: ")
                height = get_positive_int("Enter the height of the rectangle: ")
                symbol = get_symbol("Enter the drawing symbol: ")
                result = art.draw_rectangle(width, height, symbol)
            elif shape_name == "Circle":
                diameter = get_positive_int("Enter the diameter of the circle: ")
                symbol = get_symbol("Enter the drawing symbol: ")
                result = art.draw_circle(diameter, symbol)
            elif shape_name == "Triangle":
                width = get_positive_int("Enter the base width of the triangle: ")
                height = get_positive_int("Enter the height of the triangle: ")
                symbol = get_symbol("Enter the drawing symbol: ")
                result = art.draw_triangle(width, height, symbol)
            elif shape_name == "Pyramid":
                height = get_positive_int("Enter the height of the pyramid: ")
                symbol = get_symbol("Enter the drawing symbol: ")
                result = art.draw_pyramid(height, symbol)
            else:
                result = "Shape selection not valid!"

            print("\n" + result)
        except ValueError as ve:
            print(f"Error: {ve}")


if __name__ == "__main__":
    main()
