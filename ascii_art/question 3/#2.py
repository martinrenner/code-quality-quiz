
from typing import Union
import math

class AsciiArt:
    """A class for creating ASCII art shapes.
    
    This class provides methods to draw various geometric shapes using ASCII characters.
    All methods validate inputs and return string representations of the shapes.
    """
    
    @staticmethod
    def _validate_inputs(size: Union[int, tuple], symbol: str) -> None:
        """Validates input parameters for all drawing methods.
        
        Args:
            size: Integer or tuple of integers representing dimensions
            symbol: Single character to draw the shape
            
        Raises:
            ValueError: If inputs are invalid
        """
        # Validate dimensions
        if isinstance(size, tuple):
            if not all(isinstance(x, int) and x > 0 for x in size):
                raise ValueError("Dimensions must be positive integers")
        elif not isinstance(size, int) or size <= 0:
            raise ValueError("Dimension must be a positive integer")
            
        # Validate symbol
        if not isinstance(symbol, str) or len(symbol) != 1:
            raise ValueError("Symbol must be a single character")

    def draw_square(self, width: int, symbol: str) -> str:
        """Draws a square with the specified width and symbol.
        
        Args:
            width: Width and height of the square
            symbol: Character to draw the square with
            
        Returns:
            String representation of the square
        """
        self._validate_inputs(width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a rectangle with specified dimensions.
        
        Args:
            width: Width of the rectangle
            height: Height of the rectangle
            symbol: Character to draw the rectangle with
            
        Returns:
            String representation of the rectangle
        """
        self._validate_inputs((width, height), symbol)
        return '\n'.join([symbol * width] * height)

    def draw_circle(self, diameter: int, symbol: str) -> str:
        """Draws an approximate circle with specified diameter.
        
        Args:
            diameter: Diameter of the circle
            symbol: Character to draw the circle with
            
        Returns:
            String representation of the circle
        """
        self._validate_inputs(diameter, symbol)
        radius = diameter // 2
        circle = []
        
        for y in range(-radius, radius + 1):
            line = []
            for x in range(-radius, radius + 1):
                # Using the circle equation: x² + y² ≤ r²
                if x*x + y*y <= radius*radius + radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle.append(''.join(line))
            
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a right-angled triangle.
        
        Args:
            width: Base width of the triangle
            height: Height of the triangle
            symbol: Character to draw the triangle with
            
        Returns:
            String representation of the triangle
        """
        self._validate_inputs((width, height), symbol)
        triangle = []
        
        for i in range(height):
            # Calculate symbols for current row using linear interpolation
            symbols = math.ceil((i + 1) * (width / height))
            triangle.append(symbol * symbols)
            
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """Draws a symmetrical pyramid.
        
        Args:
            height: Height of the pyramid
            symbol: Character to draw the pyramid with
            
        Returns:
            String representation of the pyramid
        """
        self._validate_inputs(height, symbol)
        pyramid = []
        
        for i in range(height):
            # Calculate padding and symbols for current row
            spaces = ' ' * (height - i - 1)
            symbols = symbol * (2 * i + 1)
            pyramid.append(spaces + symbols)
            
        return '\n'.join(pyramid)


def main():
    """Main function to demonstrate the ASCII art functionality."""
    try:
        ascii_art = AsciiArt()
        
        # Example usage
        print("\nSquare (5x5):")
        print(ascii_art.draw_square(5, '#'))
        
        print("\nRectangle (6x3):")
        print(ascii_art.draw_rectangle(6, 3, '*'))
        
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, '@'))
        
        print("\nTriangle (width 5, height 3):")
        print(ascii_art.draw_triangle(5, 3, '+'))
        
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, '$'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
