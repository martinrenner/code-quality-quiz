"""
ASCII Art Generator

This module provides functionality to generate various ASCII art shapes
using specified symbols. It follows clean architecture principles and
adheres to ISO/IEC 25010 quality standards.
"""
from math import sqrt


class AsciiArt:
    """
    A class that provides methods to generate various ASCII art shapes.
    
    Each method returns a multi-line string representation of the requested shape
    filled with the specified symbol.
    """
    
    @staticmethod
    def validate_input(dimensions, symbol):
        """
        Validate input parameters for all drawing methods.
        
        Args:
            dimensions (list): List of dimension parameters (width, height, etc.)
            symbol (str): Symbol to use for drawing
            
        Raises:
            ValueError: If dimensions are not positive integers or symbol is not a single character
        """
        # Validate dimensions
        for dim in dimensions:
            if not isinstance(dim, int) or dim <= 0:
                raise ValueError("Dimensions must be positive integers")
        
        # Validate symbol
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character")
    
    def draw_square(self, width: int, symbol: str) -> str:
        """
        Draw a square filled with the specified symbol.
        
        Args:
            width (int): Width and height of the square
            symbol (str): Symbol to use for drawing
            
        Returns:
            str: Multi-line string representation of the square
            
        Raises:
            ValueError: If width is not a positive integer or symbol is not a single character
        """
        self.validate_input([width], symbol)
        
        # Create a row of symbols with the given width
        row = symbol * width
        
        # Repeat the row for 'width' times to create a square
        square = '\n'.join([row] * width)
        
        return square
    
    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draw a rectangle filled with the specified symbol.
        
        Args:
            width (int): Width of the rectangle
            height (int): Height of the rectangle
            symbol (str): Symbol to use for drawing
            
        Returns:
            str: Multi-line string representation of the rectangle
            
        Raises:
            ValueError: If dimensions are not positive integers or symbol is not a single character
        """
        self.validate_input([width, height], symbol)
        
        # Create a row of symbols with the given width
        row = symbol * width
        
        # Repeat the row for 'height' times to create a rectangle
        rectangle = '\n'.join([row] * height)
        
        return rectangle
    
    def draw_circle(self, diameter: int, symbol: str) -> str:
        """
        Draw an approximate circle filled with the specified symbol.
        
        Args:
            diameter (int): Diameter of the circle
            symbol (str): Symbol to use for drawing
            
        Returns:
            str: Multi-line string representation of the circle
            
        Raises:
            ValueError: If diameter is not a positive integer or symbol is not a single character
        """
        self.validate_input([diameter], symbol)
        
        radius = diameter / 2
        # Calculate center point (using 0-based indexing)
        center_x = radius - 0.5
        center_y = radius - 0.5
        
        circle_rows = []
        
        # For each row in the output
        for y in range(diameter):
            row = ""
            # For each column in the output
            for x in range(diameter):
                # Calculate distance from center
                distance = sqrt((x - center_x) ** 2 + (y - center_y) ** 2)
                # If point is within the radius, add symbol, otherwise add space
                if distance <= radius:
                    row += symbol
                else:
                    row += " "
            circle_rows.append(row)
        
        return '\n'.join(circle_rows)
    
    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """
        Draw a right-angled triangle filled with the specified symbol.
        
        Args:
            width (int): Width of the triangle base
            height (int): Height of the triangle
            symbol (str): Symbol to use for drawing
            
        Returns:
            str: Multi-line string representation of the triangle
            
        Raises:
            ValueError: If dimensions are not positive integers or symbol is not a single character
        """
        self.validate_input([width, height], symbol)
        
        triangle_rows = []
        
        # Calculate how much to increment the width for each row
        width_increment = width / height
        
        # For each row in the output
        for i in range(height):
            # Calculate width of current row
            current_width = int((i + 1) * width_increment)
            # Add row with current width
            triangle_rows.append(symbol * current_width)
        
        return '\n'.join(triangle_rows)
    
    def draw_pyramid(self, height: int, symbol: str) -> str:
        """
        Draw a symmetrical pyramid filled with the specified symbol.
        
        Args:
            height (int): Height of the pyramid
            symbol (str): Symbol to use for drawing
            
        Returns:
            str: Multi-line string representation of the pyramid
            
        Raises:
            ValueError: If height is not a positive integer or symbol is not a single character
        """
        self.validate_input([height], symbol)
        
        pyramid_rows = []
        
        # For each row in the pyramid
        for i in range(height):
            # Calculate spaces on each side and symbols in the middle
            spaces = ' ' * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            
            # Construct the row with proper spacing and symbols
            pyramid_rows.append(spaces + symbols)
        
        return '\n'.join(pyramid_rows)


def main():
    """
    Main function to demonstrate the ASCII Art functionality.
    """
    art = AsciiArt()
    
    print("ASCII Art Generator\n")
    print("1. Square")
    print("2. Rectangle")
    print("3. Circle")
    print("4. Right-angled Triangle")
    print("5. Pyramid")
    print("6. Exit\n")
    
    while True:
        try:
            choice = int(input("Choose a shape (1-6): "))
            
            if choice == 6:
                print("Goodbye!")
                break
                
            symbol = input("Enter a symbol to use (single character): ")
            
            if choice == 1:
                width = int(input("Enter width: "))
                print("\n" + art.draw_square(width, symbol) + "\n")
                
            elif choice == 2:
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                print("\n" + art.draw_rectangle(width, height, symbol) + "\n")
                
            elif choice == 3:
                diameter = int(input("Enter diameter: "))
                print("\n" + art.draw_circle(diameter, symbol) + "\n")
                
            elif choice == 4:
                width = int(input("Enter width: "))
                height = int(input("Enter height: "))
                print("\n" + art.draw_triangle(width, height, symbol) + "\n")
                
            elif choice == 5:
                height = int(input("Enter height: "))
                print("\n" + art.draw_pyramid(height, symbol) + "\n")
                
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except ValueError as e:
            if "Dimensions must be" in str(e) or "Symbol must be" in str(e):
                print(f"Error: {e}")
            else:
                print("Invalid input. Please enter numeric values for dimensions.")
                
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
