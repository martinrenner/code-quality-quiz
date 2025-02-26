"""
ASCII Art Generator

This module provides functionality to generate various ASCII art shapes
such as squares, rectangles, circles, triangles, and pyramids.

Author: AI Assistant
Version: 1.0.0
"""

import math
from typing import Union, List


class AsciiArt:
    """
    A class for generating ASCII art shapes.
    
    This class provides methods to create various shapes like squares,
    rectangles, circles, triangles, and pyramids using ASCII characters.
    """

    @staticmethod
    def validate_input(dimension: int, min_value: int = 1, max_value: int = 100) -> None:
        """
        Validates that the input dimension is within an acceptable range.
        
        Args:
            dimension (int): The dimension to validate.
            min_value (int, optional): Minimum acceptable value. Defaults to 1.
            max_value (int, optional): Maximum acceptable value. Defaults to 100.
            
        Raises:
            ValueError: If the dimension is not within the acceptable range.
            TypeError: If the dimension is not an integer.
        """
        if not isinstance(dimension, int):
            raise TypeError(f"Dimension must be an integer, got {type(dimension).__name__}")
        if dimension < min_value or dimension > max_value:
            raise ValueError(f"Dimension must be between {min_value} and {max_value}, got {dimension}")

    @staticmethod
    def validate_symbol(symbol: str) -> None:
        """
        Validates that the symbol is a single printable character.
        
        Args:
            symbol (str): The symbol to validate.
            
        Raises:
            ValueError: If the symbol is not exactly one character.
            TypeError: If the symbol is not a string.
        """
        if not isinstance(symbol, str):
            raise TypeError(f"Symbol must be a string, got {type(symbol).__name__}")
        if len(symbol) != 1:
            raise ValueError(f"Symbol must be a single character, got '{symbol}'")
        if not symbol.isprintable():
            raise ValueError(f"Symbol must be a printable character, got '{symbol}'")

    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.
        
        Args:
            width (int): The width and height of the square.
            symbol (str): The character to use for drawing.
            
        Returns:
            str: A multi-line string representing the ASCII art square.
            
        Raises:
            ValueError: If width is less than 1 or greater than 100.
            ValueError: If symbol is not exactly one character.
        """
        cls.validate_input(width)
        cls.validate_symbol(symbol)
        
        row = symbol * width
        return '\n'.join([row for _ in range(width)])

    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The character to use for drawing.
            
        Returns:
            str: A multi-line string representing the ASCII art rectangle.
            
        Raises:
            ValueError: If width or height is less than 1 or greater than 100.
            ValueError: If symbol is not exactly one character.
        """
        cls.validate_input(width)
        cls.validate_input(height)
        cls.validate_symbol(symbol)
        
        row = symbol * width
        return '\n'.join([row for _ in range(height)])

    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximation of a circle filled with the specified symbol.
        
        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The character to use for drawing.
            
        Returns:
            str: A multi-line string representing the ASCII art circle.
            
        Raises:
            ValueError: If diameter is less than 1 or greater than 100.
            ValueError: If symbol is not exactly one character.
        """
        cls.validate_input(diameter)
        cls.validate_symbol(symbol)
        
        # Handle special cases for small diameters
        if diameter == 1:
            return symbol
        if diameter == 2:
            return symbol * 2 + '\n' + symbol * 2
            
        radius = diameter // 2
        result = []
        
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Using the circle equation: x² + y² ≤ r²
                # Add a small adjustment for better appearance
                distance = math.sqrt(x*x + y*y)
                if distance <= radius + 0.5:
                    line.append(symbol)
                else:
                    line.append(' ')
            result.append(''.join(line))
        
        return '\n'.join(result)

    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.
        
        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The character to use for drawing.
            
        Returns:
            str: A multi-line string representing the ASCII art triangle.
            
        Raises:
            ValueError: If width or height is less than 1 or greater than 100.
            ValueError: If symbol is not exactly one character.
        """
        cls.validate_input(width)
        cls.validate_input(height)
        cls.validate_symbol(symbol)
        
        result = []
        for i in range(height):
            # Calculate how many symbols to print on this line
            # based on the ratio of current height to total height
            symbols_to_print = max(1, round((i + 1) / height * width))
            result.append(symbol * symbols_to_print)
        
        return '\n'.join(result)

    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.
        
        Args:
            height (int): The height of the pyramid.
            symbol (str): The character to use for drawing.
            
        Returns:
            str: A multi-line string representing the ASCII art pyramid.
            
        Raises:
            ValueError: If height is less than 1 or greater than 100.
            ValueError: If symbol is not exactly one character.
        """
        cls.validate_input(height)
        cls.validate_symbol(symbol)
        
        result = []
        width = 2 * height - 1  # Maximum width at the base
        
        for i in range(height):
            # Number of symbols on current line
            symbols = 2 * i + 1
            # Padding on each side
            padding = (width - symbols) // 2
            
            line = ' ' * padding + symbol * symbols + ' ' * padding
            result.append(line)
        
        return '\n'.join(result)


def main() -> None:
    """
    Main function to run the ASCII Art Generator application.
    
    Provides a command-line interface for users to generate different ASCII shapes.
    """
    print("=== ASCII Art Generator ===")
    
    while True:
        print("\nChoose a shape to draw:")
        print("1. Square")
        print("2. Rectangle")
        print("3. Circle")
        print("4. Right-angled Triangle")
        print("5. Pyramid")
        print("0. Exit")
        
        try:
            choice = int(input("Enter your choice (0-5): ").strip())
            
            if choice == 0:
                print("Thank you for using ASCII Art Generator. Goodbye!")
                break
                
            if choice < 1 or choice > 5:
                print("Invalid choice. Please enter a number between 0 and 5.")
                continue
                
            symbol = input("Enter a single character to use for drawing: ")
            
            try:
                if choice == 1:  # Square
                    width = int(input("Enter the width of the square: "))
                    print("\nResult:")
                    print(AsciiArt.draw_square(width, symbol))
                    
                elif choice == 2:  # Rectangle
                    width = int(input("Enter the width of the rectangle: "))
                    height = int(input("Enter the height of the rectangle: "))
                    print("\nResult:")
                    print(AsciiArt.draw_rectangle(width, height, symbol))
                    
                elif choice == 3:  # Circle
                    diameter = int(input("Enter the diameter of the circle: "))
                    print("\nResult:")
                    print(AsciiArt.draw_circle(diameter, symbol))
                    
                elif choice == 4:  # Right-angled Triangle
                    width = int(input("Enter the base width of the triangle: "))
                    height = int(input("Enter the height of the triangle: "))
                    print("\nResult:")
                    print(AsciiArt.draw_triangle(width, height, symbol))
                    
                elif choice == 5:  # Pyramid
                    height = int(input("Enter the height of the pyramid: "))
                    print("\nResult:")
                    print(AsciiArt.draw_pyramid(height, symbol))
                    
            except (ValueError, TypeError) as e:
                print(f"Error: {e}")
                
        except ValueError:
            print("Please enter a valid number.")
            
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
