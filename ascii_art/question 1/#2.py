#!/usr/bin/env python3
"""
ASCII Art Generator

A console-based application to generate ASCII art shapes with customizable symbols.
Implements various geometric shapes as ASCII art with a user-friendly interface.
"""

import math
import re
from typing import Callable, Dict, List, Tuple, Union


class AsciiArt:
    """Class for generating ASCII art shapes.

    This class provides methods to create various ASCII art shapes using 
    customizable symbols. Each shape is returned as a multi-line string.
    """

    @staticmethod
    def validate_input(size: Union[int, List[int]], symbol: str) -> Tuple[bool, str]:
        """Validates the input parameters for all drawing functions.

        Args:
            size: Integer or list of integers representing dimensions of the shape.
            symbol: Character to use for drawing the shape.

        Returns:
            Tuple containing:
                - Boolean indicating if input is valid
                - String with error message if invalid, or empty string if valid
        """
        # Validate symbol (must be a single printable character)
        if not symbol or len(symbol) != 1:
            return False, "Symbol must be a single character."
        
        if not re.match(r'[\x20-\x7E]', symbol):  # Basic printable ASCII range
            return False, "Symbol must be a printable character."
        
        # Validate size parameters
        if isinstance(size, list):
            for dimension in size:
                if not isinstance(dimension, int) or dimension <= 0:
                    return False, "Dimensions must be positive integers."
                if dimension > 100:  # Reasonable upper limit to prevent excessive resource usage
                    return False, "Dimension too large (max 100)."
        else:
            if not isinstance(size, int) or size <= 0:
                return False, "Size must be a positive integer."
            if size > 100:  # Reasonable upper limit
                return False, "Size too large (max 100)."
                
        return True, ""

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """Draws a square with the specified width and symbol.

        Args:
            width: Width and height of the square.
            symbol: Character to use for drawing the square.

        Returns:
            Multi-line string representing the ASCII art square.

        Raises:
            ValueError: If input parameters are invalid.
        """
        valid, error_msg = cls.validate_input(width, symbol)
        if not valid:
            raise ValueError(error_msg)
            
        row = symbol * width
        return '\n'.join([row] * width)

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """Draws a rectangle with the specified dimensions and symbol.

        Args:
            width: Width of the rectangle.
            height: Height of the rectangle.
            symbol: Character to use for drawing the rectangle.

        Returns:
            Multi-line string representing the ASCII art rectangle.

        Raises:
            ValueError: If input parameters are invalid.
        """
        valid, error_msg = cls.validate_input([width, height], symbol)
        if not valid:
            raise ValueError(error_msg)
            
        row = symbol * width
        return '\n'.join([row] * height)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """Draws a right-angled triangle with the specified dimensions and symbol.

        Args:
            width: Width of the triangle.
            height: Height of the triangle.
            symbol: Character to use for drawing the triangle.

        Returns:
            Multi-line string representing the ASCII art triangle.

        Raises:
            ValueError: If input parameters are invalid.
        """
        valid, error_msg = cls.validate_input([width, height], symbol)
        if not valid:
            raise ValueError(error_msg)
            
        result = []
        for i in range(height):
            # Calculate how many symbols to draw in each row
            # This creates a linear interpolation from 1 to width symbols
            symbols_in_row = max(1, round((i + 1) * width / height))
            result.append(symbol * symbols_in_row)
            
        return '\n'.join(result)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """Draws a symmetrical pyramid with the specified height and symbol.

        Args:
            height: Height of the pyramid.
            symbol: Character to use for drawing the pyramid.

        Returns:
            Multi-line string representing the ASCII art pyramid.

        Raises:
            ValueError: If input parameters are invalid.
        """
        valid, error_msg = cls.validate_input(height, symbol)
        if not valid:
            raise ValueError(error_msg)
            
        result = []
        max_width = 2 * height - 1
        
        for i in range(height):
            symbols_in_row = 2 * i + 1
            padding = (max_width - symbols_in_row) // 2
            result.append(' ' * padding + symbol * symbols_in_row)
            
        return '\n'.join(result)

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """Draws an approximate circle with the specified diameter and symbol.

        Args:
            diameter: Diameter of the circle.
            symbol: Character to use for drawing the circle.

        Returns:
            Multi-line string representing the ASCII art circle.

        Raises:
            ValueError: If input parameters are invalid.
        """
        valid, error_msg = cls.validate_input(diameter, symbol)
        if not valid:
            raise ValueError(error_msg)
            
        result = []
        radius = diameter / 2
        
        # Using the equation of a circle: (x - h)^2 + (y - k)^2 = r^2
        # where (h, k) is the center of the circle and r is the radius
        for y in range(diameter):
            row = []
            for x in range(diameter):
                # Adjust coordinates to center the circle
                dx = x - radius + 0.5
                dy = y - radius + 0.5
                
                # Check if point is within the circle
                if dx * dx + dy * dy <= radius * radius:
                    row.append(symbol)
                else:
                    row.append(' ')
            result.append(''.join(row))
            
        return '\n'.join(result)


def display_menu() -> None:
    """Displays the main menu of the application."""
    print("\nASCII Art Generator")
    print("===================")
    print("1. Draw a Square")
    print("2. Draw a Rectangle")
    print("3. Draw a Circle")
    print("4. Draw a Triangle")
    print("5. Draw a Pyramid")
    print("0. Exit")


def get_int_input(prompt: str, min_value: int = 1, max_value: int = 100) -> int:
    """Gets an integer input from the user with validation.

    Args:
        prompt: Message to display to the user.
        min_value: Minimum acceptable value (inclusive).
        max_value: Maximum acceptable value (inclusive).

    Returns:
        Valid integer input from the user.
    """
    while True:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            print(f"Please enter a value between {min_value} and {max_value}.")
        except ValueError:
            print("Please enter a valid integer.")


def get_symbol_input(prompt: str = "Enter a symbol to use: ") -> str:
    """Gets a symbol input from the user with validation.

    Args:
        prompt: Message to display to the user.

    Returns:
        Valid symbol from the user.
    """
    while True:
        symbol = input(prompt)
        if len(symbol) == 1 and re.match(r'[\x20-\x7E]', symbol):
            return symbol
        print("Please enter a single printable character.")


def main() -> None:
    """Main application function implementing the user interface."""
    ascii_art = AsciiArt()
    
    while True:
        display_menu()
        choice = input("\nEnter your choice (0-5): ")
        
        if choice == '0':
            print("Thank you for using ASCII Art Generator!")
            break
            
        try:
            if choice == '1':  # Square
                width = get_int_input("Enter the width of the square: ")
                symbol = get_symbol_input()
                result = ascii_art.draw_square(width, symbol)
                
            elif choice == '2':  # Rectangle
                width = get_int_input("Enter the width of the rectangle: ")
                height = get_int_input("Enter the height of the rectangle: ")
                symbol = get_symbol_input()
                result = ascii_art.draw_rectangle(width, height, symbol)
                
            elif choice == '3':  # Circle
                diameter = get_int_input("Enter the diameter of the circle: ")
                symbol = get_symbol_input()
                result = ascii_art.draw_circle(diameter, symbol)
                
            elif choice == '4':  # Triangle
                width = get_int_input("Enter the width of the triangle: ")
                height = get_int_input("Enter the height of the triangle: ")
                symbol = get_symbol_input()
                result = ascii_art.draw_triangle(width, height, symbol)
                
            elif choice == '5':  # Pyramid
                height = get_int_input("Enter the height of the pyramid: ")
                symbol = get_symbol_input()
                result = ascii_art.draw_pyramid(height, symbol)
                
            else:
                print("Invalid choice. Please enter a number between 0 and 5.")
                continue
                
            # Display the result
            print("\nYour ASCII Art:")
            print(result)
            
        except ValueError as e:
            print(f"Error: {e}")
        
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
