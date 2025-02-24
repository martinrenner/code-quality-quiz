from typing import Union
import math

class AsciiArt:
    """A class for generating various ASCII art shapes.
    
    This class provides methods to create different geometric shapes using ASCII characters.
    All methods validate inputs and return string representations of the shapes.
    """
    
    @staticmethod
    def _validate_inputs(dimensions: Union[tuple[int, ...], int], symbol: str) -> None:
        """Validates input parameters for all shape drawing methods.
        
        Args:
            dimensions: Integer or tuple of integers representing shape dimensions
            symbol: Character to draw the shape with
            
        Raises:
            ValueError: If dimensions are negative or symbol is empty/multiple characters
        """
        # Validate dimensions
        if isinstance(dimensions, tuple):
            if any(d <= 0 for d in dimensions):
                raise ValueError("All dimensions must be positive")
        elif dimensions <= 0:
            raise ValueError("Dimension must be positive")
            
        # Validate symbol
        if len(symbol) != 1:
            raise ValueError("Symbol must be exactly one character")

    def draw_square(self, width: int, symbol: str) -> str:
        """Draws a square with the specified width using the given symbol.
        
        Args:
            width: Width and height of the square
            symbol: Character to draw the square with
            
        Returns:
            String representation of the square
        """
        self._validate_inputs(width, symbol)
        return '\n'.join([symbol * width] * width)

    def draw_rectangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a rectangle with the specified dimensions using the given symbol.
        
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
        """Draws an approximate circle with the specified diameter using the given symbol.
        
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
                # Using the circle equation (x²/r² + y²/r² ≤ 1)
                if (x*x + y*y) <= radius * radius:
                    line.append(symbol)
                else:
                    line.append(' ')
            circle.append(''.join(line))
            
        return '\n'.join(circle)

    def draw_triangle(self, width: int, height: int, symbol: str) -> str:
        """Draws a right-angled triangle with the specified dimensions using the given symbol.
        
        Args:
            width: Width of the triangle
            height: Height of the triangle
            symbol: Character to draw the triangle with
            
        Returns:
            String representation of the triangle
        """
        self._validate_inputs((width, height), symbol)
        
        triangle = []
        for i in range(height):
            # Calculate number of symbols for current line
            symbols = math.ceil((i + 1) * (width / height))
            triangle.append(symbol * symbols)
            
        return '\n'.join(triangle)

    def draw_pyramid(self, height: int, symbol: str) -> str:
        """Draws a symmetrical pyramid with the specified height using the given symbol.
        
        Args:
            height: Height of the pyramid
            symbol: Character to draw the pyramid with
            
        Returns:
            String representation of the pyramid
        """
        self._validate_inputs(height, symbol)
        
        pyramid = []
        width = 2 * height - 1
        
        for i in range(height):
            # Calculate number of symbols and spaces for current line
            symbols = 2 * i + 1
            spaces = (width - symbols) // 2
            pyramid.append(' ' * spaces + symbol * symbols + ' ' * spaces)
            
        return '\n'.join(pyramid)


def main():
    """Main function to demonstrate the ASCII art generator."""
    ascii_art = AsciiArt()
    
    try:
        # Example usage
        print("Square (5x5):")
        print(ascii_art.draw_square(5, '#'))
        print("\nRectangle (6x4):")
        print(ascii_art.draw_rectangle(6, 4, '*'))
        print("\nCircle (diameter 7):")
        print(ascii_art.draw_circle(7, '@'))
        print("\nTriangle (5x5):")
        print(ascii_art.draw_triangle(5, 5, '+'))
        print("\nPyramid (height 4):")
        print(ascii_art.draw_pyramid(4, '^'))
        
    except ValueError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
