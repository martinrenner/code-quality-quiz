"""
ASCII Art Generator Module

This module provides functions to generate various ASCII art shapes.
Each shape can be customized with different dimensions and symbols.
"""
from typing import Union, List
import math


def validate_input(dimensions: List[int], symbol: str) -> None:
    """
    Validates the input parameters for all drawing functions.
    
    Args:
        dimensions (List[int]): A list of dimension values to check.
        symbol (str): The symbol to be used for drawing.
        
    Raises:
        ValueError: If any dimension is non-positive or if symbol is empty.
        TypeError: If symbol is not a string or dimensions contain non-integers.
    """
    # Validate dimensions
    for dim in dimensions:
        if not isinstance(dim, int):
            raise TypeError(f"Dimensions must be integers, got {type(dim).__name__}")
        if dim <= 0:
            raise ValueError(f"Dimensions must be positive, got {dim}")
    
    # Validate symbol
    if not isinstance(symbol, str):
        raise TypeError(f"Symbol must be a string, got {type(symbol).__name__}")
    if not symbol:
        raise ValueError("Symbol cannot be empty")


def draw_square(width: int, symbol: str) -> str:
    """
    Draws a square filled with the specified symbol.
    
    Args:
        width (int): The width and height of the square.
        symbol (str): The symbol to use for drawing the square.
        
    Returns:
        str: A multi-line string representing the ASCII art square.
        
    Raises:
        ValueError: If width is non-positive or if symbol is empty.
        TypeError: If inputs have invalid types.
    """
    validate_input([width], symbol)
    
    # Generate the square by repeating the symbol
    row = symbol * width
    square = '\n'.join([row] * width)
    
    return square


def draw_rectangle(width: int, height: int, symbol: str) -> str:
    """
    Draws a rectangle filled with the specified symbol.
    
    Args:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        symbol (str): The symbol to use for drawing the rectangle.
        
    Returns:
        str: A multi-line string representing the ASCII art rectangle.
        
    Raises:
        ValueError: If width or height is non-positive or if symbol is empty.
        TypeError: If inputs have invalid types.
    """
    validate_input([width, height], symbol)
    
    # Generate the rectangle by repeating the symbol
    row = symbol * width
    rectangle = '\n'.join([row] * height)
    
    return rectangle


def draw_circle(diameter: int, symbol: str) -> str:
    """
    Draws an approximate circle filled with the specified symbol.
    
    Args:
        diameter (int): The diameter of the circle.
        symbol (str): The symbol to use for drawing the circle.
        
    Returns:
        str: A multi-line string representing the ASCII art circle.
        
    Raises:
        ValueError: If diameter is non-positive or if symbol is empty.
        TypeError: If inputs have invalid types.
    """
    validate_input([diameter], symbol)
    
    radius = diameter / 2
    center = radius - 0.5  # Adjust for better centering in console output
    
    # Create a grid and fill in circle points
    circle_lines = []
    for y in range(diameter):
        line = []
        for x in range(diameter):
            # Calculate if the point is inside the circle
            if (x - center) ** 2 + (y - center) ** 2 <= radius ** 2:
                line.append(symbol)
            else:
                line.append(' ')
        circle_lines.append(''.join(line))
    
    return '\n'.join(circle_lines)


def draw_triangle(width: int, height: int, symbol: str) -> str:
    """
    Draws a right-angled triangle filled with the specified symbol.
    
    Args:
        width (int): The base width of the triangle.
        height (int): The height of the triangle.
        symbol (str): The symbol to use for drawing the triangle.
        
    Returns:
        str: A multi-line string representing the ASCII art right-angled triangle.
        
    Raises:
        ValueError: If width or height is non-positive or if symbol is empty.
        TypeError: If inputs have invalid types.
    """
    validate_input([width, height], symbol)
    
    triangle_lines = []
    for i in range(1, height + 1):
        # Determine the number of symbols in the current line
        # This creates a right-angled triangle
        symbols_in_line = math.ceil((i / height) * width)
        triangle_lines.append(symbol * symbols_in_line)
    
    return '\n'.join(triangle_lines)


def draw_pyramid(height: int, symbol: str) -> str:
    """
    Draws a symmetrical pyramid filled with the specified symbol.
    
    Args:
        height (int): The height of the pyramid.
        symbol (str): The symbol to use for drawing the pyramid.
        
    Returns:
        str: A multi-line string representing the ASCII art pyramid.
        
    Raises:
        ValueError: If height is non-positive or if symbol is empty.
        TypeError: If inputs have invalid types.
    """
    validate_input([height], symbol)
    
    pyramid_lines = []
    width = 2 * height - 1  # The base width of the pyramid
    
    for i in range(1, height + 1):
        # Calculate the number of symbols in the current line of the pyramid
        symbols_count = 2 * i - 1
        # Calculate the number of spaces needed for centering
        spaces_count = (width - symbols_count) // 2
        
        # Create the line with proper spacing and symbols
        line = ' ' * spaces_count + symbol * symbols_count
        pyramid_lines.append(line)
    
    return '\n'.join(pyramid_lines)


# Object-Oriented Implementation
class AsciiArt:
    """
    A class for generating ASCII art shapes.
    
    This class provides methods to generate various ASCII art shapes,
    including squares, rectangles, circles, triangles, and pyramids.
    """
    
    @staticmethod
    def validate_input(dimensions: List[int], symbol: str) -> None:
        """
        Validates the input parameters for all drawing methods.
        
        Args:
            dimensions (List[int]): A list of dimension values to check.
            symbol (str): The symbol to be used for drawing.
            
        Raises:
            ValueError: If any dimension is non-positive or if symbol is empty.
            TypeError: If symbol is not a string or dimensions contain non-integers.
        """
        # Validate dimensions
        for dim in dimensions:
            if not isinstance(dim, int):
                raise TypeError(f"Dimensions must be integers, got {type(dim).__name__}")
            if dim <= 0:
                raise ValueError(f"Dimensions must be positive, got {dim}")
        
        # Validate symbol
        if not isinstance(symbol, str):
            raise TypeError(f"Symbol must be a string, got {type(symbol).__name__}")
        if not symbol:
            raise ValueError("Symbol cannot be empty")
    
    @classmethod
    def draw_square(cls, width: int, symbol: str) -> str:
        """
        Draws a square filled with the specified symbol.
        
        Args:
            width (int): The width and height of the square.
            symbol (str): The symbol to use for drawing the square.
            
        Returns:
            str: A multi-line string representing the ASCII art square.
            
        Raises:
            ValueError: If width is non-positive or if symbol is empty.
            TypeError: If inputs have invalid types.
        """
        cls.validate_input([width], symbol)
        
        row = symbol * width
        square = '\n'.join([row] * width)
        
        return square
    
    @classmethod
    def draw_rectangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a rectangle filled with the specified symbol.
        
        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            symbol (str): The symbol to use for drawing the rectangle.
            
        Returns:
            str: A multi-line string representing the ASCII art rectangle.
            
        Raises:
            ValueError: If width or height is non-positive or if symbol is empty.
            TypeError: If inputs have invalid types.
        """
        cls.validate_input([width, height], symbol)
        
        row = symbol * width
        rectangle = '\n'.join([row] * height)
        
        return rectangle
    
    @classmethod
    def draw_circle(cls, diameter: int, symbol: str) -> str:
        """
        Draws an approximate circle filled with the specified symbol.
        
        Args:
            diameter (int): The diameter of the circle.
            symbol (str): The symbol to use for drawing the circle.
            
        Returns:
            str: A multi-line string representing the ASCII art circle.
            
        Raises:
            ValueError: If diameter is non-positive or if symbol is empty.
            TypeError: If inputs have invalid types.
        """
        cls.validate_input([diameter], symbol)
        
        radius = diameter / 2
        center = radius - 0.5  # Adjust for better centering in console output
        
        # Create a grid and fill in circle points
        circle_lines = []
        for y in range(diameter):
            line = []
            for x in range(diameter):
                # Calculate if the point is inside the circle
                if (x - center) ** 2 + (y - center) ** 2 <= radius ** 2:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle_lines.append(''.join(line))
        
        return '\n'.join(circle_lines)
    
    @classmethod
    def draw_triangle(cls, width: int, height: int, symbol: str) -> str:
        """
        Draws a right-angled triangle filled with the specified symbol.
        
        Args:
            width (int): The base width of the triangle.
            height (int): The height of the triangle.
            symbol (str): The symbol to use for drawing the triangle.
            
        Returns:
            str: A multi-line string representing the ASCII art right-angled triangle.
            
        Raises:
            ValueError: If width or height is non-positive or if symbol is empty.
            TypeError: If inputs have invalid types.
        """
        cls.validate_input([width, height], symbol)
        
        triangle_lines = []
        for i in range(1, height + 1):
            # Determine the number of symbols in the current line
            symbols_in_line = math.ceil((i / height) * width)
            triangle_lines.append(symbol * symbols_in_line)
        
        return '\n'.join(triangle_lines)
    
    @classmethod
    def draw_pyramid(cls, height: int, symbol: str) -> str:
        """
        Draws a symmetrical pyramid filled with the specified symbol.
        
        Args:
            height (int): The height of the pyramid.
            symbol (str): The symbol to use for drawing the pyramid.
            
        Returns:
            str: A multi-line string representing the ASCII art pyramid.
            
        Raises:
            ValueError: If height is non-positive or if symbol is empty.
            TypeError: If inputs have invalid types.
        """
        cls.validate_input([height], symbol)
        
        pyramid_lines = []
        width = 2 * height - 1  # The base width of the pyramid
        
        for i in range(1, height + 1):
            # Calculate the number of symbols in the current line of the pyramid
            symbols_count = 2 * i - 1
            # Calculate the number of spaces needed for centering
            spaces_count = (width - symbols_count) // 2
            
            # Create the line with proper spacing and symbols
            line = ' ' * spaces_count + symbol * symbols_count
            pyramid_lines.append(line)
        
        return '\n'.join(pyramid_lines)


# Example usage
if __name__ == "__main__":
    # Function-based approach
    print("Square (Function):")
    print(draw_square(5, "#"))
    print("\nRectangle (Function):")
    print(draw_rectangle(8, 4, "*"))
    print("\nCircle (Function):")
    print(draw_circle(10, "O"))
    print("\nTriangle (Function):")
    print(draw_triangle(10, 5, "+"))
    print("\nPyramid (Function):")
    print(draw_pyramid(5, "^"))
    
    # Object-oriented approach
    print("\n\nSquare (OOP):")
    print(AsciiArt.draw_square(5, "#"))
    print("\nRectangle (OOP):")
    print(AsciiArt.draw_rectangle(8, 4, "*"))
    print("\nCircle (OOP):")
    print(AsciiArt.draw_circle(10, "O"))
    print("\nTriangle (OOP):")
    print(AsciiArt.draw_triangle(10, 5, "+"))
    print("\nPyramid (OOP):")
    print(AsciiArt.draw_pyramid(5, "^"))
