#!/usr/bin/env python3
"""
Console-based 2D ASCII Art Application

This application allows a user to generate various filled ASCII art shapes:
- Square
- Rectangle
- Circle (approximate)
- Right-Angled Triangle
- Pyramid

Each shape is created using a user-selected printable symbol and returns 
a multi-line string representing the shape.

The implementation follows clean architecture principles, is modular and
secure against invalid inputs, and meets the ISO/IEC 25010 quality standards.
"""

from math import sqrt
from typing import Callable


class AsciiArt:
    """
    A class providing static methods to draw various ASCII art shapes.
    """

    @staticmethod
    def _validate_dimension(value: int, name: str) -> None:
        """
        Validates that a given dimension is a positive integer.

        Args:
            value (int): The dimension value.
            name (str): The name of the dimension (for error messages).

        Raises:
            ValueError: If the dimension is not a positive integer.
        """
        if not isinstance(value, int) or value < 1:
            raise ValueError(f"{name} must be a positive integer.")

    @staticmethod
    def _validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a single printable character.

        Args:
            symbol (str): The symbol to use for drawing shapes.

        Raises:
            ValueError: If the symbol is not a single printable character.
        """
        if not isinstance(symbol, str) or len(symbol) != 1 or not symbol.isprintable():
            raise ValueError("Symbol must be a single printable character.")

    @staticmethod
    def draw_square(width: int, symbol: str) -> str:
        """
        Draws a filled square of a given width using the specified symbol.

        Args:
            width (int): The side length of the square.
            symbol (str): The symbol used to draw the square.

        Returns:
            str: A multi-line string representing the square.
        """
        AsciiArt._validate_dimension(width, "Width")
        AsciiArt._validate_symbol(symbol)

        # Build each line of the square and join them by newline.
        lines = [symbol * width for _ in range(width)]
        return "\n".join(lines)

    @staticmethod
    def draw_rectangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a filled rectangle using the specified width, height, and symbol.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol used to draw the rectangle.

        Returns:
            str: A multi-line string representing the rectangle.
        """
        AsciiArt._validate_dimension(width, "Width")
        AsciiArt._validate_dimension(height, "Height")
        AsciiArt._validate_symbol(symbol)

        lines = [symbol * width for _ in range(height)]
        return "\n".join(lines)

    @staticmethod
    def draw_circle(diameter: int, symbol: str) -> str:
        """
        Draws an approximate filled circle with a given diameter using the specified symbol.

        The algorithm checks each position in a grid and fills it if its center falls
        within the circle's radius.

        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol used to draw the circle.

        Returns:
            str: A multi-line string representing the approximate circle.
        """
        AsciiArt._validate_dimension(diameter, "Diameter")
        AsciiArt._validate_symbol(symbol)

        r = diameter / 2.0
        # Using center offset to more accurately fill the circle.
        center = r
        result = []
        for y in range(diameter):
            line = ""
            for x in range(diameter):
                # Calculate distance from the center of the current "pixel"
                distance = sqrt((x + 0.5 - center) ** 2 + (y + 0.5 - center) ** 2)
                if distance <= r:
                    line += symbol
                else:
                    line += " "
            result.append(line.rstrip())
        return "\n".join(result)

    @staticmethod
    def draw_triangle(width: int, height: int, symbol: str) -> str:
        """
        Draws a filled right-angled triangle with the right angle at the bottom-left.

        The triangle spans a rectangle of the given width and height. The number of
        symbols in each row is determined by the linear scaling from 1 symbol at the top
        row to 'width' symbols in the bottom row.

        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol used to draw the triangle.

        Returns:
            str: A multi-line string representing the right-angled triangle.
        """
        AsciiArt._validate_dimension(width, "Width")
        AsciiArt._validate_dimension(height, "Height")
        AsciiArt._validate_symbol(symbol)

        # Special case: if height is 1, simply output a single row.
        if height == 1:
            return symbol * width

        lines = []
        # i=0 is the top row, which should have 1 symbol; last row has 'width' symbols.
        for i in range(height):
            # Avoid division by zero; linearly interpolate number of symbols
            num_symbols = int(round((i / (height - 1)) * (width - 1))) + 1
            lines.append(symbol * num_symbols)
        return "\n".join(lines)

    @staticmethod
    def draw_pyramid(height: int, symbol: str) -> str:
        """
        Draws a symmetrical filled pyramid.

        For each level 'i' (1-indexed), the pyramid consists of (2 * i - 1) symbols
        centered by left-padding with (height - i) spaces.

        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol used to draw the pyramid.

        Returns:
            str: A multi-line string representing the pyramid.
        """
        AsciiArt._validate_dimension(height, "Height")
        AsciiArt._validate_symbol(symbol)

        lines = []
        for i in range(1, height + 1):
            spaces = " " * (height - i)
            symbols = symbol * (2 * i - 1)
            lines.append(spaces + symbols)
        return "\n".join(lines)


def get_integer_input(prompt: str) -> int:
    """
    Prompts the user for an integer input, re-prompting upon invalid input.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        int: The validated integer input.
    """
    while True:
        try:
            value = int(input(prompt))
            if value < 1:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_symbol_input(prompt: str) -> str:
    """
    Prompts the user for a symbol input and validates that it is a single printable character.

    Args:
        prompt (str): The input prompt to display.

    Returns:
        str: The validated symbol.
    """
    while True:
        symbol = input(prompt)
        try:
            AsciiArt._validate_symbol(symbol)
            return symbol
        except ValueError as e:
            print(e)


def main() -> None:
    """
    Runs the console-based interface for the ASCII Art application.
    Presents a menu, accepts user input, and displays the drawn ASCII art.
    """
    # Map menu options to corresponding functions along with required parameter prompts.
    menu_options = {
        "1": {
            "description": "Square",
            "function": lambda: print(
                "\n" + AsciiArt.draw_square(
                    get_integer_input("Enter side length: "),
                    get_symbol_input("Enter drawing symbol: ")
                )
            )
        },
        "2": {
            "description": "Rectangle",
            "function": lambda: print(
                "\n" + AsciiArt.draw_rectangle(
                    get_integer_input("Enter width: "),
                    get_integer_input("Enter height: "),
                    get_symbol_input("Enter drawing symbol: ")
                )
            )
        },
        "3": {
            "description": "Circle",
            "function": lambda: print(
                "\n" + AsciiArt.draw_circle(
                    get_integer_input("Enter diameter: "),
                    get_symbol_input("Enter drawing symbol: ")
                )
            )
        },
        "4": {
            "description": "Right-Angled Triangle",
            "function": lambda: print(
                "\n" + AsciiArt.draw_triangle(
                    get_integer_input("Enter base width: "),
                    get_integer_input("Enter height: "),
                    get_symbol_input("Enter drawing symbol: ")
                )
            )
        },
        "5": {
            "description": "Pyramid",
            "function": lambda: print(
                "\n" + AsciiArt.draw_pyramid(
                    get_integer_input("Enter height: "),
                    get_symbol_input("Enter drawing symbol: ")
                )
            )
        },
        "6": {
            "description": "Exit",
            "function": lambda: exit(0)
        }
    }

    while True:
        print("\n=== ASCII Art Generator ===")
        for key, option in menu_options.items():
            print(f"{key}. {option['description']}")
        choice = input("Select an option (1-6): ").strip()

        if choice in menu_options:
            try:
                # Execute the corresponding function.
                menu_options[choice]["function"]()
            except Exception as e:
                print(f"An error occurred: {e}")
        else:
            print("Invalid option. Please select a valid option (1-6).")


if __name__ == "__main__":
    main()
