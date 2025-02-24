
from typing import Union
import math

class AsciiArt:
    """A class for creating various ASCII art shapes.
    
    This class provides methods to draw different geometric shapes using ASCII characters.
    All methods perform input validation and return formatted multi-line strings.
    """
    
    @staticmethod
    def _validate_input(dimension: Union[int, tuple], symbol: str) -> None:
        """Validates input parameters for all drawing methods.
        
        Args:
            dimension: Integer or tuple of integers representing shape dimensions
            symbol: Character to use for drawing
            
        Raises:
            ValueError: If dimensions are negative or symbol is empty/multiple characters
        """
        if isinstance(dimension, tuple):
            if any(d <= 0 for d in dimension):
                raise ValueError("Dimensions must be positive integers")
        elif dimension <= 0:
            raise ValueError("Dimensions must be positive integers")
            
        if len(symbol) != 1:
            raise ValueError("Symbol must be exactly one character")

    def draw_square(self, width: int, symbol: str) -> str:
        """Draws a square with the specified width using the given symbol.
        
        Args:
            width: The width and height of the square
            symbol: The character to use for drawing
            
        Returns:
            A string containing the ASCII art square
        """
        self._validate_input(width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a rectangle with the specified dimensions using the given symbol.
        
        Args:
            width: The width of the rectangle
            height: The height of the rectangle
            symbol: The character to use for drawing
            
        Returns:
            A string containing the ASCII art rectangle
        """
        self._validate_input((width, height), symbol)
        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """Draws an approximate circle with the specified diameter using the given symbol.
        
        Args:
            diameter: The diameter of the circle
            symbol: The character to use for drawing
            
        Returns:
            A string containing the ASCII art circle
        """
        self._validate_input(diameter, symbol)
        
        radius = diameter // 2
        circle = []
        
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Using the circle equation (x²/a² + y²/b² ≤ 1)
                if x*x + y*y <= radius*radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle.append(''.join(line))
            
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a right-angled triangle with the specified dimensions using the given symbol.
        
        Args:
            width: The width of the triangle
            height: The height of the triangle
            symbol: The character to use for drawing
            
        Returns:
            A string containing the ASCII art triangle
        """
        self._validate_input((width, height), symbol)
        
        triangle = []
        for i in range(height):
            # Calculate symbols for current row based on height ratio
            symbols = int((i + 1) * width / height)
            triangle.append(symbol * symbols)
            
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """Draws a symmetrical pyramid with the specified height using the given symbol.
        
        Args:
            height: The height of the pyramid
            symbol: The character to use for drawing
            
        Returns:
            A string containing the ASCII art pyramid
        """
        self._validate_input(height, symbol)
        
        pyramid = []
        for i in range(height):
            # Calculate padding and symbols for current row
            spaces = ' ' * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid.append(f"{spaces}{symbols}")
            
        return '\n'.join(pyramid)


def main():
    """Main function to demonstrate the ASCII art functionality."""
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("Square (5x5):")
        print(ascii_art.draw_square(5, '#'))
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, '*'))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, '@'))
        print("\nTriangle (5x3):")
        print(ascii_art.draw_triangle(5, 3, '+'))
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, '$'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
